import os

files = [
    'stretchplus-theme/template-parts/section-flow.php',
    'redesign/index.html',
    'index.html'
]

old_span = '<span style="font-size: 0.85em; color: #666;">※大幅に遅れた場合、施術時間の短縮やご予約の変更をお願いすることがございます。</span>'
new_span = '<span style="color: #666;">※大幅に遅れた場合、施術時間の短縮やご予約の変更をお願いすることがございます。</span>'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if old_span in content:
        content = content.replace(old_span, new_span)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
