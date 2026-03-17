import os

html_old = '<p class="sub-message">茅場町徒歩1分<br>あなたのための完全個室で<br>極上の施術体験を</p>'
html_new = '<p class="sub-message">茅場町徒歩<span class="hero-highlight">1</span>分<br>あなたのための<span class="hero-highlight">完全個室</span>で極上の施術体験を</p>'

css_addition = """
/* Hero sub-message highlight */
.hero-highlight {
    color: var(--primary-color);
    font-size: 1.25em;
    font-weight: bold;
}
"""

def update_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if html_old in content:
        content = content.replace(html_old, html_new)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find exact HTML in {filename}")

def update_css(filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("\n" + css_addition)
    print(f"Updated {filename}")

update_html('index.html')
update_html('redesign/index.html')
update_css('style.css')
update_css('redesign/style.css')
