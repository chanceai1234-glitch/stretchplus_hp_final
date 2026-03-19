import os
import time

filepaths = [
    'stretchplus-theme/header.php',
    'index.html',
    'redesign/index.html'
]

# Generate a unique cache buster string
buster = f"?v={int(time.time())}\""

for filepath in filepaths:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Replace existing style.css imports
        if 'style.css"' in html:
            html = html.replace('style.css"', f'style.css{buster}')
        elif 'style.css?v=' in html:
            import re
            html = re.sub(r'style\.css\?v=\d+"', f'style.css{buster}', html)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print("Cache bust applied.")
