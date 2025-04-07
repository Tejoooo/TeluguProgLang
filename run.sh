#!/bin/bash

FILE=${1:-sample.tl}

echo "📜 Running TeluguLang on: $FILE"
echo "=============================="
python3 main.py "$FILE"
