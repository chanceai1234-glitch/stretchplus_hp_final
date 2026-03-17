import json
import os
import shutil
import re

print("Starting Image Consolidation...")

BASE_DIR = "/Users/ai_stretch/Desktop/stretchplus HPremake final"
IMAGE_SRC_DIR = os.path.join(BASE_DIR, "images")
IMAGE_FINAL_DIR = os.path.join(BASE_DIR, "image_final")

# Create image_final directory if not exists
os.makedirs(IMAGE_FINAL_DIR, exist_ok=True)

# Define the mapping: (original_path, new_filename)
MAPPING = {
    # Logos and Global icons
    "./images/stretchplus_logo.png": "common_logo.png",
    "./images/qr_code.png": "common_qr_line.png",
    "./images/icon_instagram.svg": "icon_instagram.svg",
    "./images/icon_x.svg": "icon_x.svg",
    "./images/checklist_icon.svg": "common_checklist_icon.svg",
    "../images/checklist_icon.svg": "common_checklist_icon.svg", # for redesign CSS
    "./images/cta_bg.png": "cta_background.png",

    # Hero
    "./images/hero-new.jpg": "hero_main.jpg",
    "./images/hero_private_room.png": "hero_secondary.png", # Reused below too

    # About
    "./images/about_intro.jpg": "about_main.jpg",
    "./images/母艦HP/なぜパーソナルなのか.jpg": "about_sub_1.jpg",
    "./images/母艦HP/マッサージとストレッチの違い.jpg": "about_sub_2.jpg",

    # Worries
    "./images/persona_right.jpg": "worries_persona_1.jpg",
    "./images/persona_middle.jpg": "worries_persona_2.jpg",
    "./images/persona_left.jpg": "worries_persona_3.jpg",

    # Amenities (Using exact names mapping them for easier manual overrides)
    "./images/hero_private_room.png": "amenities_card_1.png",
    "./images/clinic_room_bed.jpg": "amenities_card_2.jpg",
    "./images/about_intro.jpg": "amenities_card_3.jpg",
    # (since the original HTML references same src, Python script must replace the N-th occurrence carefully. 
    # Actually, the best way to handle reusing the same source image but mapping to differently named destination 
    # images is to do a regex pass through the raw HTML, tracking occurrences, OR we can just use the exact same 
    # single image map per source. Wait, the user wants 'that section picture'. If I just do a global replace 
    # for the src, they will all point to 'hero_secondary.png' for instance.
    # To satisfy the user perfectly, we need to locate the specific HTML img tags.)
}

HTML_MAPPING_RULES = [
    # (regex_search, replacement_content, source_file_for_copy)
    # Global
    (r'<img src="./images/stretchplus_logo.png"', r'<img src="./image_final/common_logo.png"', "stretchplus_logo.png"),
    (r'<img src="./images/qr_code.png"', r'<img src="./image_final/common_qr_line.png"', "qr_code.png"),
    (r'<img src="./images/icon_instagram.svg"', r'<img src="./image_final/icon_instagram.svg"', "icon_instagram.svg"),
    (r'<img src="./images/icon_x.svg"', r'<img src="./image_final/icon_x.svg"', "icon_x.svg"),

    # Hero
    (r'<img src="./images/hero-new.jpg"', r'<img src="./image_final/hero_main.jpg"', "hero-new.jpg"),

    # About
    (r'<img src="./images/about_intro.jpg" alt="パーソナルストレッチを象徴する画像"', r'<img src="./image_final/about_main.jpg" alt="パーソナルストレッチを象徴する画像"', "about_intro.jpg"),
    (r'<img src="./images/母艦HP/なぜパーソナルなのか.jpg"', r'<img src="./image_final/about_sub_1.jpg"', "母艦HP/なぜパーソナルなのか.jpg"),
    (r'<img src="./images/母艦HP/マッサージとストレッチの違い.jpg"', r'<img src="./image_final/about_sub_2.jpg"', "母艦HP/マッサージとストレッチの違い.jpg"),

    # Worries
    (r'<img src="./images/persona_right.jpg"', r'<img src="./image_final/worries_persona_1.jpg"', "persona_right.jpg"),
    (r'<img src="./images/persona_middle.jpg"', r'<img src="./image_final/worries_persona_2.jpg"', "persona_middle.jpg"),
    (r'<img src="./images/persona_left.jpg"', r'<img src="./image_final/worries_persona_3.jpg"', "persona_left.jpg"),

    # Amenities
    (r'<img src="./images/hero_private_room.png" alt="完全個室"', r'<img src="./image_final/amenities_card_1.png" alt="完全個室"', "hero_private_room.png"),
    (r'<img src="./images/clinic_room_bed.jpg" alt="温熱機能付きベッド"', r'<img src="./image_final/amenities_card_2.jpg" alt="温熱機能付きベッド"', "clinic_room_bed.jpg"),
    (r'<img src="./images/about_intro.jpg" alt="シャワー＆施術着など"', r'<img src="./image_final/amenities_card_3.jpg" alt="シャワー＆施術着など"', "about_intro.jpg"),

    # Flow
    (r'<img src="./images/access_step2.jpg" alt="ご予約"', r'<img src="./image_final/flow_step_1.jpg" alt="ご予約"', "access_step2.jpg"),
    (r'<img src="./images/about_intro.jpg" alt="ご予約時間の5分前を目安にご来店ください"', r'<img src="./image_final/flow_step_2.jpg" alt="ご予約時間の5分前を目安にご来店ください"', "about_intro.jpg"),
    (r'<img src="./images/hero_private_room.png" alt="施術室へご案内、無料の施術着にお着換え！"', r'<img src="./image_final/flow_step_3.png" alt="施術室へご案内、無料の施術着にお着換え！"', "hero_private_room.png"),
    (r'<img src="./images/clinic_room_bed.jpg" alt="施術前のヒアリング"', r'<img src="./image_final/flow_step_4.jpg" alt="施術前のヒアリング"', "clinic_room_bed.jpg"),
    (r'<img src="./images/母艦HP/flow_step3_new.jpg" alt="いざ、パーソナルストレッチ開始！"', r'<img src="./image_final/flow_step_5.jpg" alt="いざ、パーソナルストレッチ開始！"', "母艦HP/flow_step3_new.jpg"),
    (r'<img src="./images/about_intro.jpg" alt="施術後の振り返り"', r'<img src="./image_final/flow_step_6.jpg" alt="施術後の振り返り"', "about_intro.jpg"),
    (r'<img src="./images/hero_private_room.png" alt="お着換え・お会計"', r'<img src="./image_final/flow_step_7.png" alt="お着換え・お会計"', "hero_private_room.png"),

    # Trainers
    (r'<img src="./images/miyasaka.jpg"', r'<img src="./image_final/trainer_1.jpg"', "miyasaka.jpg"),
    (r'<img src="./images/yamamoto.jpg"', r'<img src="./image_final/trainer_2.jpg"', "yamamoto.jpg"),
    (r'<img src="./images/sakuma.jpg"', r'<img src="./image_final/trainer_3.jpg"', "sakuma.jpg"),
    (r'<img src="./images/suzuki.jpg"', r'<img src="./image_final/trainer_4.jpg"', "suzuki.jpg"),

    # Gallery
    (r'<img src="./images/clinic_room_bed.jpg" alt="ストレッチplus 施術室の画像"', r'<img src="./image_final/gallery_slide_1.jpg" alt="ストレッチplus 施術室の画像"', "clinic_room_bed.jpg"),
    (r'<img src="./images/about_intro.jpg" alt="ストレッチplus 待合室の画像"', r'<img src="./image_final/gallery_slide_2.jpg" alt="ストレッチplus 待合室の画像"', "about_intro.jpg"),
    (r'<img src="./images/hero_private_room.png" alt="ストレッチplus シャワー室の画像"', r'<img src="./image_final/gallery_slide_3.png" alt="ストレッチplus シャワー室の画像"', "hero_private_room.png"),

    # Access
    (r'<img src="./images/access_step2.jpg" alt="茅場町駅3番出口"', r'<img src="./image_final/access_step_1.jpg" alt="茅場町駅3番出口"', "access_step2.jpg"),
    (r'<img src="./images/access_step3.jpg" alt="茅場町交差点"', r'<img src="./image_final/access_step_2.jpg" alt="茅場町交差点"', "access_step3.jpg"),
    (r'<img src="./images/access_step1.jpg" alt="V1ビル外観"', r'<img src="./image_final/access_step_3.jpg" alt="V1ビル外観"', "access_step1.jpg")
]

