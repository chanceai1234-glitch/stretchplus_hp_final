import sys

html_replacement = """    <!-- Section 7: 施術の流れ -->
    <section id="flow" class="flow-horizontal-section">
        <div class="container" style="max-width: 900px; text-align: center; margin-bottom: 30px;">
            <h2 class="section-title" style="display: inline-block; position: relative; padding: 0 40px; margin-bottom: 20px;">
                ご利用の流れ
                <span style="position: absolute; top: 50%; left: 0; width: 30px; height: 2px; background: #333;"></span>
                <span style="position: absolute; top: 50%; right: 0; width: 30px; height: 2px; background: #333;"></span>
            </h2>
            <p class="flow-lead" style="font-size: 0.95rem; color: #555; line-height: 1.8;">
                STRETCH+は、本格的なパーソナルストレッチが体験できる専門店として、<br>
                多くの方の健康的なお体づくりをサポートしております。
            </p>
        </div>
        
        <div class="flow-steps-wrapper">
            <!-- STEP 01 -->
            <div class="flow-step bg-beige">
                <div class="flow-step-inner container">
                    <div class="flow-step-image">
                        <img src="./images/access_step2.jpg" alt="まずはメニューを選んで、ご予約を！">
                    </div>
                    <div class="flow-step-content">
                        <div class="flow-step-header">
                            <span class="step-badge-orange">STEP 01</span>
                            <h3 class="step-title-inline">まずはメニューを選んで、ご予約を！</h3>
                        </div>
                        <p class="step-desc">ご予約は、オンライン、LINE、お電話にてお受付しております。<br>複数名でのご来店の場合はお電話または店頭にてご予約をお願いします。<br>お電話でのご予約の際は「お名前・ご希望のコース・ご希望の時間帯・ご連絡先」をお伺いいたします。<br>担当トレーナーの指名もできますので、お気軽にお問い合わせください。</p>
                        <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web pulse-btn" style="margin-top: 15px; display: inline-block; width: auto; padding: 12px 30px; background: #000; color: #fff; border-radius: 30px; text-decoration: none; font-weight: bold;" target="_blank">予約メニューを一覧から探す <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
                <div class="flow-triangle-down-beige"></div>
            </div>

            <!-- STEP 02 -->
            <div class="flow-step bg-white">
                <div class="flow-step-inner container">
                    <div class="flow-step-image">
                        <img src="./images/about_intro.jpg" alt="ご予約時間の5分前を目安にご来店ください。">
                    </div>
                    <div class="flow-step-content">
                        <div class="flow-step-header">
                            <span class="step-badge-orange">STEP 02</span>
                            <h3 class="step-title-inline">ご予約時間の5分前を目安にご来店ください。</h3>
                        </div>
                        <p class="step-desc">余裕を持って予定の5分前を目安に店舗にお越しください。<br>万が一ご来店が遅れそうな場合は、お早めにご予約した店舗までご連絡をお願いします。<br><small style="color:#888;">※ご予約時間に遅れた場合、他の予約状況により施術時間を短縮させていただくか、もしくは施術をお断りする場合がございます。あらかじめご了承ください。</small></p>
                    </div>
                </div>
                <div class="flow-triangle-down-white"></div>
            </div>

            <!-- STEP 03 -->
            <div class="flow-step bg-beige">
                <div class="flow-step-inner container">
                    <div class="flow-step-image">
                        <img src="./images/hero_private_room.png" alt="ご来店！ヒアリングとお会計を済ませます。">
                    </div>
                    <div class="flow-step-content">
                        <div class="flow-step-header">
                            <span class="step-badge-orange">STEP 03</span>
                            <h3 class="step-title-inline">ご来店！ヒアリングとお会計を済ませます。</h3>
                        </div>
                        <p class="step-desc">ご来店後、まずは担当トレーナーがお体の状態やお悩みについてヒアリングいたします。<br>その後、お会計をさせていただきます。無料の施術着へのお着替えが完了しましたら、完全個室の専用ベッドへご案内いたします。</p>
                    </div>
                </div>
                <div class="flow-triangle-down-beige"></div>
            </div>

            <!-- STEP 04 -->
            <div class="flow-step bg-white" style="margin-bottom: 0;">
                <div class="flow-step-inner container">
                    <div class="flow-step-image">
                        <img src="./images/母艦HP/flow_step3_new.jpg" alt="パーソナルストレッチ開始">
                    </div>
                    <div class="flow-step-content">
                        <div class="flow-step-header">
                            <span class="step-badge-orange">STEP 04</span>
                            <h3 class="step-title-inline">パーソナルストレッチ開始</h3>
                        </div>
                        <p class="step-desc">お客様一人ひとりの身体の状態に合わせて、プロのトレーナーがマンツーマンでストレッチを行います。<br>普段自分では伸ばしきれない深層筋までしっかりとアプローチします。ベッドに寝ているだけで大丈夫です。</p>
                    </div>
                </div>
            </div>
            
        </div>
    </section>"""

