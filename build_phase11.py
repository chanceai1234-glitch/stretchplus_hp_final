import os
import re
import time

# 1. CSS Modifications
css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

css_fixes = """
/* ==========================================================================
   PHASE 11: ULTIMATE ITERATION POLISH
   ========================================================================== */
@media (max-width: 768px) {
    /* 1. Hero Overlay */
    .main-message { display: none !important; }
    .hero-image-wrapper { position: relative !important; }
    .hero-image-wrapper .sub-message {
        position: absolute !important;
        bottom: -20px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        width: 90% !important;
        background: rgba(255, 255, 255, 0.95) !important;
        padding: 15px 10px !important;
        border-radius: 8px !important;
        font-weight: 800 !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15) !important;
        text-align: center !important;
        z-index: 10 !important;
        font-size: 3.5vw !important; /* Ensure it never breaks */
    }

    /* 2. Swiper Physics Alignment Fix */
    .sp-carousel-wrapper {
        justify-content: flex-start !important;
    }
    .sp-carousel-wrapper > * {
        scroll-snap-align: start !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
    }
    
    /* 3. Review Card Title */
    .sp-review-card-title {
        display: block !important;
        color: var(--primary-color) !important;
        font-size: 1.15rem !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        text-align: center !important;
        border-bottom: 2px solid var(--border-color) !important;
        padding-bottom: 10px !important;
    }

    /* 4. Store Info Left Alignment */
    .shop-table th, .shop-table td {
        padding-left: 15px !important;
        padding-right: 15px !important;
        text-align: left !important;
    }
    
    /* 5. FAQ Cleanup */
    .faq-lead {
        display: none !important;
    }
    
    /* Additional formatting for About extraction */
    .about-row.card {
        display: flex !important;
        flex-direction: column !important;
        padding-top: 20px !important;
    }
    .about-row.card h3 {
        margin-bottom: 15px !important;
        padding-left: 5% !important;
        padding-right: 5% !important;
    }
}
"""

if 'PHASE 11: ULTIMATE ITERATION POLISH' not in css:
    css += '\n' + css_fixes
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. HTML Restructuring Functions
def restructure_about(html):
    cards = html.split('<div class="about-row card">')
    new_html = cards[0]
    for card in cards[1:]:
        h3_match = re.search(r'(<h3>.*?</h3>)', card, re.DOTALL)
        if not h3_match:
            new_html += '<div class="about-row card">' + card
            continue
        h3 = h3_match.group(1)
        card_no_h3 = card.replace(h3, '')
        
        img_match = re.search(r'(<div class="about-image">.*?</div>)', card_no_h3, re.DOTALL)
        if img_match:
            img_div = img_match.group(1)
            card_no_img = card_no_h3.replace(img_div, '')
            
            content_match = re.search(r'<div class="about-content">(.*?)</div>', card_no_img, re.DOTALL)
            content_inner = content_match.group(1).strip() if content_match else ""
            rest = card_no_img.replace(content_match.group(0), '') if content_match else card_no_img
            
            new_card = f'\n                {h3}\n                {img_div}\n                <div class="about-content">\n                    {content_inner}\n                </div>{rest}'
            new_html += '<div class="about-row card">' + new_card
        else:
            new_html += '<div class="about-row card">' + card
    return new_html

def restructure_hero(html):
    sub_match = re.search(r'(<p class="sub-message">.*?</p>)', html, re.DOTALL)
    if not sub_match: return html
    sub = sub_match.group(1)
    
    if 'class="hero-image-wrapper"' in html and sub in html.split('class="hero-image-wrapper"')[1]:
        return html
        
    html = html.replace(sub, '')
    html = html.replace('<div class="hero-image-wrapper">', '<div class="hero-image-wrapper">\n                    ' + sub)
    return html

# 3. Apply Transformations
def process_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Apply About Restructure
    if 'id="about"' in content:
        content = restructure_about(content)
        
    # Apply Hero Restructure
    if 'id="hero"' in content or 'hero-split' in content:
        content = restructure_hero(content)

    # Apply Worries Title Fix
    content = content.replace('<h2>こんなお悩み<br class="sp-only">ありませんか？</h2>', '<h2>こんなお悩みで<br class="sp-only">ありませんか？</h2>')
    content = content.replace('<h2>こんなお悩み<br>ありませんか？</h2>', '<h2>こんなお悩みで<br>ありませんか？</h2>')
    content = content.replace('<h2 class="worries-title">こんなお悩み、ありませんか？</h2>', '<h2 class="worries-title">こんなお悩みで<br class="sp-only">ありませんか？</h2>')

    # Inject Review Title
    title_hook = '<h4 class="sp-review-card-title sp-only">お客様の声</h4>'
    if title_hook not in content and 'class="review-card"' in content:
        content = content.replace('<div class="review-card">', f'<div class="review-card">\n                        {title_hook}')

    # Aggressive Cache Buster
    buster = f"?v={int(time.time()*1000)}\""
    
    if 'style.css"' in content:
        content = content.replace('style.css"', f'style.css{buster}')
    elif 'style.css?v=' in content:
        content = re.sub(r'style\.css\?v=[0-9]+"', f'style.css{buster}', content)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

# File Targets
files_to_process = [
    'stretchplus-theme/template-parts/section-about.php',
    'stretchplus-theme/template-parts/section-hero.php',
    'stretchplus-theme/template-parts/section-worries.php',
    'stretchplus-theme/template-parts/section-reviews.php',
    'stretchplus-theme/template-parts/section-info.php',
    'stretchplus-theme/template-parts/section-faq.php',
    'stretchplus-theme/header.php',
    'index.html',
    'redesign/index.html'
]

for f in files_to_process:
    process_file(f)

print("Phase 11 Operations Complete.")
