import cv2
import numpy as np

width, height = 250, 350

img = cv2.imread('resources/cards.jpg')

pts1 = np.float32([[752, 118], [1120, 265], [540, 668], [871, 830]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Cards", img)
cv2.imshow("Cards Wrapped", imgOutput)
cv2.waitKey(0)