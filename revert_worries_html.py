import re

files_to_update = [
    '/Users/ai_stretch/Desktop/stretchplus HPremake final/index.html',
    '/Users/ai_stretch/Desktop/stretchplus HPremake final/redesign/index.html'
]

original_html = """            <div class="personas-wrapper">
                <!-- サラリーマン -->
                <div class="persona-card">
                    <div class="speech-bubble">
                        <ul>
                            <li>PCで目疲れがつらい</li>
                            <li>肩や首の動きが気になる</li>
                            <li>腰の張りや重さを感じる</li>
                        </ul>
                    </div>
                    <div class="persona-image">
                        <img src="./images/persona_salaryman.png" alt="サラリーマンのお悩み" onerror="this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'100\\' height=\\'100\\'><circle cx=\\'50\\' cy=\\'50\\' r=\\'40\\' fill=\\'%23eee\\'/><text x=\\'50\\' y=\\'55\\' font-size=\\'14\\' text-anchor=\\'middle\\' fill=\\'%23999\\'>No Image</text></svg>'">
                        <p class="persona-label">デスクワークの方</p>
                    </div>
                </div>

                <!-- 主婦 -->
                <div class="persona-card">
                    <div class="speech-bubble">
                        <ul>
                            <li>いつも体が重だるい</li>
                            <li>手足の冷えを感じやすい</li>
                            <li>脚のむくみが気になる</li>
                        </ul>
                    </div>
                    <div class="persona-image">
                        <img src="./images/persona_housewife.png" alt="主婦のお悩み" onerror="this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'100\\' height=\\'100\\'><circle cx=\\'50\\' cy=\\'50\\' r=\\'40\\' fill=\\'%23eee\\'/><text x=\\'50\\' y=\\'55\\' font-size=\\'14\\' text-anchor=\\'middle\\' fill=\\'%23999\\'>No Image</text></svg>'">
                        <p class="persona-label">家事・育児の方</p>
                    </div>
                </div>

                <!-- ゴルフ -->
                <div class="persona-card">
                    <div class="speech-bubble">
                        <ul>
                            <li>最近運動後の疲れが抜けにくい</li>
                            <li>動きが重い</li>
                            <li>可動域が狭くなった気がする</li>
                        </ul>
                    </div>
                    <div class="persona-image">
                        <img src="./images/persona_golfer.png" alt="ゴルファーのお悩み" onerror="this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'100\\' height=\\'100\\'><circle cx=\\'50\\' cy=\\'50\\' r=\\'40\\' fill=\\'%23eee\\'/><text x=\\'50\\' y=\\'55\\' font-size=\\'14\\' text-anchor=\\'middle\\' fill=\\'%23999\\'>No Image</text></svg>'">
                        <p class="persona-label">スポーツをされる方</p>
                    </div>
                </div>
            </div>"""

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the single image block we added earlier
    content = re.sub(
        r'<div class="worries-image-container"[^>]*>[\s\S]*?</div>',
        original_html,
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path}")
