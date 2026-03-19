import re

file_path = "stretchplus-theme/style.css"
with open(file_path, "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace(
    'background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%) !important;',
    'background: linear-gradient(180deg, rgba(15,35,55,0.3) 0%, rgba(10,25,45,0.85) 100%) !important;'
)

css = css.replace(
    '.main-message {\n        display: block !important;\n        color: #ffffff !important;\n        font-size: 7.5vw !important;\n        text-shadow: 0 2px 15px rgba(0,0,0,0.8), 0 0 10px rgba(0,0,0,0.5) !important;\n        margin-bottom: 25px !important;\n        line-height: 1.4 !important;\n        font-weight: 800 !important;\n    }',
    '.main-message {\n        display: none !important;\n    }'
)

phase_12_start = css.find('PHASE 12: SAFIE-STYLE MOBILE HERO OVERHAUL')
if phase_12_start != -1:
    before = css[:phase_12_start]
    after = css[phase_12_start:]
    
    after = re.sub(
        r'\.sub-message \{.*?\}',
        '.sub-message {\n        position: static !important;\n        background: none !important;\n        color: #ffffff !important;\n        font-size: 6.5vw !important;\n        width: 100% !important;\n        transform: none !important;\n        box-shadow: none !important;\n        text-shadow: 0 2px 15px rgba(0,0,0,0.9), 0 0 10px rgba(0,0,0,0.6) !important;\n        margin: 0 0 35px 0 !important;\n        padding: 0 !important;\n        font-weight: 800 !important;\n        line-height: 1.5 !important;\n    }',
        after,
        count=1,
        flags=re.DOTALL
    )
    css = before + after

with open(file_path, "w", encoding="utf-8") as f:
    f.write(css)
print("✅ Safe Phase 14 Applied (Restored PC Integrity)")
