from PIL import Image
import os

img_path = '/Users/ai_stretch/.gemini/antigravity/brain/5b227e4a-2e93-4b73-b436-af64a60dd58c/media__1773736600014.jpg'
out_dir = '/Users/ai_stretch/Desktop/stretchplus HPremake final/images'

# The image is 1024x199. There are 4 distinct figures horizontally.
# Each block is approximately 256px wide.
# 1st: Salaryman (0 - 256)
# 2nd: Empty suit (256 - 512) -> Skip
# 3rd: Housewife (512 - 768)
# 4th: Golfer (768 - 1024)

img = Image.open(img_path)

# Crop coordinates: (left, upper, right, lower)
salaryman = img.crop((0, 0, 256, 199))
housewife = img.crop((512, 0, 768, 199))
golfer = img.crop((768, 0, 1024, 199))

salaryman.save(os.path.join(out_dir, 'persona_salaryman.png'))
housewife.save(os.path.join(out_dir, 'persona_housewife.png'))
golfer.save(os.path.join(out_dir, 'persona_golfer.png'))

print("Cropped and saved 3 persona images.")
