import re

cta_html = """
    <!-- Pre-Footer CTA -->
    <div class="bottom-cta-banner">
        <div class="container">
            <h3>まずは1回、体感してみてください。</h3>
            <p style="color: #fff; font-size: 1.1rem; margin-bottom: 25px; font-weight: bold; text-shadow: 1px 1px 3px rgba(0,0,0,0.2);">初回限定価格 60分 3,980円（税込）</p>
            <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
                <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn-web-outline" target="_blank"><i class="far fa-file-alt"></i> WEBで予約する</a>
                <a href="https://lin.ee/rboKm7N" class="btn-web-outline" target="_blank"><i class="fab fa-line"></i> LINEで相談する</a>
            </div>
        </div>
    </div>
"""

def insert_cta(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # ensure we haven't already inserted it
    if "<!-- Pre-Footer CTA -->" in html:
        # Replace the existing one just in case
        pattern = r'<!-- Pre-Footer CTA -->.*?</div>\s*</div>\s*</div>\s*'
        html = re.sub(pattern, cta_html + '\n', html, flags=re.DOTALL)
    else:
        # Insert before footer
        html = html.replace('    <footer id="footer">', cta_html + '\n    <footer id="footer">')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Injected Navy CTA before footer in", filename)

insert_cta('index.html')
insert_cta('redesign/index.html')
