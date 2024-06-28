#!/bin/bash

# 拡張機能のリストファイルのパス
EXTENSIONS_FILE="extensions-list.txt"

# ファイルが存在するかチェック
if [ ! -f "$EXTENSIONS_FILE" ]; then
    echo "拡張機能のリストファイルが見つかりません: $EXTENSIONS_FILE"
    exit 1
fi

# 拡張機能を1つずつインストール
while IFS= read -r extension
do
    echo "Installing extension: $extension"
    code --install-extension "$extension"
done < "$EXTENSIONS_FILE"
