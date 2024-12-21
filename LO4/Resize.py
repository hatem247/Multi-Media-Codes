import cv2

# Read the image from file
image = cv2.imread('image.png')

# Get the height and width of the image
height, width = image.shape[:2]

# Reduce the height and width by half
height /= 2
width /= 2

# Resize the image to the new dimensions
resized = cv2.resize(image, (int(width), int(height)))

# Display the original image in a window
cv2.imshow('Original', image)

# Display the resized image in another window
cv2.imshow('Resized', resized)

# Wait for a key press to close the windows
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()