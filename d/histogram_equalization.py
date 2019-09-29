# -*- coding: UTF-8 -*-
# 要求： 直方图增强：图像点操作处理之后：
#           原始图像/处理后的图像/均衡化后图像的直方图比较
#           统计分析视觉观感与直方图的关系
#           指定灰度集进行直方图处理，分析不同灰度集的视觉效果

import os
import cv2
import copy
import numpy as np
from matplotlib import pyplot as plt

def hist_eq(image):
    # 直方图均衡化
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgArray = imgGray.flatten()

    # 统计不同灰度级的像素数
    grayNum = np.zeros(256, dtype=int)
    for pixel in imgArray:
        grayNum[pixel] += 1

    # 计算每个灰度级的概率
    probability = np.zeros(256, dtype=float)
    for i in range(0, 255):
        probability[i] = grayNum[i]/imgArray.size

    # 统计每个灰度级的累计概率
    probabilitySum = np.zeros(256, dtype=float)
    for i in range(0, 256):
        for j in range(0, i):
            probabilitySum[i] += probability[j]








module_path = os.path.dirname(__file__)
filein = module_path+'/testimg.jpg'
img = cv2.imread(filein)
# cv2.imshow('y', img)




# 直方图变换
i = 0
imgArrayEnhanced = copy.deepcopy(imgArray)
for pixel in imgArray:
    imgArrayEnhanced[i] = probabilitySum[pixel]*255+0.5
    i += 1

# 绘制直方图
plt.subplot(211)
plt.xlabel('grade')
plt.ylabel('numbers')
plt.hist(imgArray, bins=256, density=0, edgecolor='None', facecolor='red')
plt.subplot(212)
plt.xlabel('grade')
plt.ylabel('numbers')
plt.hist(imgArrayEnhanced, bins=256, density=0,
         edgecolor='None', facecolor='red')
plt.show()

imgGrayEnhanced = imgArrayEnhanced.reshape(512, 512)

cv2.imshow('enhanced', imgGrayEnhanced)
cv2.imshow('before', imgGray)
cv2.waitKey(0)