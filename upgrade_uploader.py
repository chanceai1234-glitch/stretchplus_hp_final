import os
import shutil

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'image_final')
WP_DIR = os.path.join(BASE_DIR, 'stretchplus-theme', 'image_final')

# Create missing physical placeholders so the Dropdown can find them
missing_files = [
    ('amenities_card_3.jpg', 'amenities_card_4.jpg'),
    ('amenities_card_3.jpg', 'amenities_card_5.jpg'),
    ('flow_step_7.png', 'flow_step_8.jpg'),
    ('flow_step_7.png', 'flow_step_9.jpg')
]

for src, dst in missing_files:
    # Static copy
    src_static = os.path.join(STATIC_DIR, src)
    dst_static = os.path.join(STATIC_DIR, dst)
    if os.path.exists(src_static) and not os.path.exists(dst_static):
        shutil.copy2(src_static, dst_static)
        
    # WP copy
    src_wp = os.path.join(WP_DIR, src)
    dst_wp = os.path.join(WP_DIR, dst)
    if os.path.exists(src_wp) and not os.path.exists(dst_wp):
        shutil.copy2(src_wp, dst_wp)

print("Generated missing placeholders for dropdown UI.")

# Upgrade image_uploader.py to dual dual-sync uploads
uploader_path = os.path.join(BASE_DIR, 'image_uploader.py')
with open(uploader_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add WP_IMAGE_FINAL_DIR variable
if 'WP_IMAGE_FINAL_DIR' not in content:
    content = content.replace(
        'IMAGE_FINAL_DIR = os.path.join(BASE_DIR, "image_final")',
        'IMAGE_FINAL_DIR = os.path.join(BASE_DIR, "image_final")\nWP_IMAGE_FINAL_DIR = os.path.join(BASE_DIR, "stretchplus-theme", "image_final")'
    )

    # Modify the upload loop
    old_upload_block = """                # Write file
                with open(filepath, 'wb') as f:
                    f.write(base64.b64decode(base64_data))"""
                    
    new_upload_block = """                # Write file to original static root
                decoded_data = base64.b64decode(base64_data)
                with open(filepath, 'wb') as f:
                    f.write(decoded_data)
                
                # Mirror to WordPress theme
                if os.path.exists(WP_IMAGE_FINAL_DIR):
                    wp_filepath = os.path.join(WP_IMAGE_FINAL_DIR, filename)
                    with open(wp_filepath, 'wb') as wp_f:
                        wp_f.write(decoded_data)"""
    
    content = content.replace(old_upload_block, new_upload_block)
    
    with open(uploader_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Upgraded image_uploader.py to support WP theme synchronization.")
