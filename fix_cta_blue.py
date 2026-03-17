import re

def process_css(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        css = f.read()

    # Change navy (26, 54, 93) to standard blue (0, 102, 204)
    old_bg = "background-image: linear-gradient(rgba(26, 54, 93, 0.85), rgba(26, 54, 93, 0.9)), url('./images/cta_bg.png');"
    new_bg = "background-image: linear-gradient(rgba(0, 102, 204, 0.85), rgba(0, 102, 204, 0.9)), url('./images/cta_bg.png');"
    
    if old_bg in css:
        css = css.replace(old_bg, new_bg)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(css)
        print("Updated CSS to Standard Blue in", filename)
    else:
        print("Could not find the navy background in", filename)

process_css('style.css')
process_css('redesign/style.css')
