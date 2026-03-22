from PIL import Image
import os

img_path = '/Users/ai_stretch/Downloads/STRETCH_PLUS_logo_tate.png'
out_path = '/Users/ai_stretch/Desktop/stretchplus HPremake final/stretchplus-theme/image_final/favicon.png'

img = Image.open(img_path)
img = img.convert("RGBA")
img = img.resize((512, 512), Image.Resampling.LANCZOS)
img.save(out_path)
print("New favicon created from user upload!")
