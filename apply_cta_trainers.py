import sys
import re

trainer_miyazaka = """
            <div class="trainer-card">
                <img src="./images/miyasaka.jpg" alt="宮坂" class="trainer-icon">
                <h3>宮坂</h3>
                <div class="trainer-info-list">
                    <div class="trainer-info-item"><span class="ti-label">業界歴</span><span class="ti-value">8年</span></div>
                    <div class="trainer-info-item"><span class="ti-label">得意施術</span><span class="ti-value">ヘッドスパの経験を活かしたヒアリングと効かせる施術</span></div>
                    <div class="trainer-info-item"><span class="ti-label">趣味</span><span class="ti-value">ラグビー観戦、自然めぐり</span></div>
                    <div class="trainer-info-item"><span class="ti-label">メッセージ</span><span class="ti-value">忙しい毎日のリセットになるような時間を提供します。</span></div>
                </div>
                <a href="https://beauty.hotpepper.jp/CSP/kr/reserve/?storeId=H000671756&staffId=W001069255"
                    class="btn btn-booking-outline" target="_blank">指名して予約</a>
            </div>
"""

trainer_yamamoto = """
            <div class="trainer-card">
                <img src="./images/yamamoto.jpg" alt="山本" class="trainer-icon">
                <h3>山本</h3>
                <div class="trainer-info-list">
                    <div class="trainer-info-item"><span class="ti-label">業界歴</span><span class="ti-value">8年</span></div>
                    <div class="trainer-info-item"><span class="ti-label">得意施術</span><span class="ti-value">肩・腰・足、女性特有のお悩みに合ったケア</span></div>
                    <div class="trainer-info-item"><span class="ti-label">趣味</span><span class="ti-value">バスケ観戦、パン屋めぐり</span></div>
                    <div class="trainer-info-item"><span class="ti-label">メッセージ</span><span class="ti-value">年代を問わず、一人ひとりに寄り添ってサポートします！</span></div>
                </div>
                <a href="https://beauty.hotpepper.jp/CSP/kr/reserve/?storeId=H000671756&staffId=W001092716"
                    class="btn btn-booking-outline" target="_blank">指名して予約</a>
            </div>
"""

trainer_sakuma = """
            <div class="trainer-card">
                <img src="./images/sakuma.jpg" alt="佐久間" class="trainer-icon">
                <h3>佐久間</h3>
                <div class="trainer-info-list">
                    <div class="trainer-info-item"><span class="ti-label">業界歴</span><span class="ti-value">5年</span></div>
                    <div class="trainer-info-item"><span class="ti-label">得意施術</span><span class="ti-value">姿勢改善、関節のお悩み、パフォーマンス向上</span></div>
                    <div class="trainer-info-item"><span class="ti-label">趣味</span><span class="ti-value">海、野球観戦、子育て</span></div>
                    <div class="trainer-info-item"><span class="ti-label">メッセージ</span><span class="ti-value">理学療法士の学びを活かし、幅広くサポートします。</span></div>
                </div>
                <a href="https://beauty.hotpepper.jp/kr/slnH000671756/staff/W001069296/" class="btn btn-booking-outline"
                    target="_blank">指名して予約</a>
            </div>
"""

trainer_suzuki = """
            <div class="trainer-card">
                <img src="./images/suzuki.jpg" alt="鈴木" class="trainer-icon">
                <h3>鈴木</h3>
                <div class="trainer-info-list">
                    <div class="trainer-info-item"><span class="ti-label">業界歴</span><span class="ti-value">1年</span></div>
                    <div class="trainer-info-item"><span class="ti-label">得意施術</span><span class="ti-value">肩甲骨・胸郭の可動域改善、パフォーマンス向上</span></div>
                    <div class="trainer-info-item"><span class="ti-label">趣味</span><span class="ti-value">スポーツ</span></div>
                    <div class="trainer-info-item"><span class="ti-label">メッセージ</span><span class="ti-value">競技にも日常にもつながる身体づくりを大切にしています！</span></div>
                </div>
                <a href="https://beauty.hotpepper.jp/kr/slnH000671756/staff/W001348826/" class="btn btn-booking-outline"
                    target="_blank">指名して予約</a>
            </div>
"""

