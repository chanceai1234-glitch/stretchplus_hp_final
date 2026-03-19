import os

css_append = """
/* ==========================================================================
   PHASE 13: SAFIE-STYLE MOBILE HEADER
   ========================================================================== */
@media (max-width: 768px) {
    #header {
        position: sticky !important;
        top: 0 !important;
        background: #ffffff !important;
        height: 60px !important;
        padding: 0 15px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        z-index: 1000 !important;
    }
    
    .header-logo {
        display: flex !important;
        align-items: center !important;
        height: 100% !important;
        margin: 0 !important;
    }
    
    .header-logo img {
        height: 25px !important; /* Safie proportion */
        width: auto !important;
        max-width: 180px !important;
        margin-top: 0 !important;
    }
    
    .sp-hamburger {
        position: relative !important;
        top: 0 !important;
        right: 0 !important;
        margin-left: auto !important;
        width: 25px !important;
        height: 18px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        margin-top: 0 !important;
    }
    
    .sp-hamburger span {
        background-color: var(--primary-color) !important;
        height: 2px !important;
        width: 100% !important;
        border-radius: 2px !important;
        position: static !important;
        transform: none !important;
    }
    
    /* Hamburger Active State (X form) */
    .sp-hamburger.is-active span:nth-child(1) {
        transform: translateY(8px) rotate(45deg) !important;
    }
    .sp-hamburger.is-active span:nth-child(2) {
        opacity: 0 !important;
    }
    .sp-hamburger.is-active span:nth-child(3) {
        transform: translateY(-8px) rotate(-45deg) !important;
    }
    
    /* Adjust Hero positioning to sit structurally underneath the 60px header */
    .hero-split {
        padding-top: 0 !important; /* It flows under sticky natively without padding */
    }
    .hero-inner {
        height: calc(100vh - 60px) !important; /* Compensate for header height strictly */
        min-height: 550px !important;
    }
}
"""

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()
if 'PHASE 13: SAFIE-STYLE MOBILE HEADER' not in css:
    css += '\n' + css_append
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ Header Hotfix Applied")
