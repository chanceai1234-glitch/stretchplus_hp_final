import os
import re

# ==========================================
# 1. HTML / PHP DOM IMMUTABLE INJECTIONS
# ==========================================

php_slideshow = """                    <div class="hero-image-bg-circle pc-only"></div>
                    <img src="<?php echo get_template_directory_uri(); ?>/image_final/hero_main.jpg" alt="パーソナルストレッチの様子" class="hero-masked-image pc-only">
                    
                    <!-- Safie Style Mobile Slideshow -->
                    <div class="sp-hero-slideshow sp-only">
                        <div class="sp-slide" style="background-image: url('<?php echo get_template_directory_uri(); ?>/image_final/hero_main.jpg');"></div>
                        <div class="sp-slide" style="background-image: url('<?php echo get_template_directory_uri(); ?>/image_final/about_main.jpg');"></div>
                        <div class="sp-slide" style="background-image: url('<?php echo get_template_directory_uri(); ?>/image_final/flow_step_8.jpg');"></div>
                        <div class="sp-hero-overlay"></div>
                    </div>"""

html_slideshow = """                    <div class="hero-image-bg-circle pc-only"></div>
                    <img src="./image_final/hero_main.jpg" alt="パーソナルストレッチの様子" class="hero-masked-image pc-only">
                    
                    <!-- Safie Style Mobile Slideshow -->
                    <div class="sp-hero-slideshow sp-only">
                        <div class="sp-slide" style="background-image: url('./image_final/hero_main.jpg');"></div>
                        <div class="sp-slide" style="background-image: url('./image_final/about_main.jpg');"></div>
                        <div class="sp-slide" style="background-image: url('./image_final/flow_step_8.jpg');"></div>
                        <div class="sp-hero-overlay"></div>
                    </div>"""

def inject_hero_slideshow(filepath, is_php=False):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicate injection
    if 'sp-hero-slideshow' in content:
        print(f"Skipping {filepath} (Already injected)")
        return

    # Find the target inner wrapper
    target = '<div class="hero-image-bg-circle"></div>'
    if target in content:
        # replace the original circle and img lines entirely
        # We find from <div class="hero-image-bg-circle"></div> down to </div>
        # Safest way: exact regex matching or simple string replace for the known block.
        if is_php:
            old_block = '<div class="hero-image-bg-circle"></div>\n                    <img src="<?php echo get_template_directory_uri(); ?>/image_final/hero_main.jpg" alt="パーソナルストレッチの様子" class="hero-masked-image">'
            content = content.replace(old_block, php_slideshow)
        else:
            old_block = '<div class="hero-image-bg-circle"></div>\n                    <img src="./image_final/hero_main.jpg" alt="パーソナルストレッチの様子" class="hero-masked-image">'
            content = content.replace(old_block, html_slideshow)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Slideshow DOM Injected -> {filepath}")

inject_hero_slideshow('stretchplus-theme/template-parts/section-hero.php', is_php=True)
inject_hero_slideshow('index.html', is_php=False)
inject_hero_slideshow('redesign/index.html', is_php=False)

# ==========================================
# 2. CSS SAFIE ARCHITECTURE INJECTION
# ==========================================

