import cv2  # Import OpenCV library

# Read the image from the file
image = cv2.imread('image.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original image in a window
cv2.imshow('original', image)

# Display the grayscale image in another window
cv2.imshow('converted', gray_image)

# Wait for a key press indefinitely
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
