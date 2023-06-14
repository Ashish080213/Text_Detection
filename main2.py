# Import the OpenCV library for image processing
import cv2

# Read in the input using the cv2.imread() function and store it in the variable img
# This image will be used as input for the subsequent image processing steps
img = cv2.imread("Ragged2eOLV21.png")

# Convert the image BGR (Blue-Green-Red) color space to grayscale
# Grayscale images only contain intensity values, while BGR images also contain color information
# Converting the image to grayscale simplifies the image processing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding is a technique that separates the text from the background by setting pixel values above a certain threshold to white and pixel values below the threshold to black
# The cv2.threshold() function takes the grayscale image as input, a threshold value of 127, and a maximum value of 255.
# This means that all pixel values below 127 will be set to 0 (black), and all pixel values above 127 will be set to 255 (white).
# The underscore (_) in the code indicates that we don't need the first value returned by cv2.threshold(), which is the threshold value used.
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours in the binary image

# Contours are continuous lines or curves that form the boundaries of objects in an image.
# The cv2.findContours() function takes the binary image as input, a retrieval mode of cv2.RETR_TREE, and a contour approximation method of cv2.CHAIN_APPROX_SIMPLE.
# The retrieval mode cv2.RETR_TREE retrieves all of the contours and reconstructs a full hierarchy of nested contours.
# The contour approximation method cv2.CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments and leaves only their end points, which speeds up the contour processing.
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop through the contours and draw bounding boxes around each one

# The cv2.boundingRect() function calculates the minimum bounding rectangle that encloses the contour.
# The function returns the (x,y) coordinates of the top-left corner of the bounding box (x, y), as well as its width (w) and height (h).
# The cv2.rectangle() function draws a green rectangle around the contour on the original image img. T
# The rectangle is defined by the top-left and bottom-right coordinates of the bounding box, (x, y) and (x+w, y+h), respectively.
# The rectangle thickness is set to 2 pixels.
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Display the image with bounding boxes
cv2.imshow("Bounding Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
