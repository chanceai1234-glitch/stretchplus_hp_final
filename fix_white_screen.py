import re

file_path = "stretchplus-theme/style.css"
with open(file_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace the fragile Phase 13 height calc with the bulletproof Phase 12 vh
css = re.sub(
    r'height: calc\(100vh - 60px\) !important;',
    r'height: 85vh !important;',
    css
)

# Replace the base opacity: 0 on .sp-slide with a dark background fallback on the wrapper
if '.sp-hero-slideshow {' in css:
    css = css.replace(
        '.sp-hero-slideshow {\n        position: absolute !important;',
        '.sp-hero-slideshow {\n        position: absolute !important;\n        background-color: #111111 !important; /* Fallback for Safari */'
    )

# Ensure sp-slide starts with visibility
css = css.replace(
    'opacity: 0;\n        animation: spFadeInOut 12s infinite;',
    'opacity: 0;\n        -webkit-animation: spFadeInOut 12s infinite;\n        animation: spFadeInOut 12s infinite;\n        will-change: opacity;'
)

# Ensure overlay works
css = css.replace(
    'z-index: 2 !important;\n        opacity: 1 !important;',
    'z-index: 2 !important;\n        opacity: 1 !important;\n        pointer-events: none !important;'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(css)

print("✅ Hotpatch applied to style.css")
