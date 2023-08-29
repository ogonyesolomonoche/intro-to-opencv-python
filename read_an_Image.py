# Import the opencv library
import cv2

# The command to load and read the image
image = cv2.imread("image.jpg")  # Image path and can be changed to your desired path

# The image is then displayed
cv2.imshow("My First Loaded Image in Opencv-Python", image)

# Wait for a specified milliseconds to keep the window on display till a key is pressed
cv2.waitKey(0)

# All OpenCV windows are closed
cv2.destroyAllWindows()
