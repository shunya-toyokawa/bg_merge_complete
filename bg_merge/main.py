from PIL import Image

# 切り抜き画像
img = Image.open('cutout.png').convert('RGBA')

# 背景画像
bg = Image.open('inpaint.png').convert('RGBA')

# 画像合成
img_clear = Image.new("RGBA", bg.size, (255, 255, 255, 0))
img_clear.paste(img, (0,0))
bg = Image.alpha_composite(bg, img_clear)

# 画像保存
bg.save('output.png')
