# My Morphological Analysis

このリポジトリは、GiNZAを使用した日本語形態素解析と固有名詞マスキングを行うPythonスクリプトを含むDockerプロジェクトです。

## 機能

- 日本語形態素解析
- CSV内の固有名詞マスキング

## 使用技術

- Python 3.8
- SpaCy
- GiNZA
- pandas
- Docker

## セットアップ

### 前提条件

- Dockerがインストールされていること

### 手順

1. このリポジトリをCloneします

 ```bash
 git clone https://github.com/Yutahhhhh/MyMorphologicalAnalysis.git
 cd MyMorphologicalAnalysis
 ```

 2. Dockerのセットアップと起動

```bash
docker-compose build
docker-compose run ginza-nlp
```

3. input.csvに、ヘッダー付きのデータを貼り付けます。

4. 以下のコマンドで実行

```bash
python mask_entities.py input.csv output.csv
```