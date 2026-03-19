import os
import time
import re

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Locate the exact line where PHASE 8 STEP 2 starts
hook = "/* PHASE 8 STEP 2: PREMIUM BANNERS & CAROUSEL UI */"
if hook in css and "@media (max-width: 768px) {\n    /* PHASE 8 STEP 2" not in css and "@media (max-width: 768px) {\n\n    /* PHASE 8 STEP 2" not in css:
    parts = css.split(hook, 1) # Split only on the first occurrence
    # Re-wrap the entire block inside a mobile media query constraint
    new_css = parts[0] + "\n@media (max-width: 768px) {\n\n    " + hook + parts[1] + "\n}\n"
    
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(new_css)
        
    print("Wrapped PHASE 8 STEP 2 in media query safely.")
else:
    print("Already wrapped or hook not found.")


# Let's also do a definitive forced Cache Bust so the PC refreshes immediately
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
            
print("Desktop CSS Patched and Cached Busted.")
