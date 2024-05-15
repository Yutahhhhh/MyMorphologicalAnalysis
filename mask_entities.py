import pandas as pd
import spacy
from tqdm import tqdm

def mask_entities_in_column(text, nlp):
    doc = nlp(text)
    masked_text = text

    # マスク対象と置換するEntityのマッピング
    entity_mask_map = {
        "PERSON": "[Masked_PERSON]",
        "GPE": "[Masked_GPE]",
        "LOC": "[Masked_LOC]",
        "ORG": "[Masked_ORG]",
        "GOE_Other": "[Masked_GOE_Other]",
        "School": "[Masked_School]",
        "Company": "[Masked_Company]",
        "Museum": "[Masked_Museum]",
        "Sports_Facility": "[Masked_Sports_Facility]",
        "Dish": "[Masked_Dish]",
        "Amusement_Park": "[Masked_Amusement_Park]",
        "Road": "[Masked_Road]",
        "Clothing": "[Masked_Clothing]",
        "Broadcast_Program": "[Masked_Broadcast_Program]",
        "International_Organization": "[Masked_International_Organization]",
        "Product_Other": "[Masked_Product_Other]",
    }

    # テキストを置換した時に文字列の長さが変わらないように、後ろからEntityを処理する
    for ent in sorted(doc.ents, key=lambda e: e.start_char, reverse=True):
        # 置換する
        if ent.label_ in entity_mask_map:
            masked_text = masked_text[:ent.start_char] + entity_mask_map[ent.label_] + masked_text[ent.end_char:]

    return masked_text

def mask_entities_in_csv(df, nlp):
    print("Masking entities in CSV...")
    # 各列を処理
    for column in df.columns:
        if df[column].dtype == 'object':  # Process only string columns
            print(f"Processing column: {column}")
            # プログレスバーの表示&初期化
            for index, text in tqdm(df[column].items(), total=df.shape[0], desc=f"Masking {column}"):
                if isinstance(text, str):
                    df.at[index, column] = mask_entities_in_column(text, nlp)
    return df

def main(input_csv, output_csv):
    print("Starting the masking process...")

    try:
        nlp = spacy.load('ja_ginza')
        print("Loaded GiNZA model successfully.")
    except Exception as e:
        print(f"Error loading GiNZA model: {e}")
        return
    
    # CSVを読み込む
    try:
        df = pd.read_csv(input_csv)
        print("Read CSV file successfully:")
        print(df.head())
    except Exception as e:
        print(f"Failed to read CSV file: {e}")
        return
    
    # CSVの各列のEntityをマスクする
    df_masked = mask_entities_in_csv(df, nlp)
    
    # 結果をCSVに書き込む
    try:
        df_masked.to_csv(output_csv, index=False)
        print(f"Successfully wrote output to {output_csv}")
    except Exception as e:
        print(f"Failed to write output file: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python mask_entities.py <input_file.csv> <output_file.csv>")
