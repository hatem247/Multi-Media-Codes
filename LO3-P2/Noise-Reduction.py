import cv2

# Read the video file
video = cv2.VideoCapture('video.mp4')

# Define the kernel size for Gaussian Blur
kernel = (5, 5)

while True:
    # Read the next frame from the video
    ret, frame = video.read()

    # Break the loop if no frame is returned (end of video)
    if not ret:
        break

    # Apply Gaussian Blur to the frame to denoise it
    denoised_frame = cv2.GaussianBlur(frame, kernel, 0)

    # Display the denoised frame in a window
    cv2.imshow('Denoised Video', denoised_frame)

    # Wait for 25 ms or until the 'q' key is pressed to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break