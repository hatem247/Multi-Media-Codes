import cv2
import numpy as np

# Create a white image of size 500x500 with 3 color channels (RGB)
image = np.ones((500, 500, 3), np.uint8) * 255

# Draw a black filled rectangle with top-left corner at (100, 100)
# and bottom-right corner at (300, 300)
cv2.rectangle(image, (100, 100), (300, 300), (0, 0, 0), -1)

# Resize the image by 1.5x in both width and height using linear interpolation
resized = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# Display the original image in a window named 'image'
cv2.imshow('image', image)

# Display the resized image in a window named 'resized'
cv2.imshow('resized', resized)

# Wait indefinitely for a key press from the user
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
