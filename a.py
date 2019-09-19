# -*- coding: UTF-8 -*-
# 要求：打开一BMP文件，将其转存为RGB三通道图像
#      将图像量化为0.5/0.25灰度范围的图像
import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 读取图片
    img = cv2.imread('wallhaven.bmp')
    # print(img.shape)

    # cv2.imread()函数读取图片后直接是BGR格式
    # 保存图片
    # cv2.imwrite('wallhaven.jpg', img)

    # opencv转化灰度图
    imgray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 手动计算转换灰度图
    imgray1 = np.dot(img[..., :3], [0.114, 0.587, 0.299]).astype(np.uint8)
    # print(imgray1.shape)
    #将图像量化到0.25~0.5之间
    imgray2 = imgray1/256*64+64
    fig = plt.figure()
    plt.subplot(2, 3, 1)
    plt.title('opencv method')
    plt.imshow(imgray0, cmap='gray')
    plt.axis('off')
    plt.subplot(2, 3, 2)
    plt.title('caculate')
    plt.imshow(imgray1, cmap='gray')
    plt.axis('off')
    plt.subplot(2, 3, 3)
    plt.title('0.25~0.5')
    plt.imshow(imgray2, cmap='gray')
    plt.axis('off')
    plt.subplot(2, 3, 4)
    plt.hist(np.ravel(imgray0), bins=256, normed=True, color='c')
    plt.subplot(2, 3, 5)
    plt.hist(np.ravel(imgray1), bins=256, normed=True, color='c')
    plt.subplot(2, 3, 6)
    plt.hist(np.ravel(imgray2), bins=256, normed=True, color='c')
    plt.show()
