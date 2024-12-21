import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import local_binary_pattern

# Read the image as grayscale
image = cv2.imread('wood.jpg', cv2.IMREAD_GRAYSCALE)

# Set the radius and number of points for LBP
radius = 1
n_points = 8 * radius

# Compute the Local Binary Pattern (LBP) of the image
lbp = local_binary_pattern(image, n_points, radius, method='uniform')

# Calculate the histogram of the LBP image
lbp_hist, _ = np.histogram(
    lbp.ravel(),  # Flatten the LBP image to a 1D array
    bins=np.arange(0, n_points + 3),  # Define the number of bins
    range=(0, n_points + 2)  # Range of LBP values
)

# Normalize the histogram to represent percentages
lbp_hist = lbp_hist.astype('float')
lbp_hist /= (lbp_hist.sum() + 1e-7)  # Avoid division by zero by adding a small number

# Plot the original image and LBP image side by side
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(image, cmap='gray')  # Show the original image
ax[0].set_title('Original Image')  # Add title to the original image
ax[0].axis('off')  # Remove axes for better visualization

ax[1].imshow(lbp, cmap='gray')  # Show the LBP image
ax[1].set_title('LBP Image')  # Add title to the LBP image
ax[1].axis('off')  # Remove axes for better visualization

# Plot the histogram of LBP values
plt.figure(figsize=(8, 6))
plt.bar(np.arange(0, len(lbp_hist)), lbp_hist, color='red')  # Bar chart of LBP histogram
plt.title('LBP Histogram')  # Add title to the histogram
plt.xlabel('LBP Prototype')  # Label x-axis
plt.ylabel('% of Pixels')  # Label y-axis
plt.show()  # Display the plots