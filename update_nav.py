import re

old_nav = """            <ul>
                <li><a href="#about">パーソナルストレッチとは</a></li>
                <li><a href="#menu">メニュー/料金</a></li>
                <li><a href="#trainers">トレーナー</a></li>
                <li><a href="#faq">FAQ</a></li>
                <li><a href="#info">店舗情報</a></li>
                <li><a href="#access">アクセス</a></li>
                <li><a href="lp4_corporate.html">法人向け</a></li>
            </ul>"""

new_nav = """            <ul>
                <li><a href="#about">パーソナルストレッチとは</a></li>
                <li><a href="#worries">よくあるお悩み</a></li>
                <li><a href="#reviews">お客様の声</a></li>
                <li><a href="#flow">ご利用の流れ</a></li>
                <li><a href="#menu">メニュー/料金</a></li>
                <li><a href="#info">店舗情報</a></li>
                <li><a href="#access">アクセス</a></li>
            </ul>"""

def update_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # If the old nav is found exactly
    if old_nav in html:
        html = html.replace(old_nav, new_nav)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated exact header nav in", filename)
    else:
        # Fallback regex replacing everything inside <nav class="header-nav">
        pattern = r'<nav class="header-nav">\s*<ul>.*?</ul>\s*</nav>'
        replacement = f'<nav class="header-nav">\n{new_nav}\n        </nav>'
        new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)
        if new_html != html:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print("Updated header nav via regex in", filename)
        else:
            print("Could not find <nav> block in", filename)

update_html('index.html')
update_html('redesign/index.html')
