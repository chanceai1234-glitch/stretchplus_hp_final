import os

css_append = """
/* ==========================================================================
   PHASE 15: HERO TEXT CENTERING & STRICT 1-VIEWPORT CAROUSEL PHYSICS
   ========================================================================== */
@media (max-width: 768px) {
    /* 1. Hero Text Precise Center Docking */
    .hero-content {
        justify-content: center !important; /* Pulls text down into exact middle */
        padding-top: 5vh !important;
        padding-bottom: 5vh !important;
        align-items: center !important;
    }
    .hero-actions-wrapper {
        margin-top: 25px !important; /* Cancel prior 'auto' gravity pushing buttons to floor */
        width: 100% !important;
    }
    
    /* 2. Review and Flow exact 1-card-per-screen viewport matching */
    .sp-carousel-wrapper {
        padding-left: 5vw !important;
        padding-right: 5vw !important;
        scroll-padding-left: 5vw !important; /* Pre-align scroll boundaries */
        justify-content: flex-start !important; /* Break any inherited centering pulling things out of flow */
    }
    
    .sp-carousel-wrapper .review-card,
    .sp-carousel-wrapper .flow-step,
    .sp-carousel-wrapper .amenity-card {
        min-width: 90vw !important;
        max-width: 90vw !important;
        scroll-snap-align: center !important;
        scroll-snap-stop: always !important; /* Prevent sliding over multiple cards blindly */
        flex: 0 0 auto !important;
        margin-left: 0 !important;
        margin-right: 15px !important;
        box-sizing: border-box !important;
    }

    /* Target nested geometry inside flow-step so horizontal layout doesn't crash width constraints */
    .flow-step-inner {
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        width: 100% !important;
    }
    .flow-step-image-wrapper {
        width: 100% !important;
        max-width: 100% !important;
        margin-bottom: 20px !important;
    }
    .flow-step-text-wrapper {
        width: 100% !important;
        margin-top: 0 !important;
        padding: 0 10px !important;
        box-sizing: border-box !important;
    }
}
"""

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

if 'PHASE 15: HERO TEXT CENTERING' not in css:
    css += '\n' + css_append
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ Phase 15 UI Geometry Appended")
else:
    print("✅ Phase 15 already exists")
