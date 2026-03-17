import re

css_addition = """
/* Update Address Wrapper Layout */
.shop-address-wrapper {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
}
.shop-address-line1 {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}
.shop-address-line2 {
    margin-top: 5px;
}

/* Copy Icon Button */
.btn-copy-icon {
    background: transparent;
    border: 1px solid #ccc;
    color: #555;
    width: 32px;
    height: 32px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.1rem;
    transition: all 0.2s ease;
    padding: 0;
}
.btn-copy-icon:hover {
    background: #f0f0f0;
    color: var(--primary-color);
    border-color: var(--primary-color);
}
.btn-copy-icon:active {
    transform: scale(0.95);
}
"""

def update_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    old_html = """                                <div class="shop-address-wrapper">
                                    <span>〒103-0025 東京都中央区日本橋茅場町2-13-14 ブイワンビル2F</span>
                                    <div class="shop-address-buttons">
                                        <button class="btn-copy-address" onclick="navigator.clipboard.writeText('東京都中央区日本橋茅場町2-13-14 ブイワンビル2F')"><i class="fas fa-copy"></i> 住所をコピー</button>
                                        <a href="https://maps.google.com/?q=東京都中央区日本橋茅場町2-13-14" class="btn-google-map" target="_blank"><i class="fas fa-map-marker-alt"></i> Google Map</a>
                                    </div>
                                </div>"""

    new_html = """                                <div class="shop-address-wrapper">
                                    <div class="shop-address-line1">
                                        <span>〒103-0025 東京都中央区日本橋茅場町2-13-14 ブイワンビル2F</span>
                                        <button class="btn-copy-icon" onclick="navigator.clipboard.writeText('東京都中央区日本橋茅場町2-13-14 ブイワンビル2F')" title="住所をコピー"><i class="far fa-copy"></i></button>
                                    </div>
                                    <div class="shop-address-line2">
                                        <a href="https://maps.google.com/?q=東京都中央区日本橋茅場町2-13-14" class="btn-google-map" target="_blank"><i class="fas fa-map-marker-alt"></i> Google Map</a>
                                    </div>
                                </div>"""

    if old_html in html:
        html = html.replace(old_html, new_html)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated HTML logic in", filename)
    else:
        print("Could not find the target HTML in", filename)

def process_css(filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("\n" + css_addition)
    print("Appended new address CSS to", filename)

update_html('index.html')
update_html('redesign/index.html')
process_css('style.css')
process_css('redesign/style.css')
