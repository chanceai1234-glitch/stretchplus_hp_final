import re

with open('redesign/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract Header
header_end = html.find('</header>') + len('</header>')
header_content = html[:header_end]
header_content = header_content.replace('</head>', '    <?php wp_head(); ?>\n</head>')
header_content = header_content.replace('<body>', '<body <?php body_class(); ?>>\n    <?php wp_body_open(); ?>')
header_content = header_content.replace('../image_final/', '<?php echo get_template_directory_uri(); ?>/image_final/')

with open('stretchplus-theme/header.php', 'w', encoding='utf-8') as f:
    f.write(header_content)

# Extract Footer
footer_start = html.find('<!-- Pre-Footer CTA -->')
if footer_start == -1:
    footer_start = html.find('<footer id="footer">')

footer_content = html[footer_start:]
footer_content = footer_content.replace('</body>', '<?php wp_footer(); ?>\n</body>')
footer_content = footer_content.replace('../image_final/', '<?php echo get_template_directory_uri(); ?>/image_final/')

with open('stretchplus-theme/footer.php', 'w', encoding='utf-8') as f:
    f.write(footer_content)

# Extract Middle Content
body_content = html[header_end:footer_start]

# Regex to safely extract top-level <section> tags
sections = []
pos = 0
while True:
    start = body_content.find('<section', pos)
    if start == -1:
        break
    # Find matching </section>
    end = body_content.find('</section>', start)
    if end == -1:
        break
    end += len('</section>')
    sec_html = body_content[start:end]
    sections.append(sec_html)
    pos = end

front_page = "<?php\n/**\n * Template Name: Front Page\n */\nget_header();\n?>\n\n<main id=\"primary\" class=\"site-main\">\n"

import os
os.makedirs('stretchplus-theme/template-parts', exist_ok=True)

for sec in sections:
    match = re.search(r'id="([^"]+)"', sec)
    if match:
        sec_id = match.group(1)
        # If there is a cta section, there might be multiple CTAs. 
        # In this template, there was <section class="cta-banner"> without an ID.
        pass
    else:
        # Search for class
        class_match = re.search(r'class="([^"]+)"', sec)
        if class_match:
            sec_id = class_match.group(1).split()[0] # get first class
        else:
            sec_id = "section"

    # Replace image paths
    sec = sec.replace('../image_final/', '<?php echo get_template_directory_uri(); ?>/image_final/')
    
    # Save template part
    part_name = f"section-{sec_id}.php"
    with open(f"stretchplus-theme/template-parts/{part_name}", 'w', encoding='utf-8') as f:
        f.write(sec)
        
    front_page += f"    <?php get_template_part('template-parts/section', '{sec_id}'); ?>\n"

front_page += "</main>\n\n<?php\nget_footer();\n"

with open('stretchplus-theme/front-page.php', 'w', encoding='utf-8') as f:
    f.write(front_page)

print("Slicing complete. All template parts generated.")
