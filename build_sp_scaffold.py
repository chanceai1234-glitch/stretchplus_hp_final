import os
import re

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Global CSS setup
new_sp_css = """
/* ==========================================================================
   SMARTPHONE GLOBAL UI OVERRIDES & FIXES
   ========================================================================== */
html, body {
    overflow-x: hidden; /* Fix horizontal shake */
    width: 100%;
    max-width: 100vw;
    position: relative;
}

@media (max-width: 768px) {
    /* Hide specific PC elements */
    .header-cta, .bottom-cta-banner {
        display: none !important;
    }
    
    /* Shrink the logo */
    .logo-container img {
        max-width: 160px; /* Reduced from default to prevent reaching halfway */
    }

    /* Padding under body for the fixed footer */
    body {
        padding-bottom: 70px; /* Space for sticky CTA */
    }

    /* Sticky Bottom CTA */
    .sp-sticky-cta {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        display: flex;
        z-index: 9999;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        background: #fff;
    }
    
    .sp-sticky-cta .btn {
        flex: 1;
        border-radius: 0;
        padding: 16px 0;
        font-size: 1.1rem;
        font-weight: bold;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #fff;
        text-decoration: none;
        border: none;
    }
    
    .sp-sticky-cta .btn-line {
        background-color: var(--line-color);
        border-right: 1px solid rgba(255,255,255,0.2);
    }
    
    .sp-sticky-cta .btn-web {
        background-color: var(--primary-color);
    }

    /* Hamburger Menu Button */
    .sp-hamburger {
        display: block;
        background: transparent;
        border: none;
        cursor: pointer;
        padding: 10px;
        z-index: 10001; /* Above the overlay */
        position: relative;
    }
    
    .sp-hamburger span {
        display: block;
        width: 25px;
        height: 2px;
        background-color: #333;
        margin: 5px 0;
        transition: all 0.3s ease;
    }

    /* Hamburger Menu Animation */
    .sp-hamburger.is-active span:nth-child(1) {
        transform: translateY(7px) rotate(45deg);
    }
    .sp-hamburger.is-active span:nth-child(2) {
        opacity: 0;
    }
    .sp-hamburger.is-active span:nth-child(3) {
        transform: translateY(-7px) rotate(-45deg);
    }

    /* Fullscreen Menu Overlay */
    .sp-nav-menu {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        background: rgba(255, 255, 255, 0.98);
        z-index: 10000;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transform: translateY(-100%);
        transition: transform 0.4s ease-in-out;
    }
    
    .sp-nav-menu.is-active {
        transform: translateY(0);
    }
    
    .sp-nav-menu ul {
        list-style: none;
        padding: 0;
        margin: 0;
        text-align: center;
    }
    
    .sp-nav-menu ul li {
        margin: 20px 0;
    }
    
    .sp-nav-menu ul a {
        font-size: 1.25rem;
        font-weight: bold;
        color: #333;
        text-decoration: none;
    }
}

/* Ensure hamburger hides on PC */
@media (min-width: 769px) {
    .sp-hamburger, .sp-nav-menu, .sp-sticky-cta {
        display: none !important;
    }
}
"""

if 'SMARTPHONE GLOBAL UI OVERRIDES' not in css:
    css += '\n' + new_sp_css
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Modify specific files for DOM
def process_html_file(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # --- HEADER MODS ---
    hamburger_html = """            <!-- Header CTA (Hidden on Mobile via CSS) -->
            <div class="header-cta">
                <a href="https://lin.ee/rboKm7N" class="btn btn-line" target="_blank"><i class="fab fa-line"></i> LINEで相談する</a>
                <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web" target="_blank"><i class="far fa-file-alt"></i> WEBで予約する</a>
            </div>
            
            <!-- Mobile Hamburger Button -->
            <button class="sp-hamburger" aria-label="メニュー">
                <span></span>
                <span></span>
                <span></span>
            </button>
            
            <!-- Mobile Navigation Overlay -->
            <nav class="sp-nav-menu">
                <ul>
                    <li><a href="#about" class="sp-nav-link">パーソナルストレッチとは</a></li>
                    <li><a href="#worries" class="sp-nav-link">お悩み解決</a></li>
                    <li><a href="#flow" class="sp-nav-link">ご利用の流れ</a></li>
                    <li><a href="#amenities" class="sp-nav-link">設備・アメニティ</a></li>
                    <li><a href="#trainers" class="sp-nav-link">トレーナー紹介</a></li>
                    <li><a href="#reviews" class="sp-nav-link">口コミ</a></li>
                    <li><a href="#faq" class="sp-nav-link">よくあるご質問</a></li>
                    <li><a href="#access" class="sp-nav-link">店舗情報・アクセス</a></li>
                </ul>
            </nav>"""
            
    if '<!-- Mobile Hamburger Button -->' not in content:
        # We need to replace the old header-cta block
        old_cta_block = re.search(r'<!-- Header CTA -->\s*<div class="header-cta">.*?</div>', content, re.DOTALL)
        if old_cta_block:
            content = content.replace(old_cta_block.group(0), hamburger_html)

    # --- FOOTER MODS (Sticky CTA and JS) ---
    sticky_cta_html = """
    <!-- Mobile Sticky Footer CTA -->
    <div class="sp-sticky-cta">
        <a href="https://lin.ee/rboKm7N" class="btn btn-line" target="_blank"><i class="fab fa-line" style="margin-right: 8px;"></i> LINE</a>
        <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web" target="_blank"><i class="far fa-file-alt" style="margin-right: 8px;"></i> WEB予約</a>
    </div>
    """
    
    if '<div class="sp-sticky-cta">' not in content:
        # Inject right before closing </body>
        content = content.replace('</body>', sticky_cta_html + '\n</body>')

    js_logic = """
        // Mobile Hamburger Logic
        const hamburger = document.querySelector('.sp-hamburger');
        const spMenu = document.querySelector('.sp-nav-menu');
        const spNavLinks = document.querySelectorAll('.sp-nav-link');
        
        if(hamburger && spMenu) {
            hamburger.addEventListener('click', () => {
                hamburger.classList.toggle('is-active');
                spMenu.classList.toggle('is-active');
                document.body.style.overflow = spMenu.classList.contains('is-active') ? 'hidden' : '';
            });
            
            // Close menu when clicking a link
            spNavLinks.forEach(link => {
                link.addEventListener('click', () => {
                    hamburger.classList.remove('is-active');
                    spMenu.classList.remove('is-active');
                    document.body.style.overflow = '';
                });
            });
        }
    """
    
    if '// Mobile Hamburger Logic' not in content:
        # Inject in existing script block or before </body>
        script_tag_end = content.rfind('</script>')
        if script_tag_end != -1:
            content = content[:script_tag_end] + js_logic + content[script_tag_end:]
        else:
            # Fallback if no script tag exists at bottom
            content = content.replace('</body>', f'\n<script>{js_logic}</script>\n</body>')
            
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

process_html_file('stretchplus-theme/header.php')
process_html_file('stretchplus-theme/footer.php') 
# Since header/footer are combined in index files, we process it as a whole
process_html_file('index.html')
process_html_file('redesign/index.html')

print("Applied Sp Scaffolding")
