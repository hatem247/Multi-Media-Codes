import cv2
from skimage.restoration import denoise_tv_chambolle

# Read the input image in grayscale mode
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Regularization parameter for the denoising algorithm (higher values result in stronger smoothing)
lambda_reg = 0.9

# Apply Total Variation denoising using the Chambolle algorithm
denoised_image = denoise_tv_chambolle(image, weight=lambda_reg)

# Display the original image in a window
cv2.imshow('original', image)

# Display the denoised image in another window
cv2.imshow('denoised', denoised_image)

# Wait indefinitely for a key press before closing the windows
cv2.waitKey(0)

# Destroy all OpenCV-created windows
cv2.destroyAllWindows()
