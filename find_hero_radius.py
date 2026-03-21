import re

with open('stretchplus-theme/style.css', 'r') as f:
    css = f.read()

# find blocks containing .hero and border-radius
blocks = re.findall(r'(\.hero[^{]*\{[^}]*border-radius[^}]*\})', css)
for b in blocks:
    if '50%' in b or 'border-radius' in b:
        print(b)
