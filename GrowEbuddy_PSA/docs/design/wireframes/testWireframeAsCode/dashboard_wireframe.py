from PIL import Image, ImageDraw, ImageFont

# Create a blank image
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw header
draw.rectangle([0, 0, width, 100], fill='lightgray')
draw.text((20, 30), "GrowEbuddy Dashboard", fill='black')

# Draw navigation bar
draw.rectangle([0, 100, width, 150], fill='lightblue')
draw.text((20, 120), "Home | Daily Check-in | Mini-Games | Profile", fill='black')

# Draw main content area
draw.rectangle([20, 160, width - 20, height - 20], outline='black', fill='lightyellow')
draw.text((30, 180), "Welcome, [User Name]!", fill='black')
draw.text((30, 220), "Your Mood: [Mood Indicator]", fill='black')

# Save the wireframe
image.save('dashboard_wireframe.png')