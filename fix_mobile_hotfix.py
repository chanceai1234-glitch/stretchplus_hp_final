import sys

try:
    with open("stretchplus-theme/style.css", "r", encoding="utf-8") as f:
        css = f.read()

        
    # Append safe header overrides at the bottom
    appended_css = """

/* --- GLOBAL HOTFIXES --- */
html, body {
    overflow-x: hidden !important;
    max-width: 100vw;
    position: relative;
    width: 100%;
}
.bg-beige {
    background-color: #FAF4E8 !important; /* Gentle beige/sand color */
}
.flow-triangle-down-beige {
    position: absolute;
    bottom: -30px;
    left: 50%;
    transform: translateX(-50%);
    width: 0; 
    height: 0; 
    border-left: 40px solid transparent;
    border-right: 40px solid transparent;
    border-top: 30px solid #FAF4E8;
    z-index: 10;
}

/* --- BACK TO TOP BUTTON --- */
.back-to-top {
    position: fixed;
    bottom: 30px;
    right: 20px;
    width: 45px;
    height: 45px;
    background: rgba(0,0,0,0.5);
    color: #fff;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 8000;
    text-decoration: none;
    font-size: 1.2rem;
    transition: background 0.3s;
}
.back-to-top:hover {
    background: rgba(0,0,0,0.8);
    color: #fff;
}

/* --- FAQ TABS --- */
.faq-tabs-nav {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 25px;
    flex-wrap: wrap;
}
.faq-tab {
    padding: 8px 18px;
    border: 2px solid var(--primary-color);
    background: #fff;
    color: var(--primary-color);
    border-radius: 30px;
    cursor: pointer;
    font-weight: bold;
    font-size: 0.95rem;
    transition: all 0.3s;
}
.faq-tab.active {
    background: var(--primary-color);
    color: #fff;
}
.faq-tab-pane {
    display: none;
}
.faq-tab-pane.active {
    display: block;
}

/* --- TABLE OVERFLOW HOTFIX --- */
.shop-address-line1 {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 5px;
}
.shop-address-line1 span {
    word-break: break-all;
}

/* =========================================
   MOBILE LAYOUT HOTFIXES
   ========================================= */
   
#hero {
    padding-top: 140px !important; /* increased to prevent header overlap */
    padding-bottom: 30px !important;
}
.hero-split {
    overflow: hidden !important;
    width: 100% !important;
}
@media (max-width: 991px) {
    /* --- PC / SP VISIBILITY --- */
    .pc-only {
        display: none !important;
    }
    .sp-only {
        display: block !important;
    }
    
    #header {
        padding: 15px 5% !important;
        background: rgba(255, 255, 255, 0.95); /* Ensure readability */
    }
    .header-logo {
        max-width: 60% !important;
    }
    .header-logo img {
        height: auto !important;
        width: 100% !important;
        max-width: 160px !important;
    }
    .header-actions {
        display: none !important;
    }
    
    /* Hamburger Button */
    .hamburger-btn {
        display: block !important;
        position: absolute;
        top: 20px;
        right: 5%;
        width: 30px;
        height: 24px;
        background: transparent;
        border: none;
        cursor: pointer;
        z-index: 1100;
    }
    .hamburger-btn span {
        display: block;
        position: absolute;
        height: 2px;
        width: 100%;
        background: var(--primary-color);
        border-radius: 2px;
        transition: 0.3s ease-in-out;
    }
    .hamburger-btn span:nth-child(1) { top: 0px; }
    .hamburger-btn span:nth-child(2) { top: 11px; }
    .hamburger-btn span:nth-child(3) { top: 22px; }
    
    .hamburger-btn.active span:nth-child(1) {
        top: 11px;
        transform: rotate(45deg);
    }
    .hamburger-btn.active span:nth-child(2) {
        opacity: 0;
    }
    .hamburger-btn.active span:nth-child(3) {
        top: 11px;
        transform: rotate(-45deg);
    }

    /* Mobile Nav Overlay */
    #header-nav {
        display: block !important;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        background: rgba(255, 255, 255, 0.98);
        z-index: 1050;
        transform: translateY(-100%);
        transition: transform 0.4s ease-in-out;
        display: flex !important;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        visibility: hidden;
    }
    #header-nav.active {
        transform: translateY(0);
        visibility: visible;
    }
    #header-nav ul {
        flex-direction: column !important;
        gap: 30px !important;
        text-align: center;
        padding: 0;
    }
    #header-nav a {
        font-size: 1.2rem !important;
        font-weight: 700 !important;
    }
    
    /* Standardize horizontal padding for all sections */
    #hero, #about, #worries, #reviews, #menu, #flow, #trainers, #amenities, #policy, #info, #faq, #access {
        padding-left: 5% !important;
        padding-right: 5% !important;
        box-sizing: border-box !important;
    }
    
    /* Force Shop Info Elements to Wrap */
    .shop-info-block {
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        overflow: hidden !important;
    }
    .shop-table {
        width: 100% !important;
        max-width: 100% !important;
        table-layout: fixed !important;
    }
    .shop-table th, .shop-table td {
        word-break: break-all !important;
        word-wrap: break-word !important;
        white-space: normal !important;
        display: block !important;
        width: 100% !important;
        padding: 5px 0 !important;
    }
    .shop-info-slideshow, .shop-info-slideshow img {
        width: 100% !important;
        max-width: 100% !important;
        height: auto !important;
    }
    .shop-address-wrapper {
        display: block !important;
    }
    .hero-image-col {
        height: auto !important;
        margin-bottom: 20px !important;
        order: -1;
    }
    .about-image {
        width: 100% !important;
        max-width: 100% !important;
        flex: 0 0 100% !important;
        margin-top: 15px !important;
    }
    .about-image img, .persona-image img {
        width: 100% !important;
        height: auto !important;
        max-width: 100% !important;
        border-radius: 8px !important;
        object-fit: cover !important;
    }
    .persona-image {
        width: 100% !important;
        max-width: 100% !important;
        flex: 0 0 100% !important;
        margin-top: 15px !important;
        text-align: center;
    }
    
    /* Sticky bottom nav 2x2 override */
    .sp-sticky-nav {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 2px !important;
        height: auto !important;
        padding: 0 !important;
    }
    .sp-sticky-nav a {
        padding: 15px 0 !important;
        height: auto !important;
        box-sizing: border-box !important;
    }
    body {
        padding-bottom: 120px !important; /* clear 2 rows of sticky nav */
    }
    
    /* Make back to top button dodge the sticky footer */
    .back-to-top {
        bottom: 120px !important;
        right: 10px !important;
        width: 40px !important;
        height: 40px !important;
        font-size: 1rem !important;
    }
    .review-slider-container {
        padding: 0 !important;
    }
    .review-grid-wrapper {
        margin: 0 !important;
        padding: 0 !important;
    }
    .review-card {
        width: 90vw !important;
        max-width: 90vw !important;
        flex: 0 0 90vw !important;
        padding: 20px 15px !important;
        box-sizing: border-box !important;
        height: auto !important;
        display: flex !important;
        flex-direction: column !important;
        align-self: stretch !important;
        background: #fff !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    }
    .review-grid {
        gap: 15px !important;
        align-items: stretch !important;
        display: flex !important;
    }
    /* Dynamic Mobile Review Restructuring */
    .review-bubble {
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        border: none !important;
    }
    .review-bubble::after, .review-quote .highlight-text, .review-quote br {
        display: none !important;
    }
    .review-user {
        display: block !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        border-bottom: 2px solid var(--primary-color) !important;
        padding-bottom: 10px !important;
        margin-bottom: 15px !important;
        text-align: center !important;
        color: var(--primary-color) !important;
    }
    .feedback-heading {
        display: none !important;
    }
    .review-header {
        font-weight: bold !important;
        font-size: 1.1rem !important;
        border-bottom: 2px solid var(--primary-color) !important;
        padding-bottom: 10px !important;
        margin-bottom: 15px !important;
        text-align: center !important;
        color: var(--primary-color) !important;
    }
    .review-episode {
        flex: 1 !important;
        display: flex !important;
        flex-direction: column !important;
    }
    .review-card p, .review-card h4, .review-card span {
        white-space: normal !important;
        word-wrap: break-word !important;
        word-break: break-all !important;
    }
    .review-feedback, .review-quote {
        font-size: 0.95rem !important;
        line-height: 1.5 !important;
    }

    /* Keep Hero Image Square / Natural without circular crops */
    .hero-image-wrapper {
        width: 100% !important;
        height: auto !important;
        max-width: 100% !important;
        max-height: none !important;
        margin: 0 auto !important;
        position: relative !important;
        right: auto !important;
        border-radius: 0 !important;
    }
    .hero-image-bg-circle {
        display: none !important; /* Remove decorative background circle */
    }
    .hero-masked-image {
        width: 100% !important;
        height: auto !important;
        top: 0 !important;
        left: 0 !important;
        transform: none !important;
        object-fit: contain !important;
        border-radius: 8px !important; /* Slight rectangle rounding */
        position: static !important;
    }
    .main-message {
        font-size: clamp(1.4rem, 6vw, 1.8rem) !important;
        line-height: 1.4 !important;
        text-align: center;
    }
    .sub-message {
        text-align: center;
        margin-top: 15px;
    }
    .hero-actions-wrapper {
        text-align: center;
        margin-top: 30px;
    }
}
"""
    css += appended_css
    
    with open("stretchplus-theme/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    
    print("✅ style.css successfully patched with mobile hotfixes.")

except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
