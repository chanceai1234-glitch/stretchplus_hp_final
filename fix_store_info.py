import re

html_patch_slideshow = """
                <div class="shop-info-slideshow" id="shopSlideshow">
                    <img src="./images/clinic_room_bed.jpg" alt="ストレッチplus 施術室の画像" class="slide active">
                    <img src="./images/about_intro.jpg" alt="ストレッチplus 待合室の画像" class="slide">
                    <img src="./images/hero_private_room.png" alt="ストレッチplus シャワー室の画像" class="slide">
                </div>
"""

css_patch = """
/* ==========================================================================
   Store Info Refinements
   ========================================================================== */
.shop-table th {
    padding-right: 30px; /* Increased separation between label and value */
    padding-top: 15px;
    padding-bottom: 15px;
    vertical-align: top;
    white-space: nowrap;
}
.shop-table td {
    padding-top: 15px;
    padding-bottom: 15px;
    line-height: 1.6;
}

.shop-address-wrapper {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
}
.shop-address-buttons {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 5px;
}

/* Slideshow styles */
.shop-info-slideshow {
    position: relative;
    width: 100%;
    aspect-ratio: 4/3;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.shop-info-slideshow img.slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0;
    transition: opacity 1s ease-in-out;
}
.shop-info-slideshow img.slide.active {
    opacity: 1;
}
"""

js_patch = """
    // Store Info Slideshow
    const slides = document.querySelectorAll('#shopSlideshow .slide');
    if(slides.length > 0) {
        let currentSlide = 0;
        setInterval(() => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }, 4000); // Change image every 4 seconds
    }
</script>
</body>
"""

def process_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Replace the single image with the slideshow
    old_img_div = """                <div class="shop-info-image">
                    <img src="./images/clinic_room_bed.jpg" alt="ストレッチplus 施術室の画像">
                </div>"""
    
    html = html.replace(old_img_div, html_patch_slideshow)
    
    # Also handle redesign index which might have slightly different formatting
    old_img_div_alt = """                <div class="shop-info-image">
                    <img src="./images/clinic_room_bed.jpg" alt="ストレッチplus 施術室">
                </div>"""
    html = html.replace(old_img_div_alt, html_patch_slideshow)

    # 2. Add Google Maps button and fix grouping
    old_address_html = """                                <div class="shop-address-wrapper">
                                    <span>〒103-0025 東京都中央区日本橋茅場町2-13-14 ブイワンビル2F</span>
                                    <button class="btn-copy-address" onclick="navigator.clipboard.writeText('東京都中央区日本橋茅場町2-13-14 ブイワンビル2F')">住所をコピー</button>
                                </div>"""
    
    new_address_html = """                                <div class="shop-address-wrapper">
                                    <span>〒103-0025 東京都中央区日本橋茅場町2-13-14 ブイワンビル2F</span>
                                    <div class="shop-address-buttons">
                                        <button class="btn-copy-address" onclick="navigator.clipboard.writeText('東京都中央区日本橋茅場町2-13-14 ブイワンビル2F')"><i class="fas fa-copy"></i> 住所をコピー</button>
                                        <a href="https://maps.google.com/?q=東京都中央区日本橋茅場町2-13-14" class="btn-google-map" target="_blank"><i class="fas fa-map-marker-alt"></i> Google Map</a>
                                    </div>
                                </div>"""
    
    html = html.replace(old_address_html, new_address_html)

    # 3. Add JS
    html = html.replace('</script>\n</body>', js_patch)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated HTML logic in", filename)

def process_css(filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(css_patch)
    print("Appended CSS in", filename)

process_html('index.html')
process_html('redesign/index.html')
process_css('style.css')
process_css('redesign/style.css')
