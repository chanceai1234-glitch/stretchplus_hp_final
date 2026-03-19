import re

css_append = """
/* ==========================================================================
   PHASE 17: HERO HOIST, FLOW CENTERING, AND CAROUSEL PURGE
   ========================================================================== */
@media (max-width: 768px) {
    /* Hoist Hero text into upper quadrant */
    .hero-content {
        justify-content: center !important;
        padding-top: 5vh !important;
        padding-bottom: 25vh !important; /* Force the content box to sit physically higher */
    }

    /* Destroy legacy slider buttons on Flow */
    #flow .slider-btn {
        display: none !important;
    }

    /* Recenter Flow blocks natively instead of floating */
    .flow-step-inner {
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
    }
    
    .flow-step-image-wrapper {
        float: none !important; /* Kill the left alignment float */
        width: 100% !important;
        max-width: 300px !important; /* Keep image elegant */
        margin: 0 auto 20px auto !important;
    }
    
    .flow-step-text-wrapper {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
    }
    
    .flow-step-header {
        text-align: center !important; /* Center the title too */
        width: 100% !important;
    }
    
    .flow-step-desc {
        text-align: left !important; /* Keep paragraph reading natively */
        width: 100% !important;
        padding-top: 15px !important;
    }
}
"""

# Append CSS Fixes
css_path = 'stretchplus-theme/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
if 'PHASE 17:' not in css:
    css += '\n' + css_append
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# Update JS in footer.php and index.html to use mathematically perfect scrollIntoView
def fix_js_strictly(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace the JS chunk deployed in Phase 16
    bad_js = """                prevReviewBtn.addEventListener('click', () => {
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
                
    good_js = """                // Mathematical Drift-Proof JS System
                let spCurrentIndex = 0;
                
                prevReviewBtn.addEventListener('click', () => {
                    if (window.innerWidth <= 768) {
                        const cards = reviewGrid.querySelectorAll('.review-card');
                        if(spCurrentIndex > 0) {
                            spCurrentIndex--;
                            cards[spCurrentIndex].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
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
                        const cards = reviewGrid.querySelectorAll('.review-card');
                        if(spCurrentIndex < cards.length - 1) {
                            spCurrentIndex++;
                            cards[spCurrentIndex].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
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
                
    if bad_js in content:
        content = content.replace(bad_js, good_js)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            
fix_js_strictly('stretchplus-theme/footer.php')
fix_js_strictly('redesign/index.html')

print("✅ Phase 17 fixes injected into system IO.")
