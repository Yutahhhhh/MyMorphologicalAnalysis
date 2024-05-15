#!/bin/bash

# CSVファイルを作成（既存の場合でも大丈夫）
touch input.csv
touch output.csv

exec "$@"
