from PIL import Image

def make_bg_white(img_path, out_path, tolerance=40):
    img = Image.open(img_path).convert("RGBA")
    data = list(img.getdata())
    
    # Get background color from top-left corner
    bg_color = data[0][:3]
    new_data = []
    
    for item in data:
        if (abs(item[0] - bg_color[0]) <= tolerance and 
            abs(item[1] - bg_color[1]) <= tolerance and 
            abs(item[2] - bg_color[2]) <= tolerance):
            new_data.append((255, 255, 255, 255))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img_out = img.convert("RGB")
    img_out.save(out_path, quality=95)
    print(f"Processed {out_path}")

images = [
    ('/Users/ai_stretch/.gemini/antigravity/brain/5b227e4a-2e93-4b73-b436-af64a60dd58c/media__1773738489297.jpg', 'persona_left.jpg'),
    ('/Users/ai_stretch/.gemini/antigravity/brain/5b227e4a-2e93-4b73-b436-af64a60dd58c/media__1773738494637.jpg', 'persona_middle.jpg'),
    ('/Users/ai_stretch/.gemini/antigravity/brain/5b227e4a-2e93-4b73-b436-af64a60dd58c/media__1773738503787.jpg', 'persona_right.jpg')
]

for in_path, out_name in images:
    out_path = f"/Users/ai_stretch/Desktop/stretchplus HPremake final/images/{out_name}"
    make_bg_white(in_path, out_path, tolerance=45)
