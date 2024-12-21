import cv2

# Read the video file
video = cv2.VideoCapture('video.mp4')

# Loop through the video frames
while True:
    ret, frame = video.read()  # Read a single frame from the video
    if not ret:  # Break the loop if no frame is returned (end of video)
        break

    # Convert the frame from BGR to YUV color space
    yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

    # Equalize the histogram of the Y channel (brightness)
    yuv_frame[:, :, 0] = cv2.equalizeHist(yuv_frame[:, :, 0])

    # Convert the frame back from YUV to BGR color space
    corrected_frame = cv2.cvtColor(yuv_frame, cv2.COLOR_YUV2BGR)

    # Display the corrected frame in a window
    cv2.imshow('Corrected Video', corrected_frame)

    # Wait for 25 ms or until the 'q' key is pressed to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break