import re

css_patch = """
.bg-blue {
    background-color: #eaf5fa; /* light blue */
}

.flow-triangle-down-blue {
    position: absolute;
    bottom: -30px;
    left: 50%;
    transform: translateX(-50%);
    width: 0; 
    height: 0; 
    border-left: 40px solid transparent;
    border-right: 40px solid transparent;
    border-top: 30px solid #eaf5fa;
    z-index: 10;
}

/* ==========================================================================
   Bottom Stick CTA / Google Map Btn
   ========================================================================== */
.bottom-cta-banner {
    background-image: linear-gradient(rgba(95, 180, 212, 0.8), rgba(95, 180, 212, 0.85)), url('./images/cta_bg.png');
    background-size: cover;
    background-position: center;
    background-attachment: scroll;
    padding: 80px 20px;
    text-align: center;
    color: #fff;
    font-family: 'Noto Sans JP', sans-serif;
}
.bottom-cta-banner h3 {
    margin-bottom: 30px;
    font-size: clamp(1.5rem, 4vw, 2.2rem);
    font-weight: bold;
    letter-spacing: 2px;
}
.bottom-cta-banner .btn-web-outline {
    display: inline-block;
    border: 2px solid #fff;
    color: #fff;
    background: transparent;
    padding: 15px 40px;
    font-size: 1.1rem;
    border-radius: 40px;
    text-decoration: none;
    transition: all 0.3s ease;
    min-width: 250px;
}
.bottom-cta-banner .btn-web-outline:hover {
    background: #fff;
    color: var(--primary-color);
}
"""

def process_css(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # Remove old .bg-beige and .flow-triangle-down-beige
    css = re.sub(r'\.bg-beige\s*\{[^}]*\}', '', css)
    css = re.sub(r'\.flow-triangle-down-beige\s*\{[^}]*\}', '', css)
    
    # Remove old .bottom-cta-banner stuff
    css = re.sub(r'\.bottom-cta-banner\s*\{[^}]*\}', '', css)
    css = re.sub(r'\.bottom-cta-banner h3\s*\{[^}]*\}', '', css)
    css = re.sub(r'\.bottom-cta-banner \.btn\s*\{[^}]*\}', '', css)
    css = re.sub(r'\.bottom-cta-banner \.btn:hover\s*\{[^}]*\}', '', css)
    
    # Append new CSS
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(css + "\n" + css_patch)
    print("Updated CSS in", filename)

def update_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Need to update the buttons in HTML to use the outline style as requested
    old_buttons = '''            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web pulse-btn" target="_blank" style="padding: 12px 30px;">WEBで予約する <i class="fas fa-arrow-right"></i></a>
                <a href="https://lin.ee/rboKm7N" class="btn btn-line" target="_blank" style="background:#06C755; color:#fff; padding: 12px 30px;"><i class="fab fa-line"></i> LINEで相談する</a>
            </div>'''
            
    new_buttons = '''            <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
                <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn-web-outline" target="_blank"><i class="far fa-file-alt"></i> WEBで予約する</a>
                <a href="https://lin.ee/rboKm7N" class="btn-web-outline" target="_blank"><i class="fab fa-line"></i> LINEで相談する</a>
            </div>'''
            
    html = html.replace(old_buttons, new_buttons)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated CTA HTML buttons in", filename)

process_css('style.css')
process_css('redesign/style.css')
update_html('index.html')
update_html('redesign/index.html')
