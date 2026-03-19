import os

css_append = """
/* ==========================================================================
   PHASE 18: UNIVERSAL SLIDER PURGE (CENTRAL VERTICAL STACK FOR ALL DEVICES)
   ========================================================================== */
@media (max-width: 768px) {
    /* Annihilate horizontal native scroll across Amenities, Reviews, Trainers, Flow */
    .sp-carousel-wrapper {
        display: flex !important;
        flex-direction: column !important;
        flex-wrap: nowrap !important;
        overflow: visible !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 5vw !important; /* Standard edge constraint */
        scroll-snap-type: none !important;
    }
    
    /* Expand all inner cards to rigidly fill the viewport width */
    .sp-carousel-wrapper > * {
        width: 100% !important;
        min-width: 100% !important;
        max-width: 100% !important;
        margin: 0 0 40px 0 !important; /* Vertical gap replaces horizontal margin */
        scroll-snap-align: none !important;
        flex: 0 0 auto !important;
    }

    /* Target specific components that had horizontal specifics */
    .review-card, .amenity-card {
        margin-right: 0 !important; /* Wipe old slider margins */
        margin-left: 0 !important;
    }

    /* Hide ALL horizontal arrow buttons and scroll progressions globally on mobile */
    .slider-btn, .review-progress-container, .swiper-button-next, .swiper-button-prev { 
        display: none !important; 
    }
}
"""

css_path = 'stretchplus-theme/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if 'PHASE 18:' not in css:
    css += '\n' + css_append
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
print("✅ Phase 18 Universal Sliders Purged (Stacked Centered Columns Online)")
