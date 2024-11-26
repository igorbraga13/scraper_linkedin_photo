# Importing packages
from rembg import remove
from PIL import Image

exec(open('src/scraper.py').read())

# Opening images
image1 = Image.open('data/image1.jpg')
image2 = Image.open('data/image2.jpg')
background = Image.open('data/background.jpg')

# Removing background
image1 = remove(image1)
image2 = remove(image2)
# img1.save('data/image1.png')
# img2.save('data/image2.png')

# Resizing images if necessary
image1 = image1.resize((250, 250)) 
image2 = image2.resize((250, 250))
background = background.resize((500, 250))

# Defining the positions where images will be overlapped on the background image
position1 = (50, 0)   # Coordinates (x, y) for the first image
position2 = (200, 0)  # Coordinates (x, y) for the second image

# Overlapping
background.paste(image1, position1, image1)
background.paste(image2, position2, image2)
background.save('data/combined_image.png')