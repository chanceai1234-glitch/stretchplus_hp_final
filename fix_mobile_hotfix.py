import sys

try:
    with open("stretchplus-theme/style.css", "r", encoding="utf-8") as f:
        css = f.read()

        
    # Append safe header overrides at the bottom
    appended_css = """

/* --- GLOBAL HOTFIXES --- */
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

/* --- MOBILE HOTFIXES --- */
@media (max-width: 991px) {
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
    
    .hero-split {
        overflow: hidden !important;
        padding-top: 80px !important; /* give space to header */
    }
    .hero-image-col {
        height: auto !important;
        margin-bottom: 10px !important;
        order: -1;
    }
    .about-image {
        width: 100% !important;
        margin-top: 15px !important;
    }
    .about-image img {
        width: 100% !important;
        max-width: 100% !important;
        height: auto !important;
    }
    .review-slider-container {
        padding: 0 !important;
    }
    .review-grid-wrapper {
        margin: 0 !important;
        padding: 0 !important;
    }
    .review-card {
        width: 100vw !important;
        max-width: 100vw !important;
        flex: 0 0 100vw !important;
        padding: 5% 8% !important;
        box-sizing: border-box !important;
    }
    .review-grid {
        gap: 0 !important;
    }
    .hero-image-wrapper {
        width: 85vw !important;
        height: 85vw !important;
        max-width: 350px !important;
        max-height: 350px !important;
        margin: 0 auto !important;
        position: relative !important;
        right: auto !important;
    }
    .hero-image-bg-circle {
        width: 100% !important;
        height: 100% !important;
        top: 0 !important;
        left: 0 !important;
        transform: none !important;
    }
    .hero-masked-image {
        width: 100% !important;
        height: 100% !important;
        top: 0 !important;
        left: 0 !important;
        transform: none !important;
        object-fit: cover !important;
        object-position: center !important;
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
