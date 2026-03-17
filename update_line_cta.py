import re

css_addition = """
.bottom-cta-banner .btn-line-outline {
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
.bottom-cta-banner .btn-line-outline:hover {
    background: #fff;
    color: #06C755; /* LINE green */
}
"""

def process_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Change the class of only the LINE link inside the CTA
    # Example snippet: <a href="https://lin.ee/rboKm7N" class="btn-web-outline" target="_blank"><i class="fab fa-line"></i> LINEで相談する</a>
    
    html = html.replace(
        '<a href="https://lin.ee/rboKm7N" class="btn-web-outline" target="_blank"><i class="fab fa-line"></i> LINEで相談する</a>',
        '<a href="https://lin.ee/rboKm7N" class="btn-line-outline" target="_blank"><i class="fab fa-line"></i> LINEで相談する</a>'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated LINE button class in", filename)

def process_css(filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(css_addition)
    print("Appended green hover rules to", filename)

process_html('index.html')
process_html('redesign/index.html')
process_css('style.css')
process_css('redesign/style.css')

