import cv2

# Read the image from a file
image = cv2.imread('image.png')

# Convert the image from BGR to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Prompt the user for the hue shift value (0-179)
hue_shift = int(input("Enter the hue shift value (0-179): "))

# Extract the hue channel from the HSV image
hue_channel = hsv[:, :, 0]

# Apply the hue shift and ensure the values wrap around using modulo 180
hue_channel = (hue_channel + hue_shift) % 180

# Update the hue channel of the HSV image with the shifted values
hsv[:, :, 0] = hue_channel

# Convert the modified HSV image back to BGR color space
modified_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Display the original image
cv2.imshow('original', image)

# Display the modified image with the hue shift applied
cv2.imshow('converted', modified_image)

# Wait for a key press and close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
