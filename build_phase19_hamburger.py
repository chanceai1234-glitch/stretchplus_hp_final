import re

css_append = """
/* ==========================================================================
   PHASE 19: SAFIE-STYLE FULL HAMBURGER MENU OVERHAUL
   ========================================================================== */
@media (max-width: 768px) {
    /* 1. Force Hamburger to front and visible */
    .sp-hamburger {
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        width: 25px !important;
        height: 18px !important;
        position: absolute !important;
        right: 15px !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        z-index: 10005 !important;
        background: none !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
        cursor: pointer !important;
    }
    
    .sp-hamburger span {
        width: 100% !important;
        height: 2px !important;
        background: var(--primary-color) !important;
        transition: all 0.3s ease !important;
        border-radius: 2px !important;
    }
    
    .sp-hamburger.is-active span:nth-child(1) {
        transform: translateY(8px) rotate(45deg) !important;
    }
    .sp-hamburger.is-active span:nth-child(2) {
        opacity: 0 !important;
    }
    .sp-hamburger.is-active span:nth-child(3) {
        transform: translateY(-8px) rotate(-45deg) !important;
    }

    /* 2. Safie Overlay White Theme */
    .sp-nav-menu {
        position: fixed !important;
        top: 60px !important; /* Launch strictly below sticky header */
        left: 0 !important;
        width: 100vw !important;
        height: calc(100vh - 60px) !important;
        background: #ffffff !important;
        z-index: 10000 !important;
        overflow-y: auto !important;
        padding: 10px 20px 80px 20px !important;
        transition: transform 0.3s ease, opacity 0.3s ease !important;
        transform: translateX(100%) !important; /* Slide in from right */
        opacity: 0 !important;
        visibility: hidden !important;
    }
    
    .sp-nav-menu.is-active {
        transform: translateX(0) !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    /* 3. Link Architecture (List Borders + Plus Icon) */
    .sp-nav-menu ul {
        list-style: none !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        flex-wrap: wrap !important;
    }
    
    .sp-nav-menu > ul > li {
        width: 100% !important;
    }
    
    /* Hide top CTA */
    li.sp-nav-cta {
        display: none !important;
    }

    .sp-nav-link {
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        padding: 22px 0 !important;
        border-bottom: 2px solid #f0f0f0 !important; /* Clean gray line */
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        color: #111 !important;
        text-decoration: none !important;
    }
    
    .sp-nav-link::after {
        content: '+' !important;
        font-size: 1.5rem !important;
        color: #888 !important;
        font-weight: 300 !important;
    }

    /* 4. Split Safie Bottom Pill Buttons */
    .sp-nav-menu > ul > li.sp-nav-bottom-cta {
        width: 48% !important; /* Split width */
        margin-top: 40px !important;
    }
    
    .sp-nav-menu > ul > li.sp-nav-bottom-cta.web {
        margin-right: 4% !important;
    }
    
    .sp-nav-bottom-cta a.btn {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        padding: 12px 10px !important;
        font-size: 0.85rem !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        text-decoration: none !important;
        color: #ffffff !important;
    }
    
    /* Keep brand colors but use Safie pill structure */
    .sp-nav-bottom-cta.web a.btn {
        background-color: #E6006E !important; /* Safie Pink to perfectly match the requested image reference */
    }
    .sp-nav-bottom-cta.line a.btn {
        background-color: #000000 !important; /* Safie Black to perfectly match reference */
    }
}
"""

css_path = 'stretchplus-theme/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if 'PHASE 19:' not in css:
    css += '\n' + css_append
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# Scrub duplicate JS block created by Phase 16/17 overlap
footer_path = 'stretchplus-theme/footer.php'
with open(footer_path, 'r', encoding='utf-8') as f:
    footer = f.read()

pattern = re.compile(
    r'(// Keep the manual swipe tracked.*?spCurrentIndex = closest;\s*\}\s*\}\);\s*\})[\s\S]*?(// Keep the manual swipe tracked.*?spCurrentIndex = closest;\s*\}\s*\}\);\s*\})'
)
if pattern.search(footer):
    # Regex is tricky across multiple duplicate blocks. Let's do a simple string find/replace
    dup_string = """                    } else {
                        const cards = reviewGrid.querySelectorAll('.review-card');
                        const itemsPerView = getItemsPerView();
                        const maxSlide = Math.max(0, cards.length - itemsPerView);
                        if (currentSlide < maxSlide) {
                            currentSlide = Math.min(maxSlide, currentSlide + itemsPerView);
                            updateSliderPosition();
                        }
                    }
                });
                
                // Keep the manual swipe tracked
                if(reviewGrid) {
                    reviewGrid.addEventListener('scroll', () => {
                        if (window.innerWidth <= 768) {
                            const cards = reviewGrid.querySelectorAll('.review-card');
                            if(!cards.length) return;
                            const center = reviewGrid.scrollLeft + (reviewGrid.clientWidth / 2);
                            let closest = 0;
                            let minDistance = Infinity;
                            cards.forEach((card, i) => {
                                const cardCenter = card.offsetLeft + (card.offsetWidth / 2);
                                const dist = Math.abs(center - cardCenter);
                                if(dist < minDistance) {
                                    minDistance = dist;
                                    closest = i;
                                }
                            });
                            spCurrentIndex = closest;
                        }
                    });
                }"""
    
    # We count occurrences
    if footer.count(dup_string) > 1:
        # replace the first occurrence with empty, thus leaving only one
        footer = footer.replace(dup_string, "", 1)
        with open(footer_path, 'w', encoding='utf-8') as f:
            f.write(footer)
            
print("✅ Phase 19 Safie Hamburger Overhaul Implemented")
