import cv2
import numpy as np

# Read the image from a file
image = cv2.imread('image.png')

# Convert the image from BGR to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Extract the saturation channel (2nd channel) from the HSV image
saturation_channel = hsv[:, :, 1]

# Get the saturation multiplier from user input
multiplier = float(input("Enter the saturation multiplier (e.g., 1.5): "))

# Adjust the saturation by scaling it with the multiplier and clip values to the range [0, 255]
saturation_channel = np.clip(saturation_channel * multiplier, 0, 255)

# Update the saturation channel in the HSV image
hsv[:, :, 1] = saturation_channel

# Convert the modified HSV image back to BGR color space
modified_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Display the original image
cv2.imshow('original', image)

# Display the image with adjusted saturation
cv2.imshow('converted', modified_image)

# Wait for any key press before closing the image windows
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()
