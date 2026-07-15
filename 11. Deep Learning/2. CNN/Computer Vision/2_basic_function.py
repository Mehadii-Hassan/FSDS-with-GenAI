import cv2

# 1. Convert color image to grayscale
# image = cv2.imread('C:\\Users\\Mehedi\\Desktop\\FSDS with Gen AI\\FSDS-with-GenAI\\11. Deep Learning\\2. CNN\\Computer Vision\\resources\\lena.png')
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# print(image.shape) 
# print(image_gray.shape) 

# cv2.imshow('Lena Image', image) # Display the image in a window
# cv2.imshow('Lena Image Gray', image_gray) # Display the grayscale image in a window

# cv2.waitKey(0) # Wait for a key press to close the window
# cv2.destroyAllWindows() # Close all OpenCV windows



# 2. Convert color image to blur
# image = cv2.imread('C:\\Users\\Mehedi\\Desktop\\FSDS with Gen AI\\FSDS-with-GenAI\\11. Deep Learning\\2. CNN\\Computer Vision\\resources\\lena.png')
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# image_blur = cv2.GaussianBlur(image_gray, (7, 7), 0) # Apply Gaussian blur with a kernel size of 7x7

# print(image.shape) 
# print(image_gray.shape) 
# print(image_blur.shape) 

# cv2.imshow('Lena Image', image) 
# cv2.imshow('Lena Image Gray', image_gray) 
# cv2.imshow('Lena Image Blur', image_blur) 

# cv2.waitKey(0) 
# cv2.destroyAllWindows() 



# 3. Convert color image to canny edge detection
image = cv2.imread('C:\\Users\\Mehedi\\Desktop\\FSDS with Gen AI\\FSDS-with-GenAI\\11. Deep Learning\\2. CNN\\Computer Vision\\resources\\lena.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blur = cv2.GaussianBlur(image_gray, (7, 7), 0) # Apply Gaussian blur with a kernel size of 7x7
image_canny = cv2.Canny(image_blur, 100, 100) # Apply Canny edge detection with threshold values of 100 and 100

print(image.shape) 
print(image_gray.shape) 
print(image_blur.shape) 
print(image_canny.shape) 

cv2.imshow('Lena Image', image) 
cv2.imshow('Lena Image Gray', image_gray) 
cv2.imshow('Lena Image Blur', image_blur) 
cv2.imshow('Lena Image Canny', image_canny) 

cv2.waitKey(0) 
cv2.destroyAllWindows() 