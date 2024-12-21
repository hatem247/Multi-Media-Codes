import cv2
import numpy as np

# Create a white image of size 400x400 with 3 color channels (RGB)
image = np.ones((400, 400, 3), dtype=np.uint8) * 255

# Draw a black rectangle with top-left corner at (100, 100) and bottom-right at (300, 300)
cv2.rectangle(image, (100, 100), (300, 300), (0, 0, 0), 2)

# Define the boundary of the rectangle
x_min, y_min = 100, 100
x_max, y_max = 300, 300

# Define the line starting and ending points
x1, y1 = 50, 50
x2, y2 = 350, 350

# Clip the line's start and end points to ensure they stay within the rectangle
if x1 < x_min: x1 = x_min
if y1 < y_min: y1 = y_min
if x2 > x_max: x2 = x_max
if y2 > y_max: y2 = y_max

# Draw a blue line (BGR: (255, 0, 0)) from the clipped (x1, y1) to (x2, y2)
cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Define the second line's start and end points
x1, y1 = 150, 50
x2, y2 = 150, 350

# Clip the line's start and end points to ensure they stay within the rectangle
if x1 < x_min: x1 = x_min
if y1 < y_min: y1 = y_min
if x2 > x_max: x2 = x_max
if y2 > y_max: y2 = y_max

# Draw a red line (BGR: (0, 0, 255)) from the clipped (x1, y1) to (x2, y2)
cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the image in a window
cv2.imshow('image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
