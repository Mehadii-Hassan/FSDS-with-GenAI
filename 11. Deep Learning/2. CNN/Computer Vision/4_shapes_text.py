import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) # Create a black image of size 512x512 pixels
print(img.shape)

# img[:] = 255, 0, 0 # Fill the image with blue color
# img[:] = 0, 255, 0 # Fill the image with green color
# img[:] = 0, 0, 255 # Fill the image with red color
img[:] = 124, 199, 243 # Fill the image with a custom color (BGR format)

# Create a line
# cv2.line(img, (0, 0), (300, 400), (0, 255, 0), 5) # Draw a white line from (0,0) to (300,300) with thickness of 5 pixels

# Create a Rectangle
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 7) # Draw a rectangle from (0,0) to (250,350) with red color and thickness of 7 pixels

# Create a Circle
# cv2.circle(img, (400, 50), 50, (0, 0, 255), 4) # Draw a circle at (400, 50) with radius 50 and blue color and thickness of 4 pixels

# Put Text on the image
cv2.putText(img, "Md. Mehadi Hassan", (200, 440), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1) 

cv2.imshow("Output", img)
cv2.waitKey(0)