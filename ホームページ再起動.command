#!/bin/bash
echo "==============================================="
echo "ホームページ（テスト環境）自動復旧システム"
echo "==============================================="

# 1. Open Docker Desktop application
echo "1. パソコンの奥にあるDockerシステムを起動しています..."
open -a Docker

echo "システムが完全に立ち上がるまで約30秒〜1分ほどお待ちください..."

# 2. Wait until Docker daemon is fully responsive before trying to boot WP
while ! docker info > /dev/null 2>&1; do
    printf "."
    sleep 3
done

echo ""
echo "Dockerシステムが正常に立ち上がりました！"
echo "2. WordPressのテスト環境を再起動しています..."

# 3. Boot the actual WordPress environment
cd ../stretchplus_local_wp
docker compose up -d

echo "==============================================="
echo "復旧が完了しました！！"
echo "これで『 http://localhost:8000/ 』が元通り開けるようになります！"
echo "この黒い画面は閉じてしまって大丈夫です。"
echo "==============================================="
sleep 5
