import os

for f in ['redesign/index.html', 'redesign/style.css']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('./image_final/', '../image_final/')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
