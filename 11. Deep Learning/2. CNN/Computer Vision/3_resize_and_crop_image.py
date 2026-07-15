import cv2

# Resizing images
# img = cv2.imread("resources\lambo.png")
# print(img.shape)

# resized_img = cv2.resize(img, (300, 200)) # Resize the image to 300x200 pixels
# print(resized_img.shape)
# cv2.imshow("Output", img)
# cv2.imshow("Resized Output", resized_img)
# cv2.waitKey(0) 



# Cropping images
img = cv2.imread("resources\lambo.png")
crop_img = img[0:200, 200:500] # Crop the image from y=0 to y=200 and x=200 to x=500
print(crop_img.shape)

cv2.imshow("Output", img)
cv2.imshow("Cropped Output", crop_img)
cv2.waitKey(0) 