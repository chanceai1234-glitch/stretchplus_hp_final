try:
    from PIL import Image
    import os
    img_path = 'stretchplus-theme/image_final/common_logo.png'
    out_path = 'stretchplus-theme/image_final/favicon.png'
    
    img = Image.open(img_path)
    
    # 透過の正方形キャンバスを作成（元画像の長辺を基準に少し余白を作る）
    size = max(img.size)
    pad_size = int(size * 1.1) 
    
    new_img = Image.new("RGBA", (pad_size, pad_size), (255, 255, 255, 0)) # 完全透過
    # 元画像を中央に貼り付け
    offset_x = (pad_size - img.width) // 2
    offset_y = (pad_size - img.height) // 2
    new_img.paste(img, (offset_x, offset_y))
    
    # 標準的なファビコンサイズ (512x512) にリサイズ
    new_img = new_img.resize((512, 512), Image.Resampling.LANCZOS)
    new_img.save(out_path)
    print(f"Success: {out_path} created!")
except Exception as e:
    print(f"Error: {e}")
