import re
import shutil

# --- 1. Propagate User's index.html Manual Edits to PHP Templates ---

header_path = "stretchplus-theme/header.php"
with open(header_path, 'r', encoding='utf-8') as f:
    header_content = f.read()
if 'sp-nav-bottom-cta web' not in header_content:
    injection = """                <li><a href="#access" class="sp-nav-link">店舗情報・アクセス</a></li>
                <li class="sp-nav-bottom-cta web" style="margin-top: 30px;"><a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web" target="_blank" style="width: 100%; padding: 15px;">Web予約 <i class="fas fa-chevron-right"></i></a></li>
                <li class="sp-nav-bottom-cta line" style="margin-top: 15px;"><a href="https://lin.ee/rboKm7N" class="btn btn-line" target="_blank" style="width: 100%; padding: 15px; background-color: var(--line-color); color: #fff;">LINE相談 <i class="fas fa-chevron-right"></i></a></li>"""
    header_content = header_content.replace('<li><a href="#access" class="sp-nav-link">店舗情報・アクセス</a></li>', injection)
    with open(header_path, 'w', encoding='utf-8') as f:
        f.write(header_content)

worries_path = "stretchplus-theme/template-parts/section-worries.php"
with open(worries_path, 'r', encoding='utf-8') as f:
    worries_content = f.read()
if 'こんなお悩みで' in worries_content:
    worries_content = worries_content.replace('こんなお悩みで<br', 'こんなお悩み<br')
    with open(worries_path, 'w', encoding='utf-8') as f:
        f.write(worries_content)

# --- 2. Fix JS Slider Drift in footer.php and index.html ---

def fix_slider_js(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The drift happens because css has a 15px gap but JS hardcodes 30.
    # More importantly, on mobile we MUST use scrollBy.
    js_replace = """                prevReviewBtn.addEventListener('click', () => {
                    if (window.innerWidth <= 768) {
                        const card = reviewGrid.querySelector('.review-card');
                        if(card) {
                            const style = window.getComputedStyle(card);
                            const margin = parseInt(style.marginRight, 10) || 0;
                            reviewGrid.scrollBy({ left: -(card.offsetWidth + margin), behavior: 'smooth' });
                        }
                    } else {
                        const itemsPerView = getItemsPerView();
                        if (currentSlide > 0) {
                            currentSlide = Math.max(0, currentSlide - itemsPerView);
                            updateSliderPosition();
                        }
                    }
                });

                nextReviewBtn.addEventListener('click', () => {
                    if (window.innerWidth <= 768) {
                        const card = reviewGrid.querySelector('.review-card');
                        if(card) {
                            const style = window.getComputedStyle(card);
                            const margin = parseInt(style.marginRight, 10) || 0;
                            reviewGrid.scrollBy({ left: (card.offsetWidth + margin), behavior: 'smooth' });
                        }
                    } else {
                        const cards = reviewGrid.querySelectorAll('.review-card');
                        const itemsPerView = getItemsPerView();
                        const maxSlide = Math.max(0, cards.length - itemsPerView);
                        if (currentSlide < maxSlide) {
                            currentSlide = Math.min(maxSlide, currentSlide + itemsPerView);
                            updateSliderPosition();
                        }
                    }
                });"""

    # We use regex to replace the old event listeners
    pattern = re.compile(
        r'prevReviewBtn\.addEventListener\(\'click\', \(\) => \{.+?nextReviewBtn\.addEventListener\(\'click\', \(\) => \{.+?\}\);',
        re.DOTALL
    )
    if 'scrollBy({ left' not in content:
        content = pattern.sub(js_replace, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

fix_slider_js('stretchplus-theme/footer.php')
fix_slider_js('redesign/index.html')
# The user's index.html was modified by them, but we want to restore the Review slider!
# Let's extract section-reviews.php HTML and put it back into index.html
with open('stretchplus-theme/template-parts/section-reviews.php', 'r', encoding='utf-8') as f:
    php_reviews = f.read()
    php_reviews = php_reviews.replace('<?php echo get_template_directory_uri(); ?>/', '')
with open('redesign/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
pattern = re.compile(r'<section id="reviews" class="reveal">.+?</section>', re.DOTALL)
html_content = pattern.sub(php_reviews, html_content)
# Apply the manual fixes to index.html as well for safe keeping
html_content = html_content.replace('こんなお悩みで<br', 'こんなお悩み<br')
with open('redesign/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# --- 3. Morph .flow-step into Vertical Timeline via CSS ---

css_append = """
/* ==========================================================================
   PHASE 16: FLOW SECTION VERTICAL TIMELINE MUTATION
   ========================================================================== */
@media (max-width: 768px) {
    /* Explode the carousel wrapper specifically for flow */
    #flow .sp-carousel-wrapper {
        display: block !important;
        overflow: visible !important;
        padding: 0 !important;
        white-space: normal !important;
    }
    
    .flow-step {
        width: 100% !important;
        min-width: 100% !important;
        max-width: 100% !important;
        padding: 40px 15px 50px !important;
        margin: 0 !important;
        background: var(--bg-light) !important;
        position: relative !important;
        scroll-snap-align: none !important;
        text-align: left !important;
    }
    .flow-step:nth-child(even) {
        background: #ffffff !important;
    }

    /* Interlocking descending triangles */
    .flow-step::before {
        content: '';
        position: absolute;
        top: 0; left: 50%;
        transform: translate(-50%, -100%);
        width: 0; height: 0;
        border-left: 20px solid transparent;
        border-right: 20px solid transparent;
        border-top: 20px solid #ffffff;
        z-index: 5;
    }
    .flow-step:nth-child(odd)::before { border-top-color: #ffffff; }
    .flow-step:nth-child(even)::before { border-top-color: var(--bg-light); }
    .flow-step:first-child::before { display: none; }
    
    .flow-step-inner {
        display: block !important;
        padding: 0 !important;
        max-width: 100% !important;
    }
    
    /* Decouple logic */
    .flow-step-text-wrapper {
        display: contents !important;
    }
    
    /* Image floats left */
    .flow-step-image-wrapper {
        float: left !important;
        width: 42% !important;
        margin: 0 15px 10px 0 !important;
    }
    .flow-step-image-wrapper img {
        border-radius: 6px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
    }
    
    /* Title occupies right space */
    .flow-step-header {
        overflow: hidden !important; 
        display: block !important;
        text-align: left !important;
        margin-top: 0 !important;
    }
    .flow-step-number {
        display: inline-block !important;
        background: var(--primary-color) !important;
        color: #ffffff !important;
        font-size: 0.8rem !important;
        padding: 4px 12px !important;
        border-radius: 20px !important;
        margin-bottom: 10px !important;
        font-weight: bold !important;
    }
    .flow-step-title {
        display: block !important;
        font-size: 1.05rem !important;
        line-height: 1.4 !important;
        border-bottom: 2px solid #333 !important;
        padding-bottom: 6px !important;
        margin-bottom: 0 !important;
        color: #111 !important;
    }
    
    /* Description wraps cleanly underneath everything */
    .flow-step-desc {
        clear: both !important;
        display: block !important;
        width: 100% !important;
        padding-top: 20px !important;
        font-size: 0.9rem !important;
        line-height: 1.6 !important;
        color: #333 !important;
        text-align: left !important;
    }
}
"""

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

if 'PHASE 16: FLOW SECTION VERTICAL TIMELINE' not in css:
    css += '\n' + css_append
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

print("✅ Phase 16 executed: Carousel Drift fixed, Flow Vertical Timeline morphed, manual edits ingested.")
