# 生成图像文件，要求颜色等阶渐变，观察人言最小分辨率

import numpy as np
import cv2

img = np.zeros((500, 1000), np.uint8)

img.fill(240)

for i in range(256):
    img[i + 100][120:180] = 255 - i

for i in range(0, 256, 32):
    img[i+100:i+132, 720:780] = 255-i

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
