# Import the opencv library
import cv2

# We initialize the webcam
cap = cv2.VideoCapture(0)  # 0 represents the built-in camera (can be changed depending on the number of webcams)

# Set the Frame Width and Height ( you can change to your desired Frame Width and Height )
cap.set(4, 640)  # set Width
cap.set(3, 480)  # set Height


while True:

    # The Captured video frame is read
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('My First Webcam Video Capture in Opencv-Python', frame)

    # The "s" button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('s'):  # you can change to your desired button of your choice
        break

# After the loop release the cap object
cap.release()
# All OpenCV windows are closed
cv2.destroyAllWindows()
