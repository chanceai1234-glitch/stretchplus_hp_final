import sys

def fix_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix centering
    html = html.replace(
        '<div class="container" style="max-width: 900px; text-align: center; margin-bottom: 30px;">',
        '<div class="container" style="max-width: 900px; text-align: center; margin: 0 auto 30px;">'
    )
    
    # Change badge class to blue
    html = html.replace('step-badge-orange', 'step-badge-blue')
    
    # If the amenities section is being hidden by the reveal animation, let's remove it to test
    html = html.replace(
        '<section id="amenities" class="reveal section-bg-light" style="padding: 60px 0;">',
        '<section id="amenities" class="section-bg-light" style="padding: 60px 0;">'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed {filename}")

fix_html('index.html')
fix_html('redesign/index.html')
