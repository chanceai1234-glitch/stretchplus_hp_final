import re
import os

files = [
    '/Users/ai_stretch/Desktop/stretchplus HPremake final/index.html',
    '/Users/ai_stretch/Desktop/stretchplus HPremake final/redesign/index.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the menu row block completely
    # The menu row block looks like:
    # <div class="review-detail-row">
    #     <div class="review-detail-label">メニュー</div>
    #     <div class="review-detail-value">...</div>
    # </div>
    pattern_menu = r'<div class="review-detail-row">\s*<div class="review-detail-label">メニュー</div>\s*<div class="review-detail-value">.*?</div>\s*</div>\s*'
    content = re.sub(pattern_menu, '', content, flags=re.DOTALL)

    # 2. Rename "お悩み" label to "主なお悩み"
    content = content.replace('<div class="review-detail-label">お悩み</div>', '<div class="review-detail-label">主なお悩み</div>')

    # 3. Rename "お客様の声" heading to "ご感想"
    content = content.replace('<h4 class="feedback-heading">お客様の声</h4>', '<h4 class="feedback-heading">ご感想</h4>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML structure updated successfully!")
