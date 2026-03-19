import os
import re
import time

# 1. CSS Modifications
css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

css_fixes = """
    /* PHASE 9: UX GUIDELINE ALIGNMENTS */
    body {
        font-size: 16px !important;
        line-height: 1.6 !important;
    }
    
    /* Shrink the massive vertical spacing on Mobile */
    section {
        padding: 40px 0 !important;
    }
    .section-bg-light {
        padding: 40px 5% !important;
    }

    /* Style for the CTA Button inside the Nav Menu */
    .sp-nav-cta {
        margin-bottom: 30px !important;
    }
    .sp-nav-cta .btn {
        display: inline-block;
        width: 80%;
        margin: 0 auto;
        padding: 15px;
        background-color: var(--primary-color);
        color: white !important;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(95, 180, 212, 0.3);
    }
"""

if 'PHASE 9: UX GUIDELINE ALIGNMENTS' not in css:
    hook = '/* HERO FIXES */'
    css = css.replace(hook, css_fixes + '\n    ' + hook)
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. HTML Modifications
def process_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Inject Hamburger Reservation CTA
    target_ul = '<nav class="sp-nav-menu">\n            <ul>'
    new_ul = """<nav class="sp-nav-menu">
            <ul>
                <li class="sp-nav-cta"><a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web" target="_blank">まずはWEBで予約する <i class="fas fa-chevron-right"></i></a></li>"""
    
    if 'class="sp-nav-cta"' not in content:
        content = content.replace(target_ul, new_ul)

    # 3. Aggressive Cache Buster
    buster = f"?v={int(time.time()*1000)}\""
    
    if 'style.css"' in content:
        content = content.replace('style.css"', f'style.css{buster}')
    elif 'style.css?v=' in content:
        content = re.sub(r'style\.css\?v=[0-9]+"', f'style.css{buster}', content)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

process_file('stretchplus-theme/header.php')
process_file('index.html')
process_file('redesign/index.html')

print("Phase 9 UX Complete.")
