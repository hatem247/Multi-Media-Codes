import cv2

# Read the video file
video = cv2.VideoCapture('video.mp4')

# Loop through each frame of the video
while True:
    # Read the next frame from the video
    ret, frame = video.read()

    # Break the loop if no frame is returned (end of video)
    if not ret:
        break

    # Adjust the frame's brightness and contrast
    # alpha controls contrast, beta controls brightness
    edited_frame = cv2.convertScaleAbs(frame, alpha=1.5, beta=50)

    # Display the edited frame in a window
    cv2.imshow('Edited Video', edited_frame)

    # Wait for 25 ms or until the 'q' key is pressed to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break