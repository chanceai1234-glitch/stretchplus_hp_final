import os
import re

# 1. CSS Modifications
css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

css_fixes = """
    /* PHASE 8: HEADER & FOOTER REFINEMENTS */
    .header-actions {
        display: none !important; /* Hide old PC header buttons */
    }
    
    .sp-sticky-cta {
        height: 65px !important;
        align-items: stretch !important;
    }
    .sp-sticky-cta .btn {
        height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        box-sizing: border-box !important;
        border-radius: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .sp-sticky-cta .btn-web {
        border-right: 1px solid rgba(255,255,255,0.3) !important;
    }
    .sp-sticky-cta .btn-line {
        border-right: none !important;
        border-left: none !important;
    }
    
    .footer-nav {
        display: none !important; /* Collapse redundant footer links on mobile */
    }
    
    .hero-actions-wrapper {
        display: none !important; /* Remove "First time try" block and buttons natively inside hero on mobile */
    }
"""

if 'PHASE 8: HEADER & FOOTER REFINEMENTS' not in css:
    hook = '/* HERO FIXES */'
    css = css.replace(hook, css_fixes + '\n    ' + hook)
    
    # Also fix the previous typo: .header-cta -> .header-actions in the old block is now redundant, but fine.
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. HTML Modifications
hamburger_html = """</div>
        
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

def process_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Inject Hamburger
    if 'class="sp-hamburger"' not in content:
        # Replace the closing div of header-actions
        content = re.sub(r'<div class="header-actions">.*?</div>', r'\g<0>' + '\n' + hamburger_html[6:], content, flags=re.DOTALL)
        
    # Swap Sticky Footer Buttons (Web Left, Line Right)
    old_sticky = """<div class="sp-sticky-cta">
        <a href="https://lin.ee/rboKm7N" class="btn btn-line" target="_blank"><i class="fab fa-line" style="margin-right: 8px;"></i> LINE</a>
        <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web" target="_blank"><i class="far fa-file-alt" style="margin-right: 8px;"></i> WEB予約</a>
    </div>"""
    
    new_sticky = """<div class="sp-sticky-cta">
        <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web" target="_blank"><i class="far fa-file-alt" style="margin-right: 8px;"></i> WEB予約</a>
        <a href="https://lin.ee/rboKm7N" class="btn btn-line" target="_blank"><i class="fab fa-line" style="margin-right: 8px;"></i> LINE相談</a>
    </div>"""
    
    content = content.replace(old_sticky, new_sticky)
    
    # Catch any variations of old sticky
    content = re.sub(
        r'<div class="sp-sticky-cta">\s*<a href="https://lin.ee/rboKm7N".*?</a>\s*<a href="https://yui.kanzashi.*?</a>\s*</div>',
        new_sticky,
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

process_file('stretchplus-theme/header.php')
process_file('stretchplus-theme/footer.php')
process_file('index.html')
process_file('redesign/index.html')

print("Phase 8 Step 1 Complete.")
