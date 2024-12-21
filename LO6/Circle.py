import cv2
import numpy as np

# Create a white 500x500 image with 3 color channels (RGB)
image = np.ones((500, 500, 3), np.uint8) * 255

# Draw a filled black circle at the center of the image with a radius of 100 pixels
cv2.circle(image, (250, 250), 100, (0, 0, 0), -1)

# Display the image in a window titled 'image'
cv2.imshow('image', image)

# Wait for a key press indefinitely
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
