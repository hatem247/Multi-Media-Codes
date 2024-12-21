import cv2

# Read the input image in grayscale mode
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Convert the grayscale image to an RGB (3-channel) image
RGB_image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

# To make the image appear green, set the Red and Blue channels to 0
RGB_image[:, :, 0] = 0  # Set Blue channel to 0
RGB_image[:, :, 2] = 0  # Set Red channel to 0

# To make the image appear Red, set the Green and Blue channels to 0
# RGB_image[:, :, 1] = 0  # Set Blue channel to 0
# RGB_image[:, :, 2] = 0  # Set Red channel to 0

# To make the image appear Blue, set the Red and Green channels to 0
# RGB_image[:, :, 0] = 0  # Set Blue channel to 0
# RGB_image[:, :, 1] = 0  # Set Red channel to 0

# Convert the modified RGB image to BGR (OpenCV's default format)
BGR_image = cv2.cvtColor(RGB_image, cv2.COLOR_RGB2BGR)

# Display the original grayscale image
cv2.imshow('Original', image)

# Display the converted green-tinted image
cv2.imshow('Converted', BGR_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
