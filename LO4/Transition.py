import cv2
import numpy as np

# Read the input image
image = cv2.imread('image.png')

# Get the number of rows and columns in the image
rows, cols = image.shape[:2]

# Define the transition offsets
x = 200  # Transition 200 pixels to the right
y = 50  # Transition 50 pixels down

# Create the transition matrix
Transition_Matrix = np.float32([[1, 0, x], [0, 1, y]])

# Apply the affine transformation using the transition matrix
Transitioned_image = cv2.warpAffine(image, Transition_Matrix, (cols, rows))

# Display the original image
cv2.imshow('Original', image)

# Display the transitioned image
cv2.imshow('Transitioned_image', Transitioned_image)

# Wait for any key press to close the windows
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()
