import os
import re

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update CSS for Hero, About, Worries
new_css = """
/* ==========================================================================
   SMARTPHONE HERO, ABOUT & WORRIES OVERRIDES
   ========================================================================== */
@media (max-width: 768px) {
    /* HERO FIXES */
    .hero-split {
        padding-top: 80px; /* adjust top padding for mobile */
    }
    .hero-image-col {
        height: auto !important;
        aspect-ratio: 1/1;
        max-height: 90vw;
        margin-bottom: 0px !important;
    }
    .hero-image-wrapper {
        height: 100%;
    }
    .hero-image-bg-circle, .hero-masked-image {
        width: 90vw !important;
        height: 90vw !important;
        max-width: 400px;
        max-height: 400px;
    }
    .hero-content {
        margin-top: -10px; /* Pull text immediately under image */
        padding-bottom: 20px;
    }
    
    /* PRICE BANNER OVERRIDE */
    .hero-note {
        font-size: 1rem;
        line-height: 1.3;
        text-align: center;
        background: #fdf5f6;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #fbdcde;
    }
    .sp-price-top {
        display: block;
        margin-bottom: 5px;
        font-weight: bold;
        color: #333;
    }
    .sp-price-top .strike {
        text-decoration: line-through;
        opacity: 0.7;
    }
    .sp-price-bottom {
        display: block;
        font-size: 2.8rem;
        color: #E50121;
        line-height: 1;
        letter-spacing: -2px;
    }
    .sp-price-bottom .arrow {
        font-size: 1.5rem;
        vertical-align: middle;
        color: #E50121;
        margin-right: 5px;
    }
    .sp-price-bottom .yen {
        font-size: 1.2rem;
        letter-spacing: 0;
    }

    /* ABOUT FIXES */
    .about-row.card {
        padding: 0 !important;
        box-shadow: none !important;
        border: none !important;
        background: transparent !important;
        gap: 15px !important;
        margin-bottom: 40px;
    }
    .about-image {
        order: -1 !important; /* Force Image Top */
        width: 100% !important;
        max-width: 100% !important;
    }
    .about-image img {
        border-radius: 8px;
        width: 100%;
        height: auto;
    }
    .about-content {
        padding: 0 10px;
    }
}
"""

if 'SMARTPHONE HERO, ABOUT & WORRIES OVERRIDES' not in css:
    css += '\n' + new_css
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Update HTML elements
def process_html_file(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Hero Price Banner HTML Replacement
    hero_old = '<p class="hero-note">初回限定価格 60分：10,680円 → <strong>3,980円</strong></p>'
    hero_new = """<div class="hero-note">
                        <span class="sp-price-top">初回限定価格 60分：<span class="strike">10,680円</span></span><br class="sp-only">
                        <strong class="sp-price-bottom"><span class="arrow">▶︎</span>3,980<span class="yen">円</span></strong>
                    </div>"""
    content = content.replace(hero_old, hero_new)
    
    # Hero Price Banner HTML Replacement (if space variation exists)
    hero_old_2 = '<p class="hero-note">初回限定価格 60分：10,680円 → <strong>3,980円</strong></p>'
    if hero_old_2 in content:
        pass # Already handled

    # Worries Text Replacement
    # Current: <p class="catchy-message">そのお悩み、<br class="sp-only"><span class="highlight-blue">ストレッチplusが全部解決</span>します！</p>
    worries_old = '<p class="catchy-message">そのお悩み、<br class="sp-only"><span class="highlight-blue">ストレッチplusが全部解決</span>します！</p>'
    worries_new = '<p class="catchy-message">そのお悩み<br>ストレッチplusが<br><span class="highlight-blue">全部解決します！</span></p>'
    content = content.replace(worries_old, worries_new)
    
    # Catch any variations of worries
    content = re.sub(
        r'<p class="catchy-message">そのお悩み.*?全部解決します！？</p>', 
        worries_new, 
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

process_html_file('stretchplus-theme/template-parts/section-hero.php')
process_html_file('stretchplus-theme/template-parts/section-worries.php')
process_html_file('index.html')
process_html_file('redesign/index.html')

print("Applied Hero, About, and Worries refactors")
