import cv2
import numpy as np

# Load the image
image = cv2.imread('image.png')

# Convert the image from BGR to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Get user input for the value to adjust the brightness
value = int(input("Enter the value: "))

# Extract the Value channel (brightness) from the HSV image
value_channel = hsv[:, :, 2]

# Modify the Value channel by adding the user-input value, ensuring it remains within the valid range (0-255)
value_channel = np.clip(value_channel + value, 0, 255)

# Update the Value channel in the HSV image
hsv[:, :, 2] = value_channel

# Convert the modified HSV image back to BGR color space
modified_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Display the original image
cv2.imshow('original', image)

# Display the modified image
cv2.imshow('converted', modified_image)

# Wait for a key press before closing the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
