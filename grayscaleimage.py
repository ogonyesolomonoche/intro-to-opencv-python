# Import the opencv library
import cv2

# The command to load and read the image
image = cv2.imread("image.jpg")  # Image path and can be changed to your desired path
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert Image to RGB
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to GrayScale

# The image is then displayed
cv2.imshow("My First Loaded GrayScale-Image in Opencv-Python", gray)

# Wait for a specified milliseconds to keep the window on display till a key is pressed
cv2.waitKey(0)

# All OpenCV windows are closed
cv2.destroyAllWindows()
