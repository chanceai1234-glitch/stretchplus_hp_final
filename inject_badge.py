import os

def insert_badge(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    target = '<h2>豊富な設備・アメニティ</h2>'
    replacement = '<div class="speech-badge">手ぶらでOK！</div>\n            <h2>豊富な設備・アメニティ</h2>'

    if target in html and '<div class="speech-badge">' not in html:
        html = html.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {filepath}")

insert_badge('stretchplus-theme/template-parts/section-amenities.php')
insert_badge('redesign/index.html')
insert_badge('index.html')
