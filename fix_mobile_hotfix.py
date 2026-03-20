import sys

try:
    with open("stretchplus-theme/style.css", "r", encoding="utf-8") as f:
        css = f.read()

        
    # Append safe header overrides at the bottom
    appended_css = """

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
    .hero-split {
        overflow: hidden !important;
        padding-top: 80px !important; /* give space to header */
    }
    .hero-image-col {
        height: auto !important;
        margin-bottom: 30px !important;
        order: -1;
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
