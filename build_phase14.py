import re

file_path = "stretchplus-theme/style.css"
with open(file_path, "r", encoding="utf-8") as f:
    css = f.read()

# 1. Modify the overlay gradient to a premium blueish tint
css = css.replace(
    'background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%) !important;',
    'background: linear-gradient(180deg, rgba(15,35,55,0.3) 0%, rgba(10,25,45,0.85) 100%) !important; /* Premium Blue Tint */'
)

# 2. Hide .main-message entirely on mobile
if '.main-message {\n        display: block !important;' in css:
    css = css.replace(
        '.main-message {\n        display: block !important;\n        color: #ffffff !important;\n        font-size: 7.5vw !important;\n        text-shadow: 0 2px 15px rgba(0,0,0,0.8), 0 0 10px rgba(0,0,0,0.5) !important;\n        margin-bottom: 25px !important;\n        line-height: 1.4 !important;\n        font-weight: 800 !important;\n    }',
        '.main-message {\n        display: none !important; /* Removed as per user request */\n    }'
    )

# 3. Promote .sub-message to be the primary hero typography
if '.sub-message {\n        position: static !important;' in css:
    css = re.sub(
        r'\.sub-message \{.*?\}',
        '.sub-message {\n        position: static !important;\n        background: none !important;\n        color: #ffffff !important;\n        font-size: 6.5vw !important; /* Promoted size */\n        width: 100% !important;\n        transform: none !important;\n        box-shadow: none !important;\n        text-shadow: 0 2px 15px rgba(0,0,0,0.9), 0 0 10px rgba(0,0,0,0.6) !important;\n        margin: 0 0 35px 0 !important;\n        padding: 0 !important;\n        font-weight: 800 !important;\n        line-height: 1.5 !important;\n    }',
        css,
        flags=re.DOTALL
    )

with open(file_path, "w", encoding="utf-8") as f:
    f.write(css)

print("✅ Phase 14 Typography and Tint Override Applied")