css_additions = """
/* ==========================================================================
   Trainer detailed info list
   ========================================================================== */
.trainer-info-list {
    text-align: left;
    margin-bottom: 20px;
    font-size: 0.9rem;
}
.trainer-info-item {
    display: flex;
    margin-bottom: 8px;
    border-bottom: 1px dashed #eee;
    padding-bottom: 5px;
}
.trainer-info-item:last-child {
    border-bottom: none;
}
.ti-label {
    flex: 0 0 70px;
    font-weight: bold;
    color: var(--primary-color);
}
.ti-value {
    flex: 1;
    color: #4a4a4a;
    line-height: 1.5;
}

/* ==========================================================================
   Bottom Stick CTA / Google Map Btn
   ========================================================================== */
.btn-google-map {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: #4285F4;
    color: #fff;
    padding: 12px 24px;
    border-radius: 4px;
    text-decoration: none;
    font-weight: bold;
    margin-top: 15px;
    transition: background 0.3s;
}
.btn-google-map:hover {
    background-color: #3367d6;
    color: #fff;
}
.btn-google-map i {
    margin-right: 8px;
}

.bottom-cta-banner {
    background-color: var(--primary-color);
    padding: 20px;
    text-align: center;
    color: #fff;
}
.bottom-cta-banner h3 {
    margin-bottom: 15px;
    font-size: 1.2rem;
}
.bottom-cta-banner .btn {
    background-color: #fff;
    color: var(--primary-color);
}
.bottom-cta-banner .btn:hover {
    background-color: #f0f0f0;
}
"""

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add CTA after Section 9 ("ストレッチplusが大切にしていること" closing tag or container)
    # The section is `<section id="policy">`
    about_cta = """
        <div style="text-align: center; margin-top: 40px;">
            <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web pulse-btn" target="_blank" style="display:inline-block; padding: 15px 40px; font-size: 1.1rem; width: auto;">ストレッチplusの想いに共感いただけた方はコチラ <i class="fas fa-arrow-right"></i></a>
        </div>
    </section>"""
    html = html.replace('    </section>\n\n    <!-- Section 10: トレーナー紹介 -->', about_cta + '\n\n    <!-- Section 10: トレーナー紹介 -->')

    # 2. Replace trainers
    start_trainers = html.find('<div class="trainer-grid">')
    end_trainers = html.find('</section>', start_trainers)
    if start_trainers != -1 and end_trainers != -1:
        new_trainers = '<div class="trainer-grid">\n' + trainer_miyazaka + trainer_yamamoto + trainer_sakuma + trainer_suzuki + '        </div>\n    '
        html = html[:start_trainers] + new_trainers + html[end_trainers:]

    # 3. Add Google Map button to Access section
    # search for `<button class="btn-copy"` and append map button after it.
    map_btn = """
                    <button class="btn-copy" onclick="copyAddress()"><i class="fas fa-copy"></i> 住所をコピー</button>
                    <a href="https://maps.google.com/?q=東京都中央区日本橋兜町9-15" class="btn-google-map" target="_blank"><i class="fas fa-map-marker-alt"></i> Google Map</a>"""
    html = html.replace('<button class="btn-copy" onclick="copyAddress()"><i class="fas fa-copy"></i> 住所をコピー</button>', map_btn)

    # 4. Add floating/sticky CTA banner above footer
    footer_idx = html.find('<footer>')
    if footer_idx != -1:
        bottom_banner = """
    <!-- Pre-Footer CTA -->
    <div class="bottom-cta-banner">
        <div class="container">
            <h3>まずは1回、体感してみてください。</h3>
            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web pulse-btn" target="_blank" style="padding: 12px 30px;">WEBで予約する <i class="fas fa-arrow-right"></i></a>
                <a href="https://lin.ee/rboKm7N" class="btn btn-line" target="_blank" style="background:#06C755; color:#fff; padding: 12px 30px;"><i class="fab fa-line"></i> LINEで相談する</a>
            </div>
        </div>
    </div>
    
    <footer>"""
        html = html.replace('<footer>', bottom_banner)


    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated", filename)

def update_css(filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(css_additions)
    print("Updated CSS", filename)


update_file('index.html')
update_file('redesign/index.html')
update_css('style.css')
update_css('redesign/style.css')
