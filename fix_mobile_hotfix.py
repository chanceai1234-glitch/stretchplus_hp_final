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
        align-items: flex-start !important; /* Prevents stretching if flex height is weird */
    }
    .header-logo {
        max-width: 50% !important;
    }
    .header-logo img {
        height: auto !important;
        width: 100% !important;
        max-width: 140px !important;
    }
    .hero-split {
        overflow: hidden !important;
    }
    .hero-image-col {
        height: auto !important;
        margin-bottom: 30px !important;
    }
    .hero-image-wrapper {
        width: 90vw !important;
        height: 90vw !important;
        max-width: 380px !important;
        max-height: 380px !important;
        margin: 0 auto !important;
        position: relative !important;
        right: auto !important;
    }
    .hero-image-bg-circle {
        width: 100% !important;
        height: 100% !important;
        left: 0 !important;
        transform: none !important;
    }
    .hero-masked-image {
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
    }
    .main-message {
        font-size: clamp(1.2rem, 5vw, 1.8rem) !important;
        line-height: 1.4 !important;
    }
    .hero-actions {
        flex-direction: column !important;
    }
    .hero-actions .btn {
        width: 100% !important;
        text-align: center !important;
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
