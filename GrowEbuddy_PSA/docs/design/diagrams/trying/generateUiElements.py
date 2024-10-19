from PIL import Image, ImageDraw

def create_button(text, width, height):
    img = Image.new('RGB', (width, height), color='white')
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, width-1, height-1], outline='black')
    d.text((10, 10), text, fill='black')
    return img

button = create_button('Click me', 100, 40)
button.save('button.png')

# Add these lines to display the image
button.show()
