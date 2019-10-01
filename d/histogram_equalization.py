# -*- coding: UTF-8 -*-
# 要求： 直方图增强：图像点操作处理之后：
#           原始图像/处理后的图像/均衡化后图像的直方图比较
#           统计分析视觉观感与直方图的关系
#           指定灰度集进行直方图处理，分析不同灰度集的视觉效果

import os
import cv2
import copy as cp
import numpy as np
from matplotlib import pyplot as plt


def hist_eq(image, gray_min=0, gray_max=255):
    # 直方图均衡化
    # image: opencv读入的BGR三通道图片
    # gray_min: 直方图均衡化后灰度值下界，默认为0
    # gray_max: 直方图均衡化后灰度值上界，默认为255

    # 转为灰度图
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = img_gray.shape
    pixel_sum = height*width
    # 统计不同灰度级的像素数
    gray_num = np.zeros(256, dtype=int)
    for i in range(height):
        for j in range(width):
            gray_num[img_gray[i, j]] += 1
    # 计算每个灰度级的概率
    probability = np.zeros(256, dtype=float)
    for i in range(0, 255):
        probability[i] = gray_num[i] / pixel_sum
    # 统计每个灰度级的累计概率
    probability_sum = np.zeros(256, dtype=float)
    for i in range(0, 256):
        for j in range(0, i):
            probability_sum[i] += probability[j]
    # 直方图均衡化
    img_hist_eq = cp.deepcopy(img_gray)
    for i in range(height):
        for j in range(width):
            img_hist_eq[i, j] = probability_sum[img_gray[i, j]]*(gray_max-gray_min)+gray_min
    return img_gray, img_hist_eq


if __name__ == "__main__":
    module_path = os.path.dirname(__file__)
    filein = module_path+'/example.png'
    img = cv2.imread(filein)
    img_O, img_HE = hist_eq(img)
    img_O_hist = img_O.flatten()
    img_HE_hist = img_HE.flatten()

    # opencv直方图均衡化
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eq = cv2.equalizeHist(image)
    hist = cv2.calcHist([eq], [0], None, [256], [0, 256])
    
    # 绘制直方图
    plt.figure()
    plt.subplot(321)
    plt.title('original')
    plt.imshow(img_O, cmap='gray')
    plt.axis('off')
    plt.subplot(322)
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.hist(img_O_hist, bins=256, density=0,
             edgecolor='None', facecolor='black')
    plt.xlim([0, 256])
    plt.subplot(323)
    plt.title('histogram_equalization')
    plt.imshow(img_HE, cmap='gray')
    plt.axis('off')
    plt.subplot(324)
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.hist(img_HE_hist, bins=256, density=0,
             edgecolor='None', facecolor='red')
    plt.xlim([0, 256])
    plt.subplot(325)
    plt.title('openCV histogram equalization')
    plt.imshow(eq, cmap='gray')
    plt.axis('off')
    plt.subplot(326)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
