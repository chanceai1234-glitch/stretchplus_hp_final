import os
import re

css_fixes = """
/* ==========================================================================
   PHASE 11: SAFE MOBILE UX POLISH (DESKTOP PRESERVED)
   ========================================================================== */
@media (max-width: 768px) {
    /* 1. HTML Extraction bypass: About Row Reordering via 'display: contents' */
    .about-row.card {
        display: flex !important;
        flex-direction: column !important;
        padding-top: 30px !important;
    }
    .about-content {
        display: contents !important; /* Extremely useful for flattening DOM nodes */
    }
    .about-content h3 {
        order: -2 !important;
        margin-bottom: 20px !important;
        text-align: center !important;
        padding: 0 15px !important;
    }
    .about-image {
        order: -1 !important;
        margin-bottom: 20px !important;
    }
    .about-content p {
        order: 0 !important;
    }

    /* 2. Hero Mobile Overlay */
    .hero-split {
        position: relative !important;
        padding-bottom: 80px !important; /* Space for absolute elements if needed */
    }
    .main-message {
        display: none !important;
    }
    /* We place sub-message over the image by positioning it absolutely to the base container */
    .sub-message {
        position: absolute !important;
        bottom: 200px !important; /* Position roughly over the image's top bounds */
        left: 50% !important;
        transform: translateX(-50%) !important;
        width: 90% !important;
        background: rgba(255, 255, 255, 0.95) !important;
        padding: 15px 10px !important;
        border-radius: 8px !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15) !important;
        text-align: center !important;
        z-index: 20 !important;
    }

    /* 3. Swiper Physics Fixing */
    .sp-carousel-wrapper {
        justify-content: flex-start !important;
    }
    .sp-carousel-wrapper > * {
        scroll-snap-align: start !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
    }

    /* 4. Review Card Titles */
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

    /* 5. Shop Info Alignment */
    .shop-table th, .shop-table td {
        padding-left: 15px !important;
        padding-right: 15px !important;
        text-align: left !important;
    }

    /* 6. FAQ Cleanup */
    .faq-lead {
        display: none !important;
    }
}
"""

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

if 'PHASE 11: SAFE MOBILE UX POLISH' not in css:
    css += '\n' + css_fixes
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

def process_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Apply Worries Title Fix (SAFE)
    content = content.replace('<h2>こんなお悩み<br class="sp-only">ありませんか？</h2>', '<h2>こんなお悩みで<br class="sp-only">ありませんか？</h2>')
    content = content.replace('<h2>こんなお悩み<br>ありませんか？</h2>', '<h2>こんなお悩みで<br>ありませんか？</h2>')
    content = content.replace('<h2 class="worries-title">こんなお悩み、ありませんか？</h2>', '<h2 class="worries-title">こんなお悩みで<br class="sp-only">ありませんか？</h2>')

    # Inject Review Title (SAFE because of display: none on PC, which we add inline or via CSS)
    # The class 'sp-review-card-title sp-only' guarantees it vanishes on desktop!
    title_hook = '<h4 class="sp-review-card-title sp-only" style="display:none;">お客様の声</h4>'
    if 'sp-review-card-title' not in content and 'class="review-card"' in content:
        content = content.replace('<div class="review-card">', f'<div class="review-card">\n                        {title_hook}')

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

files_to_process = [
    'stretchplus-theme/template-parts/section-worries.php',
    'stretchplus-theme/template-parts/section-reviews.php',
    'index.html',
    'redesign/index.html'
]

for f in files_to_process:
    process_file(f)

print("Safe Phase 11 Hotfix Complete.")
