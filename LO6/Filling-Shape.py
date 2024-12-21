import cv2
import numpy as np

# Create a white image of size 300x300 with 3 color channels (RGB)
image = np.ones((300, 300, 3), np.uint8) * 255

# Draw a black rectangle with a thickness of 2 pixels
cv2.rectangle(image, (50, 50), (250, 250), (0, 0, 0), 2)

# Define a seed point for the flood fill operation
seed_point = (100, 100)

# Define the color to fill with (green in BGR format)
filling_color = (0, 255, 0)

# Create a mask of size (302x302) with a border of 1 pixel around the image
mask = np.zeros((302, 302), dtype=np.uint8)

# Perform flood fill starting from the seed point
cv2.floodFill(image, mask, seed_point, filling_color)

# Display the filled image in a window
cv2.imshow('image', image)

# Wait for a key press to close the window
cv2.waitKey(0)

# Destroy all created windows
cv2.destroyAllWindows()
