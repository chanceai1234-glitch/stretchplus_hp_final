import os
import re

files_to_check = [
    'stretchplus-theme/footer.php',
    'stretchplus-theme/header.php',
    'stretchplus-theme/template-parts/section-cta-1.php',
    'stretchplus-theme/template-parts/section-cta-2.php',
    'redesign/index.html',
    'index.html'
]

for f in files_to_check:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 1. Clean up inline styles first
        content = content.replace('style="background: rgba(255,255,255,0.1);"', '')
        
        # 2. Replace classes in CTA banners
        content = content.replace('class="btn-web-outline"', 'class="btn btn-web pulse-btn"')
        content = content.replace('class="btn-line-outline"', 'class="btn btn-line pulse-btn"')
        
        content = content.replace('class="btn btn btn-web', 'class="btn btn-web')
        content = content.replace('class="btn btn btn-line', 'class="btn btn-line')

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

# 3. Clean and redefine style.css
css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

new_buttons = """
.btn-web {
    background-color: var(--primary-color);
    color: #fff;
    border: 2px solid var(--primary-color);
}

.btn-web:hover {
    background-color: #fff;
    color: var(--primary-color);
}

.btn-line {
    background-color: var(--line-color);
    color: #fff;
    border: 2px solid var(--line-color);
}

.btn-line:hover {
    background-color: #fff;
    color: var(--line-color);
}
"""

# Completely erase old .btn-web and .btn-line
css = re.sub(r'\.btn-web\s*\{[^}]*\}', '', css)
css = re.sub(r'\.btn-web:hover\s*\{[^}]*\}', '', css)
css = re.sub(r'\.btn-line\s*\{[^}]*\}', '', css)
css = re.sub(r'\.btn-line:hover\s*\{[^}]*\}', '', css)

# Make sure btn-final-web perfectly inverts
css = re.sub(r'\.btn-final-web\s*\{[^}]*\}', """
.btn-final-web {
    background-color: var(--primary-color);
    color: #fff;
    border: 2px solid var(--primary-color);
    font-size: 1.25rem;
    font-weight: bold;
    padding: 20px 50px;
    border-radius: 40px;
    display: inline-block;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}
""", css)

css = re.sub(r'\.btn-final-web:hover\s*\{[^}]*\}', """
.btn-final-web:hover {
    background-color: #fff;
    color: var(--primary-color);
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}
""", css)


# Remove the `.bottom-cta-banner` outline definitions completely to prevent zombie css
css = re.sub(r'\.bottom-cta-banner\s+\.btn-web-outline\s*\{[^}]*\}', '', css)
css = re.sub(r'\.bottom-cta-banner\s+\.btn-web-outline:hover\s*\{[^}]*\}', '', css)
css = re.sub(r'\.bottom-cta-banner\s+\.btn-line-outline\s*\{[^}]*\}', '', css)
css = re.sub(r'\.bottom-cta-banner\s+\.btn-line-outline:hover\s*\{[^}]*\}', '', css)

# Inject our exact new base buttons at the top of the Buttons section
target_comment = '/* ==========================================================================\n   Buttons'
if target_comment in css:
    css = css.replace(target_comment, target_comment + new_buttons)
else:
    css += new_buttons

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("Unified CTA buttons globally.")
