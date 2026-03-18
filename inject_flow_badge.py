import os

def insert_badge(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    target1 = '<h2 class="section-title">\n                ご利用の流れ\n            </h2>'
    target2 = '<h2 class="section-title">\n                    ご利用の流れ\n                </h2>'
    target3 = '<h2>ご利用の流れ</h2>'
    
    replacement = '<div class="speech-badge">初めてでも安心！</div>\n            <h2 class="section-title">\n                ご利用の流れ\n            </h2>'

    if target1 in html and '初めてでも安心！' not in html:
        html = html.replace(target1, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {filepath}")
    elif target3 in html and '初めてでも安心！' not in html:
        html = html.replace(target3, '<div class="speech-badge">初めてでも安心！</div>\n            <h2>ご利用の流れ</h2>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {filepath}")

insert_badge('stretchplus-theme/template-parts/section-flow.php')
insert_badge('redesign/index.html')
insert_badge('index.html')