css_append = """
/* ==========================================================================
   PHASE 12: SAFIE-STYLE MOBILE HERO OVERHAUL (100% PC PRESERVATION)
   ========================================================================== */
@media (max-width: 768px) {
    .pc-only { display: none !important; }

    .hero-split {
        padding: 0 !important;
        margin: 0 !important;
    }
    .hero-inner {
        position: relative !important;
        height: 85vh !important;
        min-height: 600px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-end !important;
        overflow: hidden !important;
        padding-top: 0 !important;
    }
    
    .hero-image-col {
        position: absolute !important;
        top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important;
        width: 100vw !important;
        height: 100% !important;
        margin: 0 !important; padding: 0 !important;
        z-index: 1 !important;
    }
    .hero-image-wrapper {
        margin: 0 !important; padding: 0 !important;
        width: 100% !important; height: 100% !important;
        transform: none !important; /* Cancel PC hover pop */
    }

    .sp-hero-slideshow {
        position: absolute !important;
        top: 0 !important; left: 0 !important; width: 100% !important; height: 100% !important;
        display: block !important;
    }

    .sp-slide {
        position: absolute !important;
        top: 0 !important; left: 0 !important; width: 100% !important; height: 100% !important;
        background-size: cover !important;
        background-position: center center !important;
        opacity: 0;
        animation: spFadeInOut 12s infinite;
    }
    .sp-slide:nth-child(1) { animation-delay: 0s; }
    .sp-slide:nth-child(2) { animation-delay: 4s; }
    .sp-slide:nth-child(3) { animation-delay: 8s; }

    @keyframes spFadeInOut {
        0%, 25% { opacity: 1; }
        33%, 92% { opacity: 0; }
        100% { opacity: 1; }
    }

    .sp-hero-overlay {
        position: absolute !important;
        top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important;
        background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%) !important;
        z-index: 2 !important;
        opacity: 1 !important;
    }

    /* Content Z-Layering */
    .hero-content {
        position: relative !important;
        z-index: 10 !important;
        width: 100% !important;
        padding: 0 5vw 8vh 5vw !important; /* 8vh pushes it perfectly up from bottom */
        text-align: center !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-end !important;
        height: 100% !important;
    }
    
    /* Safie High-Contrast Aesthetics */
    .main-message {
        display: block !important;
        color: #ffffff !important;
        font-size: 7.5vw !important;
        text-shadow: 0 2px 15px rgba(0,0,0,0.8), 0 0 10px rgba(0,0,0,0.5) !important;
        margin-bottom: 25px !important;
        line-height: 1.4 !important;
        font-weight: 800 !important;
    }
    .main-message .highlight-blue {
        color: #ffffff !important;
        background: none !important;
        border-bottom: 3px solid #FFCC00 !important; /* Sharp yellow underline */
        padding-bottom: 2px !important;
    }

    .sub-message {
        position: static !important;
        background: none !important;
        color: #ffffff !important;
        font-size: 4.5vw !important;
        width: 100% !important;
        transform: none !important;
        box-shadow: none !important;
        text-shadow: 0 2px 10px rgba(0,0,0,0.8) !important;
        margin: 0 0 30px 0 !important;
        padding: 0 !important;
        font-weight: bold !important;
    }
    .sub-message .hero-highlight {
        color: #FFCC00 !important; /* Safie Yellow */
        font-size: 1.25em !important;
        display: inline-block;
        margin: 0 2px;
    }

    .hero-lead-text {
        color: #ffffff !important;
        font-size: 1.15rem !important;
        font-weight: 800 !important;
        text-shadow: 0 2px 8px rgba(0,0,0,0.8) !important;
        margin-bottom: 25px !important; /* Spaced perfectly above massive CTA */
    }

    /* SAFIE STYLE PILL BUTTONS */
    .hero-actions-wrapper {
        margin-top: auto !important; /* Pushes block heavily to bottom */
    }
    .hero-actions {
        display: flex !important;
        flex-direction: column !important;
        gap: 15px !important;
        align-items: center !important;
    }
    .hero-actions .btn {
        width: 100% !important;
        border-radius: 50px !important; /* Pill shape */
        padding: 22px 20px !important;
        font-size: 1.35rem !important;
        font-weight: 800 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        position: relative !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
        letter-spacing: 0.05em !important;
    }
    .hero-actions .btn-line { /* Overwriting btn-line to yellow for primary Safie emphasis! Wait, web is primary on top, let's reverse semantics for visually perfect mapping. */ }
    
    .hero-actions .btn-web {
        background: #FFCC00 !important;
        color: #000000 !important;
        box-shadow: 0 10px 30px rgba(255, 204, 0, 0.4) !important;
    }
    .hero-actions .btn-line {
        background: #06C755 !important;
        color: #ffffff !important;
    }
    
    /* Safie Right-side arrow > */
    .hero-actions .btn::after {
        content: "〉";
        position: absolute;
        right: 25px;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .hero-actions .btn i {
        display: none !important;
    }
    
    .hero-note { /* Erase old pricing box */
        display: none !important;
    }
}
"""

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()
if 'PHASE 12: SAFIE-STYLE MOBILE HERO OVERHAUL' not in css:
    css += '\n' + css_append
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ CSS Safie Overhaul Appended")
else:
    print("✅ CSS Safie Overhaul already exists")

print("Build Complete.")
