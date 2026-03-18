import os

base_dir = os.path.dirname(os.path.abspath(__file__))
uploader_path = os.path.join(base_dir, "image_uploader.py")

with open(uploader_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("PORT = 8000", "PORT = 8080")

with open(uploader_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Changed port to 8080 in image_uploader.py")
