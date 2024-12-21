import cv2

# Read the image from the file
image = cv2.imread('image.png')

# Set alpha (contrast factor) and beta (brightness factor)
alpha = 2  # Contrast control (higher means more contrast)
beta = 100  # Brightness control (higher means brighter)

# Apply the contrast and brightness adjustment to the image
new_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Display the original image in a window
cv2.imshow('Original Image', image)

# Display the adjusted image in a window
cv2.imshow('Adjusted Image', new_image)

# Close when a key is pressed
cv2.waitKey(0)

# Destroy all windows created by OpenCV
cv2.destroyAllWindows()
