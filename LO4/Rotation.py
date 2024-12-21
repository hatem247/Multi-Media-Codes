import cv2
import imutils

# Load the image from the file 'image.png'
image = cv2.imread('image.png')

# Rotate the image 90 degrees using the imutils library
rotated = imutils.rotate(image, 90)

# Display the original image in a window named 'Original'
cv2.imshow('Original', image)

# Display the rotated image in a window named 'Rotated'
cv2.imshow('Rotated', rotated)

# Wait for key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
