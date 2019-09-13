import cv2
import numpy as np

imgmk = np.zeros([500, 900, 3], dtype=np.uint8)
imgmk[:, 0:300, 2] = 255
imgmk[:, 300:600, 1] = 255
imgmk[:, 600:900, 0] = 255

cv2.namedWindow('imgmk', cv2.WINDOW_AUTOSIZE)
cv2.imshow('imgmk', imgmk)
cv2.waitKey(0)
imgary = cv2.cvtColor(imgmk, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgary', imgary)
cv2.waitKey(0)

imgB, imgG, imgR = cv2.split(imgmk)
# img=cv2.merge([imgB,imgG,imgR])
# cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# cv2.imshow('img', img)
# cv2.waitKey(0)
cv2.namedWindow('imgB', cv2.WINDOW_AUTOSIZE)
cv2.imshow('imgB', imgB)
cv2.waitKey(0)
cv2.namedWindow('imgG', cv2.WINDOW_AUTOSIZE)
cv2.imshow('imgG', imgG)
cv2.waitKey(0)
cv2.namedWindow('imgR', cv2.WINDOW_AUTOSIZE)
cv2.imshow('imgR', imgR)
cv2.waitKey(0)
cv2.destroyAllWindows()
