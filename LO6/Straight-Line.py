import cv2
import numpy as np

# Create a blank white image of size 500x500 with 3 color channels (RGB)
image = np.ones((500, 500, 3), np.uint8) * 255

# Draw a black diagonal line from the top-left corner to the bottom-right corner
# The line has a thickness of 5 pixels
cv2.line(image, (0, 0), (500, 500), (0, 0, 0), 5)

# Display the image in a window named 'image'
cv2.imshow('image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
