import re

css_append = """
@media (max-width: 900px) {
    /* ---------------------------------------------------
       PHASE 30: HORIZONTAL CSS-SNAP CAROUSELS
       --------------------------------------------------- */
    .flow-steps-wrapper,
    .amenities-grid,
    .trainer-grid,
    .access-cards-container {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        overflow-y: hidden !important;
        scroll-snap-type: x mandatory !important;
        -webkit-overflow-scrolling: touch !important;
        scrollbar-width: none !important;
        -ms-overflow-style: none !important;
        padding-bottom: 30px !important;
        padding-left: 5vw !important;
        padding-right: 5vw !important;
        gap: 15px !important;
        /* Disable PC alignment overrides */
        justify-content: flex-start !important;
        margin-left: calc(-50vw + 50%) !important;
        margin-right: calc(-50vw + 50%) !important;
        width: 100vw !important;
        max-width: 100vw !important;
    }

    .flow-steps-wrapper::-webkit-scrollbar,
    .amenities-grid::-webkit-scrollbar,
    .trainer-grid::-webkit-scrollbar,
    .access-cards-container::-webkit-scrollbar {
        display: none !important;
    }

    .flow-step,
    .amenity-card,
    .trainer-card,
    .access-card {
        scroll-snap-align: center !important;
        scroll-snap-stop: always !important;
        flex: 0 0 85vw !important;
        min-width: 85vw !important;
        max-width: 85vw !important;
        margin: 0 !important;
    }

    /* Fix image aspect ratios in Flow and Amenities */
    .flow-step-image img,
    .amenity-img-wrapper img,
    .access-card-img img {
        width: 100% !important;
        object-fit: cover !important;
        height: auto !important;
    }

    /* Hide flow downward triangles on horizontal UI */
    .flow-triangle-down-blue,
    .flow-triangle-down-white,
    .flow-triangle-down-beige {
        display: none !important;
    }
    
    /* Flow specific padding reset */
    .flow-step {
        padding: 30px 0 !important;
    }
}
"""

with open('style.css', 'a') as f:
    f.write(css_append)

print("Appended CSS successfully.")
