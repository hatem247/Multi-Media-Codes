import cv2
import numpy as np

# Read the video file
video = cv2.VideoCapture('video.mp4')

# Define a kernel for edge enhancement
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

# Loop through each frame in the video
while True:
    ret, frame = video.read()  # Read a single frame from the video
    if not ret:  # Break the loop if no frame is returned (end of video)
        break

    # Apply edge enhancement filter to the current frame
    edge_enhanced = cv2.filter2D(frame, -1, kernel)

    # Display the processed frame
    cv2.imshow('Edge Enhanced Video', edge_enhanced)

    # Wait for 25 ms or until the 'q' key is pressed to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
