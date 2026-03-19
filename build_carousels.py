import os
import re

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

carousel_css = """
    /* APP-LIKE HORIZONTAL CAROUSELS */
    .sp-carousel-wrapper {
        display: flex !important;
        flex-wrap: nowrap !important;
        flex-direction: row !important;
        overflow-x: auto !important;
        scroll-snap-type: x mandatory !important;
        gap: 20px !important;
        padding-bottom: 20px !important;
        -webkit-overflow-scrolling: touch !important;
        scrollbar-width: none !important; /* Hide standard scrollbar */
        padding-left: 5vw !important; /* Start padding for the scroll */
        padding-right: 5vw !important;
        margin-left: -5vw !important; /* Break out of container padding */
        margin-right: -5vw !important;
    }
    .sp-carousel-wrapper::-webkit-scrollbar {
        display: none !important;
    }
    .sp-carousel-wrapper > * {
        flex: 0 0 85% !important; /* Show 85% of screen width, peeking next card */
        scroll-snap-align: center !important;
        max-width: 85% !important;
        margin-bottom: 0 !important;
    }
    
    /* Flow specific fix because of triangles */
    .flow-step .flow-triangle-down-blue, .flow-step .flow-triangle-down-white, .flow-step .flow-triangle-down-beige {
        display: none !important; /* Hide arrows on horizontal scroll */
    }
    
    /* Hide review slider buttons on mobile */
    .slider-btn {
        display: none !important;
    }
    
    /* Remove chat bubbles from reviews on mobile */
    .review-bubble::after, .review-bubble::before {
        display: none !important;
    }
    .review-bubble {
        border-radius: 8px !important;
        padding: 20px !important;
        background: #f8f8f8 !important;
    }

    /* STORE INFO TABLE FIX */
    .shop-table {
        display: block;
        width: 100%;
        overflow-x: hidden;
    }
    .shop-table tbody {
        display: block;
        width: 100%;
    }
    .shop-table tr {
        display: flex;
        flex-direction: column;
        border-bottom: 1px solid #eee;
        padding: 15px 0;
    }
    .shop-table th, .shop-table td {
        display: block;
        width: 100%;
        padding: 5px 0 !important;
        border: none !important;
    }
    .shop-table th {
        font-weight: bold;
        color: var(--primary-color);
        padding-bottom: 5px !important;
    }
"""

if 'APP-LIKE HORIZONTAL CAROUSELS' not in css:
    hook = '/* HERO FIXES */'
    css = css.replace(hook, carousel_css + '\n    ' + hook)
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

def inject_carousel_classes(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Flow
    content = content.replace('class="flow-steps-wrapper"', 'class="flow-steps-wrapper sp-carousel-wrapper"')
    # Amenities
    content = content.replace('class="amenities-grid"', 'class="amenities-grid sp-carousel-wrapper"')
    # Trainers
    content = content.replace('class="trainers-grid"', 'class="trainers-grid sp-carousel-wrapper"')
    # Access
    content = content.replace('class="access-cards-container"', 'class="access-cards-container sp-carousel-wrapper"')
    # Reviews
    content = content.replace('class="review-grid"', 'class="review-grid sp-carousel-wrapper"')

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

inject_carousel_classes('stretchplus-theme/template-parts/section-flow.php')
inject_carousel_classes('stretchplus-theme/template-parts/section-amenities.php')
inject_carousel_classes('stretchplus-theme/template-parts/section-trainers.php')
inject_carousel_classes('stretchplus-theme/template-parts/section-access.php')
inject_carousel_classes('stretchplus-theme/template-parts/section-reviews.php')
inject_carousel_classes('index.html')
inject_carousel_classes('redesign/index.html')

print("Carousel architecture injected.")
