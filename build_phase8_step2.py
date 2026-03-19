import os
import re

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update CSS
css_fixes = """
    /* PHASE 8 STEP 2: PREMIUM BANNERS & CAROUSEL UI */
    
    /* 1. Premium Hero Banner */
    .hero-note {
        background: linear-gradient(135deg, #ffffff 0%, #fafafa 100%) !important;
        border: 2px solid #D4AF37 !important; /* Premium Gold */
        box-shadow: 0 10px 25px rgba(212, 175, 55, 0.15), inset 0 0 15px rgba(212, 175, 55, 0.05) !important;
        position: relative !important;
        overflow: hidden !important;
        padding: 24px 15px !important;
        border-radius: 12px !important;
        width: 95% !important;
        margin: 10px auto 30px auto !important;
    }
    .hero-note::before {
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 50%; height: 100%;
        background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.9) 50%, rgba(255,255,255,0) 100%);
        transform: skewX(-25deg);
        animation: premiumShine 4s infinite;
    }
    @keyframes premiumShine {
        0% { left: -100%; }
        20% { left: 200%; }
        100% { left: 200%; }
    }
    .sp-price-top {
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        color: #4a4a4a !important;
        letter-spacing: 1px !important;
    }
    .sp-price-bottom {
        font-size: 3.2rem !important;
        color: #C00000 !important; /* Deep Red */
        text-shadow: 1px 1px 0px rgba(0,0,0,0.1) !important;
        margin-top: 5px !important;
    }
    .sp-price-bottom .arrow {
        color: #D4AF37 !important; /* Gold Arrow */
    }
    .hero-message .sub-message {
        font-size: 3.5vw !important; /* Prevent orphan wrapping dynamically */
    }

    /* 2. Hide Redundant Mobile Elements */
    .review-bubble {
        display: none !important; /* Hide speech bubbles */
    }
    .review-badge-text {
        display: none !important; /* Hide "Lots of reviews" */
    }
    .flow-lead {
        display: none !important; /* Hide Flow subtext */
    }

    /* 3. Shop Image Fix */
    .shop-info-slideshow {
        width: 100vw !important;
        margin-left: -5vw !important;
        margin-right: -5vw !important;
        overflow: hidden !important;
    }
    .shop-info-slideshow img {
        width: 100% !important;
        height: auto !important;
        object-fit: cover !important;
    }

    /* 4. Carousel Card Width & Arrows */
    .sp-carousel-wrapper > * {
        flex: 0 0 90vw !important; /* Wider to fit 1 instruction securely */
        max-width: 90vw !important;
    }
    .sp-swipe-arrow {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 40px;
        height: 40px;
        background: rgba(0,0,0,0.4);
        border-radius: 50%;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        z-index: 10;
        cursor: pointer;
    }
    .sp-swipe-arrow.left { left: 0px; }
    .sp-swipe-arrow.right { right: 0px; }
"""

if 'PHASE 8 STEP 2' not in css:
    css += '\n' + css_fixes
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Modify specific files for DOM
def process_html_file(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Change "豊富な設備・アメニティ" to "設備・アメニティ"
    content = content.replace('<h2>豊富な設備・アメニティ</h2>', '<h2>設備・アメニティ</h2>')

    # Inject Arrow JS logic into Footer/HTML bottoms
    arrow_js = """
        // Inject Swipe Arrows for Carousels on Mobile
        if(window.innerWidth <= 768) {
            document.querySelectorAll('.sp-carousel-wrapper').forEach(wrapper => {
                const parent = wrapper.parentElement;
                parent.style.position = 'relative';
                
                const leftArrow = document.createElement('div');
                leftArrow.className = 'sp-swipe-arrow left';
                leftArrow.innerHTML = '&#10094;';
                
                const rightArrow = document.createElement('div');
                rightArrow.className = 'sp-swipe-arrow right';
                rightArrow.innerHTML = '&#10095;';
                
                parent.appendChild(leftArrow);
                parent.appendChild(rightArrow);
                
                const scrollWidth = window.innerWidth * 0.9;
                leftArrow.addEventListener('click', () => wrapper.scrollBy({left: -scrollWidth, behavior: 'smooth'}));
                rightArrow.addEventListener('click', () => wrapper.scrollBy({left: scrollWidth, behavior: 'smooth'}));
            });
        }
    """
    if '// Inject Swipe Arrows' not in content:
        script_tag_end = content.rfind('</script>')
        if script_tag_end != -1:
            content = content[:script_tag_end] + arrow_js + content[script_tag_end:]
            
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

process_html_file('stretchplus-theme/template-parts/section-amenities.php')
process_html_file('stretchplus-theme/footer.php')
process_html_file('index.html')
process_html_file('redesign/index.html')

print("Phase 8 Step 2 Complete.")
