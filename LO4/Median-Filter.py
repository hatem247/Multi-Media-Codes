import cv2

# Read the input image from the file
image = cv2.imread('Median_image.png')

# Apply median blur filter to remove noise, with a kernel size of 7
denoised_image = cv2.medianBlur(image, 7)

# Display the original image in a window
cv2.imshow('Original Image', image)

# Display the denoised image after applying the median filter
cv2.imshow('Median Filter', denoised_image)

# Close the window when a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()