# Import the opencv library
import cv2

# We Load the video path
cap = cv2.VideoCapture(0)  # ".."represents the default webcam (can be changed to your desired webcam)

# Set the Frame Width and Height ( you can change to your desired Frame Width and Height )
cap.set(4, 640)  # set Width
cap.set(3, 480)  # set Height

# We start Video Record
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:

    # The Captured video frame is read
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert Frame to GrayScale

    # The recorded video is saved
    out.write(frame)

    # Display the resulting frames
    cv2.imshow('My first window frame to capture video', frame)
    cv2.imshow('the gray_scale video', gray)

    # The "s" button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('s'):  # you can change to your desired button of your choice
        break

# After the loop release the cap and output object
cap.release()
out.release()
# All OpenCV windows are closed
cv2.destroyAllWindows()
