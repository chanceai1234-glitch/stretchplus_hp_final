import os
import time
import re

# 1. Fix the Header Break in Worries Section
def fix_worries_header(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(r'<h2>こんなお悩み.*?ありませんか？</h2>', r'<h2>こんなお悩み<br class="sp-only">ありませんか？</h2>', html)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_worries_header('stretchplus-theme/template-parts/section-worries.php')
fix_worries_header('index.html')
fix_worries_header('redesign/index.html')

# 2. Re-run Cache Bust globally for Safari Users
filepaths = ['stretchplus-theme/header.php', 'index.html', 'redesign/index.html']
buster = f"?v={int(time.time()*1000)}\""

for filepath in filepaths:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        if 'style.css"' in html:
            html = html.replace('style.css"', f'style.css{buster}')
        elif 'style.css?v=' in html:
            html = re.sub(r'style\.css\?v=[0-9]+"', f'style.css{buster}', html)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print("Worries header patched and Cache busted globally.")
