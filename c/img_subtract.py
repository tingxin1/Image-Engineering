# -*- coding: UTF-8 -*-
# 要求： 图像减法

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def img_subtract(image1, image2):
    # 读取图片
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    # openCV的图片减法
    imgCV = cv2.subtract(img2, img1)
    # 自己动手实现图片减法
    imgME = np.empty_like(img1)

    rows, cols, channals = img1.shape
    for c in range(channals):
        for i in range(rows):
            for j in range(cols):
                if img2[i, j, c] > img1[i, j, c]:
                    imgME[i, j, c] = img2[i, j, c]-img1[i, j, c]

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure()
    plt.subplot(2, 2, 1)
    plt.imshow(img1[..., ::-1])
    plt.axis('off')
    plt.title("image1")
    plt.subplot(2, 2, 2)
    plt.imshow(img2[..., ::-1])
    plt.axis('off')
    plt.title("image2")
    plt.subplot(2, 2, 3)
    plt.imshow(imgCV[..., ::-1])
    plt.axis('off')
    plt.title(u'使用opencv函数')
    plt.subplot(2, 2, 4)
    plt.imshow(imgME[..., ::-1])
    plt.axis('off')
    plt.title(u'自己手动计算')
    plt.show()


if __name__ == "__main__":
    module_path = os.path.dirname(__file__)
    img_subtract(module_path+"/c1.jpg", module_path+"/c2.jpg")
