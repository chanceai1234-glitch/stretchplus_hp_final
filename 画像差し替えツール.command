#!/bin/bash
cd "$(dirname "$0")"

# Kill any existing process on port 8000 just in case
lsof -t -i tcp:8000 | xargs kill -9 2>/dev/null

echo "ブラウザで画像差し替えツールを起動しています..."
python3 image_uploader.py
