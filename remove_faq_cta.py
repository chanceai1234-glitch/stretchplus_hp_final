import re
import os

files = [
    'stretchplus-theme/template-parts/section-faq.php',
    'redesign/index.html',
    'index.html'
]

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regex to remove the faq-btn-wrap div and its contents completely
        content = re.sub(r'\s*<div class="faq-btn-wrap">.*?</div>\s*', '\n', content, flags=re.DOTALL)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
