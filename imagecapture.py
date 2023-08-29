# Import the opencv library
import cv2

# We initialize the webcam
cap = cv2.VideoCapture(0)  # 0 represents the built-in camera (can be changed depending on the number of webcams)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
else:
    # the command to read the frame from webcam
    ret, frame = cap.read()

    if ret:
        # The captured frame is saved as an image
        cv2.imwrite("captured_image.jpg", frame)  # Image path and can be changed to your desired path
        print("Image captured successfully and saved as 'captured_image.jpg'")
    else:
        print("Error: Failed to capture an image.")

    # Release the webcam
    cap.release()

# All OpenCV windows are closed
cv2.destroyAllWindows()
