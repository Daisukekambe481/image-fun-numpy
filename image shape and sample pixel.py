import numpy as np
from PIL import Image

# Load/Open the image
img = Image.open(r"C:\Users\Rameez\OneDrive\Projects\numpy project\image-fun-numpy\Sample image.jpg")

# Convert to NumPy array
img_array = np.array(img)

# Print Image shape
print("Image shape:", img_array.shape)

# Print a small 5x5 block of pixels (rows 40-44, cols 40-44)
print("5x5 block from (50,50):\n", img_array[40:45, 40:45])