css_replacement = """/* ==========================================================================
   Flow Section - Horizontal Timeline (Reference Image Design)
   ========================================================================== */
.flow-horizontal-section {
    padding: 60px 0 0;
    width: 100%;
}

.flow-steps-wrapper {
    width: 100%;
    margin-top: 40px;
}

.flow-step {
    position: relative;
    padding: 60px 0;
    width: 100%;
}

.bg-beige {
    background-color: #fcece3; /* light beige/pinkish tint from image */
}

.bg-white {
    background-color: #ffffff;
}

.flow-step-inner {
    display: flex;
    align-items: flex-start;
    max-width: 1000px;
    margin: 0 auto;
    gap: 40px;
}

.flow-step-image {
    width: 40%;
    flex-shrink: 0;
}

.flow-step-image img {
    width: 100%;
    border-radius: 4px; /* subtle rounding */
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    object-fit: cover;
    aspect-ratio: 4/3;
}

.flow-step-content {
    width: 60%;
    text-align: left;
}

.flow-step-header {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    border-bottom: 2px solid #555;
    padding-bottom: 10px;
    gap: 15px;
}

.step-badge-orange {
    background-color: #ff6a3c;
    color: #fff;
    font-weight: bold;
    font-size: 1.1rem;
    padding: 5px 20px;
    border-radius: 30px; /* pill shape */
    white-space: nowrap;
    letter-spacing: 1px;
}

.step-title-inline {
    font-size: 1.3rem;
    color: #333;
    font-weight: bold;
    margin: 0;
    line-height: 1.4;
}

.step-desc {
    font-size: 0.95rem;
    color: #4a4a4a;
    line-height: 1.8;
}

/* Triangles */
.flow-triangle-down-beige {
    position: absolute;
    bottom: -30px;
    left: 50%;
    transform: translateX(-50%);
    width: 0; 
    height: 0; 
    border-left: 40px solid transparent;
    border-right: 40px solid transparent;
    border-top: 30px solid #fcece3;
    z-index: 10;
}

.flow-triangle-down-white {
    position: absolute;
    bottom: -30px;
    left: 50%;
    transform: translateX(-50%);
    width: 0; 
    height: 0; 
    border-left: 40px solid transparent;
    border-right: 40px solid transparent;
    border-top: 30px solid #ffffff;
    z-index: 10;
}

@media (max-width: 768px) {
    .flow-step-inner {
        flex-direction: column;
        gap: 20px;
        padding: 0 20px;
    }
    .flow-step-image {
        width: 100%;
    }
    .flow-step-content {
        width: 100%;
    }
    .flow-step-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
    }
}
"""

def update_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    start_idx = html.find('    <!-- Section 7: 施術の流れ -->')
    end_idx = html.find('    <!-- Section 8:')

    if start_idx != -1 and end_idx != -1:
        new_html = html[:start_idx] + html_replacement + '\n\n' + html[end_idx:]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated HTML in {filename}")
    else:
        print(f"Could not find start/end tags in {filename}")

def update_css(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        css = f.read()
    
    start_idx = css.find('/* ==========================================================================')
    # Find the vertical timeline block
    v_timeline_idx = css.find('   Flow Section - Vertical Timeline', start_idx)
    
    if v_timeline_idx != -1:
        # We need to find the start of this block comment
        block_start = css.rfind('/* ==========================================================================', 0, v_timeline_idx)
        if block_start != -1:
            new_css = css[:block_start] + css_replacement
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_css)
            print(f"Replaced vertical timeline CSS in {filename}")
            return
    
    # If not found, just append
    with open(filename, 'a', encoding='utf-8') as f:
        f.write('\n' + css_replacement)
    print(f"Appended CSS to {filename}")

update_html('/Users/ai_stretch/Desktop/stretchplus HPremake final/index.html')
update_html('/Users/ai_stretch/Desktop/stretchplus HPremake final/redesign/index.html')
update_css('/Users/ai_stretch/Desktop/stretchplus HPremake final/style.css')
update_css('/Users/ai_stretch/Desktop/stretchplus HPremake final/redesign/style.css')
