import sys

replacement = """    <!-- Section 7: 施術の流れ -->
    <section id="flow" class="reveal section-bg-light">
        <div class="container">
            <h2>施術の流れ</h2>
            <p class="flow-lead">ご来店からお帰りまでの流れをご紹介いたします。</p>
            <div class="flow-timeline">
                
                <div class="timeline-item">
                    <div class="timeline-number">01</div>
                    <div class="timeline-content">
                        <h3>まずはコースを選んでご予約</h3>
                        <p>30、60、90分など、ご予定とお悩みに合わせて豊富なコースをご用意しております。お好きなコースをお選びいただき、ご予約ください。</p>
                        <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web pulse-btn" style="margin-top: 5px; display: inline-block; width: auto; padding: 12px 30px;" target="_blank">コースを選んで予約する <i class="fas fa-chevron-right"></i></a>
                    </div>
                </div>

                <div class="timeline-item">
                    <div class="timeline-number">02</div>
                    <div class="timeline-content">
                        <h3>ご予約時間の5分前にお店に到着</h3>
                        <p>お時間いっぱい施術をさせていただけるよう、5分前にはお店にご来店ください。スタッフが笑顔でお出迎えいたします。</p>
                        <div class="timeline-image"><img src="./images/access_step2.jpg" alt="ご来店"></div>
                    </div>
                </div>

                <div class="timeline-item">
                    <div class="timeline-number">03</div>
                    <div class="timeline-content">
                        <h3>施術ベッドへご案内</h3>
                        <p>完全個室のリラックスできる専用施術ベッドへご案内いたします。お着替えをご希望の方は、無料の施術着を完備しておりますので手ぶらでも安心です。</p>
                        <div class="timeline-image"><img src="./images/hero_private_room.png" alt="完全個室へご案内"></div>
                    </div>
                </div>

                <div class="timeline-item">
                    <div class="timeline-number">04</div>
                    <div class="timeline-content">
                        <h3>カウンセリング</h3>
                        <p>現在のお悩みや重点的に改善したい部位、日常生活でのクセなどを担当トレーナーにお伝えください。お客様の身体の状態や目的に合わせて、その日最適なストレッチメニューを組み立てます。</p>
                        <div class="timeline-image"><img src="./images/母艦HP/施術の流れ_1.jpg" alt="カウンセリング"></div>
                    </div>
                </div>

                <div class="timeline-item">
                    <div class="timeline-number">05</div>
                    <div class="timeline-content">
                        <h3>いざ、パーソナルストレッチ開始</h3>
                        <p>お客様一人ひとりの身体の状態に合わせて、プロのトレーナーがマンツーマンでストレッチを行います。普段自分では伸ばしきれない深層筋までしっかりとアプローチします。ベッドに寝ているだけで大丈夫です。</p>
                        <div class="timeline-image"><img src="./images/母艦HP/flow_step3_new.jpg" alt="パーソナルストレッチ"></div>
                    </div>
                </div>

                <div class="timeline-item">
                    <div class="timeline-number">06</div>
                    <div class="timeline-content">
                        <h3>施術の振り返り</h3>
                        <p>施術後の身体の変化を確認し、施術前との違いを一緒に見ていきます。必要に応じて、効果を維持するためにご自宅でも取り入れやすい簡単なセルフケア方法などもアドバイスします。</p>
                        <div class="timeline-image"><img src="./images/母艦HP/flow_step2_new.jpg" alt="施術の振り返り"></div>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

with open('redesign/index.html', 'r') as f:
    html = f.read()

start_idx = html.find('    <!-- Section 7: 施術の流れ -->')
end_idx = html.find('    <!-- Section 8:')

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + replacement + '\n\n' + html[end_idx:]
    with open('redesign/index.html', 'w') as f:
        f.write(new_html)
    print("Updated redesign/index.html")
else:
    print("Tags not found")

