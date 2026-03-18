import os
import re

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Revert btn-web and btn-line to be Solid -> White
css = re.sub(r'\.btn-web\s*\{\s*background-color\s*:\s*#fff;\s*color\s*:\s*var\(--primary-color\);\s*border\s*:\s*2px solid var\(--primary-color\);\s*\}',
""".btn-web {
    background-color: var(--primary-color);
    color: #fff;
    border: 2px solid var(--primary-color);
}""", css)

css = re.sub(r'\.btn-web:hover\s*\{\s*background-color\s*:\s*var\(--primary-color\);\s*color\s*:\s*#fff;\s*\}',
""".btn-web:hover {
    background-color: #fff;
    color: var(--primary-color);
}""", css)

# btn-line
css = re.sub(r'\.btn-line\s*\{\s*background-color\s*:\s*#fff;\s*color\s*:\s*var\(--line-color\);\s*border\s*:\s*2px solid var\(--line-color\);\s*\}',
""".btn-line {
    background-color: var(--line-color);
    color: #fff;
    border: 2px solid var(--line-color);
}""", css)

css = re.sub(r'\.btn-line:hover\s*\{\s*background-color\s*:\s*var\(--line-color\);\s*color\s*:\s*#fff;\s*\}',
""".btn-line:hover {
    background-color: #fff;
    color: var(--line-color);
}""", css)

# 2. Add btn-web-outline and btn-line-outline to style.css for the bottom Banners
new_outlines = """

.btn-web-outline {
    background-color: #fff;
    color: var(--primary-color);
    border: 2px solid var(--primary-color);
    font-size: 1.15rem;
    font-weight: bold;
    padding: 18px 40px;
    border-radius: 40px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    text-decoration: none;
    transition: all 0.3s ease;
}
.btn-web-outline:hover {
    background-color: var(--primary-color);
    color: #fff;
    box-shadow: 0 4px 12px rgba(35, 173, 198, 0.3);
}

.btn-line-outline {
    background-color: #fff;
    color: var(--line-color);
    border: 2px solid var(--line-color);
    font-size: 1.15rem;
    font-weight: bold;
    padding: 18px 40px;
    border-radius: 40px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    text-decoration: none;
    transition: all 0.3s ease;
}
.btn-line-outline:hover {
    background-color: var(--line-color);
    color: #fff;
    box-shadow: 0 4px 12px rgba(6, 199, 85, 0.3);
}
"""

if '.btn-web-outline {' not in css:
    css += new_outlines

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Swap the CTA banners back to utilizing the newly created pure outline instances
cta_files = [
    'stretchplus-theme/footer.php',
    'stretchplus-theme/template-parts/section-cta-1.php',
    'stretchplus-theme/template-parts/section-cta-2.php',
    'index.html',
    'redesign/index.html'
]

for f in cta_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
        
        html = html.replace('class="btn btn-web pulse-btn"', 'class="btn-web-outline pulse-btn"')
        html = html.replace('class="btn btn-line pulse-btn"', 'class="btn-line-outline pulse-btn"')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)

print("Restored Solid Header/Hero CTA behavior successfully.")
