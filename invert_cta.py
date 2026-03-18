import os
import re

css_file = 'stretchplus-theme/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .btn-web
css = re.sub(r'\.btn-web\s*\{\s*background-color\s*:\s*var\(--primary-color\);\s*color\s*:\s*#fff;\s*border\s*:\s*2px solid var\(--primary-color\);\s*\}',
""".btn-web {
    background-color: #fff;
    color: var(--primary-color);
    border: 2px solid var(--primary-color);
}""", css)

css = re.sub(r'\.btn-web:hover\s*\{\s*background-color\s*:\s*#fff;\s*color\s*:\s*var\(--primary-color\);\s*\}',
""".btn-web:hover {
    background-color: var(--primary-color);
    color: #fff;
}""", css)


# Replace .btn-line
css = re.sub(r'\.btn-line\s*\{\s*background-color\s*:\s*var\(--line-color\);\s*color\s*:\s*#fff;\s*border\s*:\s*2px solid var\(--line-color\);\s*\}',
""".btn-line {
    background-color: #fff;
    color: var(--line-color);
    border: 2px solid var(--line-color);
}""", css)

css = re.sub(r'\.btn-line:hover\s*\{\s*background-color\s*:\s*#fff;\s*color\s*:\s*var\(--line-color\);\s*\}',
""".btn-line:hover {
    background-color: var(--line-color);
    color: #fff;
}""", css)


# Replace .btn-final-web
css = re.sub(r'\.btn-final-web\s*\{[^}]*\}',
""".btn-final-web {
    background-color: #fff;
    color: var(--primary-color);
    border: 2px solid var(--primary-color);
    font-size: 1.25rem;
    font-weight: bold;
    padding: 20px 50px;
    border-radius: 40px;
    display: inline-block;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}""", css)

css = re.sub(r'\.btn-final-web:hover\s*\{[^}]*\}',
""".btn-final-web:hover {
    background-color: var(--primary-color);
    color: #fff;
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}""", css)


# Replace .btn-booking-outline
css = re.sub(r'\.btn-booking-outline\s*\{[^}]*\}',
""".btn-booking-outline {
    background-color: #fff;
    border: 2px solid var(--primary-color);
    color: var(--primary-color);
    font-weight: bold;
}""", css)

css = re.sub(r'\.btn-booking-outline:hover\s*\{[^}]*\}',
""".btn-booking-outline:hover {
    background-color: var(--primary-color);
    color: #fff;
}""", css)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("Inverted CTA button colors successfully.")
