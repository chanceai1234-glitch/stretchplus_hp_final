import re

def process_css(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        css = f.read()

    # Change light blue (rgba(95, 180, 212, 0.8)) to Navy (rgba(26, 54, 93, 0.85))
    old_bg = "background-image: linear-gradient(rgba(95, 180, 212, 0.8), rgba(95, 180, 212, 0.85)), url('./images/cta_bg.png');"
    new_bg = "background-image: linear-gradient(rgba(26, 54, 93, 0.85), rgba(26, 54, 93, 0.9)), url('./images/cta_bg.png');"
    
    css = css.replace(old_bg, new_bg)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated CSS to Navy in", filename)

def process_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

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

    # We need to insert the CTA after FAQ section and before footer.
    # The FAQ section ends with `    </section>` around line 770. Then Section 15 is somewhere?
    # Actually, we already have a bottom-cta-banner right above <footer> from our previous script.
    # Wait, the user said "insert between FAQ and Footer". We *already* put one right above the footer inside `apply_cta_trainers.py`, which is after all sections including FAQ.
    # Let's check if there's already one between FAQ and the footer.
    # Ah, let's just make sure there's one right after `</section>` of FAQ.
    # Actually, the user says "よくあるご質問とフッターの間にも「まずは一回」のCTAバナーを差し込んでください。"
    # Did they miss that it's already at the very bottom, or do they want another one?
    # Our previous script put it at:
    # `    <!-- Pre-Footer CTA -->`
    # `    <div class="bottom-cta-banner">`
    # `    ...`
    # `    <footer>`
    # This IS between FAQ and Footer (if FAQ is the last section).
    # Let me check what the last sections are.
    pass

process_css('style.css')
process_css('redesign/style.css')
