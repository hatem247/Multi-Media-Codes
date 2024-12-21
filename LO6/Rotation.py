import cv2
import numpy as np

# Create a white image of size 300x300 with 3 color channels
image = np.ones((300, 300, 3), np.uint8) * 255

# Draw a black rectangle on the image with the top-left corner at (100,100) and bottom-right corner at (200,200)
cv2.rectangle(image, (100, 100), (200, 200), (0, 0, 0), -1)

# Define the center of the image for the rotation
center = (image.shape[1] // 2, image.shape[0] // 2)

# Define the rotation angle in degrees and the scaling factor
angle = 45
scale = 1.0

# Get the 2D rotation matrix for the given center, angle, and scale
Rotation_Matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Rotate the image using the computed rotation matrix
rotated = cv2.warpAffine(image, Rotation_Matrix, (image.shape[1], image.shape[0]))

# Display the original image in a window named 'image'
cv2.imshow('image', image)

# Display the rotated image in a window named 'rotated'
cv2.imshow('rotated', rotated)

# Wait indefinitely for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
