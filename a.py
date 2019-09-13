# -*- coding: UTF-8 -*-
# 要求：打开一BMP文件，将其转存为RGB三通道图像
#       将图像量化为0.5/0.25灰度范围的图像
import cv2

if __name__ == "__main__":
    # 读取图片
    img = cv2.imread('wallhaven.bmp')
    # print(img.shape)

    # cv2.imread()函数读取图片后直接是BGR格式
    # 保存图片
    cv2.imwrite('wallhaven.jpg', img)

    # 转化为灰度图
    imgary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
