header = """/*
Theme Name: STRETCH+ Final
Theme URI: https://stretch-plus.com
Author: AILABO Group
Description: A custom premium theme for STRETCH+ 茅場町.
Version: 1.0.0
Text Domain: stretchplus
*/
"""
with open('redesign/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace any ../image_final/ with standard PHP dynamic paths? Wait, CSS is loaded from the theme root!
# So images in style.css should just point to ./image_final/! 
# In redesign/style.css, it was pointing to ../image_final/ -- we must change it to ./image_final/ for the WP theme's style.css.
css = css.replace('../image_final/', './image_final/')

with open('stretchplus-theme/style.css', 'w', encoding='utf-8') as f:
    f.write(header + css)
