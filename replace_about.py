import re

new_about_redesign = """<section id="about" class="section-bg-light reveal">
        <div class="about-inner">
            <!-- Card 1: What is Personal Stretch? -->
            <div class="about-row card">
                <div class="about-content">
                    <h3><strong>パーソナルストレッチとは？</strong></h3>
                    <p>パーソナルストレッチは、専門知識を持つスタッフがお客様の体の状態に合わせて行う<strong><span class="highlight-blue">マンツーマンのストレッチ</span></strong>です。<br>
                    自分でやるストレッチは、届く範囲を"自分の力だけ"で伸ばすため、つい体に力が入ってしまい、思ったほど伸ばせていないことが少なくありません。<br>
                    パーソナルストレッチなら、プロに身をあずけて"他人の手で"ゆっくり伸ばしていくので、力を抜いたまま、<strong><span class="highlight-blue">自分では届かない深い筋肉まで安全に伸ばしていくことができます。</span></strong></p>
                </div>
                <div class="about-image">
                    <img src="../image_final/about_main.jpg" alt="パーソナルストレッチとは">
                </div>
            </div>

            <!-- Card 2: Difference from Massage -->
            <div class="about-row card">
                <div class="about-content">
                    <h3><strong>マッサージやもみほぐしとの違いは？</strong></h3>
                    <p>マッサージやもみほぐしは、固くなったところを"押したり揉んだりして"その場のコリや疲れを楽にするケアです。<br>
                    パーソナルストレッチは、関節を"動かしながら筋肉を伸ばす"ことで、柔軟性アップや姿勢改善など、<strong><span class="highlight-blue">コリや疲れが起きにくい体づくりを支援するケア</span></strong>です。<br>
                    <strong><span class="highlight-blue">「ほぐしてもすぐ戻ってしまう」</span></strong>と感じている方ほど、ストレッチで体の動き方そのものを変えていくアプローチが合うかもしれません。</p>
                </div>
                <div class="about-image">
                    <img src="../image_final/about_sub_2.jpg" alt="マッサージやもみほぐしとの違い">
                </div>
            </div>

        </div>
    </section>"""

new_about_index = new_about_redesign.replace('class="section-bg-light reveal"', 'class="section-bg-light"').replace('../image_final/', './image_final/')

for filename, new_content in [('redesign/index.html', new_about_redesign), ('index.html', new_about_index)]:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    start_match = re.search(r'<section id="about"', html)
    if not start_match: continue
    start_idx = start_match.start()
    end_idx = html.find('</section>', start_idx) + len('</section>')
    
    html = html[:start_idx] + new_content + html[end_idx:]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Replacement complete.")
