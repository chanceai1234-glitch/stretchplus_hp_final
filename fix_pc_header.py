import os
import time
import re

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. PC Header Sizing Patch
css_fixes = """
/* ==========================================================================
   DESKTOP HEADER RESPONSIVE SCALING (Phase 10)
   ========================================================================== */
.header-nav a,
.header-actions .btn {
    white-space: nowrap !important; /* Force text to NEVER break */
}

/* 1366px Laptops */
@media (max-width: 1300px) and (min-width: 769px) {
    .header-nav ul { gap: 15px !important; }
    .header-nav a { font-size: 0.85rem !important; }
    .header-actions { gap: 8px !important; }
    .header-actions .btn {
        padding: 8px 12px !important;
        font-size: 0.85rem !important;
    }
    .header-logo img { max-width: 180px !important; }
}

/* 1024px Tablets and Small Desktop */
@media (max-width: 1100px) and (min-width: 769px) {
    .header-nav ul { gap: 8px !important; }
    .header-nav a { font-size: 0.75rem !important; }
    .header-actions .btn {
        padding: 6px 10px !important;
        font-size: 0.75rem !important;
    }
    .header-logo img { max-width: 140px !important; }
}
"""

if 'DESKTOP HEADER RESPONSIVE SCALING' not in css:
    hook = '/* ==========================================================================\n   SMARTPHONE GLOBAL UI OVERRIDES'
    if hook in css:
        css = css.replace(hook, css_fixes + '\n' + hook)
    else:
        css += '\n' + css_fixes
        
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Definitively Cache Bust
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

print("PC Header Scaled and Cache Busted.")
