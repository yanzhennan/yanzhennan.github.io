from PIL import Image, ImageDraw, ImageFont

# Create a 32x32 image
img = Image.new('RGB', (32, 32), color='#333333')
d = ImageDraw.Draw(img)

# Try to use a font
try:
    fnt = ImageFont.truetype('arial.ttf', 20)
except:
    fnt = ImageFont.load_default()

# Draw a simple 'B' for blog
d.text((8, 4), 'B', font=fnt, fill='white')

# Save as ICO
img.save('assets/images/favicon.ico')
print('Favicon created successfully!')