# Specifically handle CSS files natively
CSS_RULES = [
    (r"url\(['\"]?\.\/images\/checklist_icon\.svg['\"]?\)", "url('../image_final/common_checklist_icon.svg')", "checklist_icon.svg"),
    (r"url\(['\"]?\.\.\/images\/checklist_icon\.svg['\"]?\)", "url('../image_final/common_checklist_icon.svg')", "checklist_icon.svg"),
    (r"url\(['\"]?\.\/images\/cta_bg\.png['\"]?\)", "url('../image_final/cta_background.png')", "cta_bg.png"),
    (r"url\(['\"]?\.\.\/images\/cta_bg\.png['\"]?\)", "url('../image_final/cta_background.png')", "cta_bg.png"),
]

# Process target files
targets_html = [
    os.path.join(BASE_DIR, "index.html"),
    os.path.join(BASE_DIR, "redesign/index.html")
]
targets_css = [
    os.path.join(BASE_DIR, "style.css"),
    os.path.join(BASE_DIR, "redesign/style.css")
]

# Apply HTML replacements and copy mapped files
missing_images = []
for html_file in targets_html:
    print(f"Processing HTML: {html_file}")
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for regex_p, rep_str, src_f in HTML_MAPPING_RULES:
        content, count = re.subn(regex_p, rep_str, content)
        if count > 0:
            # Copy source file to final dest
            source_path = os.path.join(IMAGE_SRC_DIR, src_f)
            dest_name = re.search(r'image_final/([^"]+)', rep_str)
            if dest_name:
                dest_name = dest_name.group(1)
                dest_path = os.path.join(IMAGE_FINAL_DIR, dest_name)
                
                if os.path.exists(source_path):
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied {src_f} -> {dest_name}")
                else:
                    if src_f not in missing_images:
                        missing_images.append(source_path)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)


# Process CSS files
for css_file in targets_css:
    print(f"Processing CSS: {css_file}")
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()

    for regex_p, rep_str, src_f in CSS_RULES:
        content, count = re.subn(regex_p, rep_str, content)
        if count > 0:
            source_path = os.path.join(IMAGE_SRC_DIR, src_f)
            dest_name = re.search(r'image_final/([^)]+)', rep_str)
            if dest_name:
                dest_name = dest_name.group(1).replace("'", "").replace('"', "")
                dest_path = os.path.join(IMAGE_FINAL_DIR, dest_name)

                if os.path.exists(source_path):
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied CSS ref {src_f} -> {dest_name}")

    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Done. Missing images: {missing_images}")

