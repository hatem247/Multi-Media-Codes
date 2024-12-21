import cv2
import numpy as np

# Compresses data using Run-Length Encoding (RLE).
def rle_encoding(img):
    encoding = []
    prev_pixel = img[0]
    count = 1
    for pixel in img[1:]:
        if pixel == prev_pixel:
            count += 1
        else:
            encoding.extend([prev_pixel, count])
            prev_pixel = pixel
            count = 1
    encoding.extend([prev_pixel, count])
    return encoding

# Decompresses data using Run-Length Encoding (RLE).
def rle_decoding(encoded_img, shape):
    decoded = []
    for i in range(0, len(encoded_img), 2):
        pixel = encoded_img[i]
        count = encoded_img[i + 1]
        decoded.extend([pixel] * count)
    return np.array(decoded).reshape(shape)

# Read the image
image = cv2.imread('image.bmp')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize image
width = int(gray_image.shape[1] * 0.5)
height = int(gray_image.shape[0] * 0.5)
gray_image = cv2.resize(gray_image, (width, height), interpolation = cv2.INTER_AREA)

# Flatten image pixels
pixels = gray_image.flatten()

# Compress using RLE
compressed_image = rle_encoding(pixels)

# Convert to NumPy array with a larger data type
compressed_array = np.array(compressed_image, dtype=np.uint8)

# Save the compressed data as npy
np.save("compressed_pixels.npy", compressed_array)

# Decompress the data
decompressed_image = rle_decoding(compressed_image, gray_image.shape)

# Save the decompressed image as a .bmp file
cv2.imwrite("compressed_image.bmp", decompressed_image)

print("Compression complete. Decompressed image saved as 'Compressed_image_new.bmp'.")