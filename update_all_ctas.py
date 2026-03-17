import re

cta_html = """    <div class="bottom-cta-banner">
        <div class="container">
            <h3>まずは1回、体感してみてください。</h3>
            <p style="color: #fff; font-size: 1.1rem; margin-bottom: 25px; font-weight: bold; text-shadow: 1px 1px 3px rgba(0,0,0,0.2);">初回限定価格 60分 3,980円（税込）</p>
            <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
                <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn-web-outline" target="_blank"><i class="far fa-file-alt"></i> WEBで予約する</a>
                <a href="https://lin.ee/rboKm7N" class="btn-web-outline" target="_blank"><i class="fab fa-line"></i> LINEで相談する</a>
            </div>
        </div>
    </div>"""

def process_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace <section id="cta-1"> ... </section>
    pattern_cta1 = r'<section id="cta-1">.*?</section>'
    html = re.sub(pattern_cta1, cta_html, html, flags=re.DOTALL)

    # Replace <section id="cta-2"> ... </section> (might be Section 8)
    # the old id was cta-something, let's just make sure.
    # We can also replace the existing bottom CTA banner to be the new one with the text "初回限定価格 60分 3,980円（税込）"
    
    pattern_old_bottom_cta = r'<div class="bottom-cta-banner">.*?</div>\n    \n    <footer>'
    new_bottom_cta = cta_html + '\n    \n    <footer>'
    html = re.sub(pattern_old_bottom_cta, new_bottom_cta, html, flags=re.DOTALL)

    # Note section 8 might just be <section id="cta-2"> if it exists.
    pattern_cta2 = r'<section id="cta-2">.*?</section>'
    html = re.sub(pattern_cta2, cta_html, html, flags=re.DOTALL)
    
    # Just to be sure, maybe the old cta is named something else, let's check
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated CTAs in", filename)

process_html('index.html')
process_html('redesign/index.html')
