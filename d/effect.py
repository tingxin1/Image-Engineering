# -*- coding: UTF-8 -*-
# 要求： 实现两种图片特效
import os
import cv2
import copy as cp
import numpy as np
import matplotlib.pyplot as plt


def wave_effect(image):
    # 水波特效
    img = cp.deepcopy(image)
    row, col, channal = img.shape
    # 水波中心坐标
    center_x = col / 2.0
    center_y = row / 2.0
    A = 3.0  # 振幅大小
    F = 2.0  # 频率大小

    x_mask = np.zeros([row, col])
    y_mask = np.zeros([row, col])
    for i in range(row):
        for j in range(col):
            x_mask[i, j] = j
            y_mask[i, j] = i

    xx_dif = x_mask - center_x
    yy_dif = center_y - y_mask
    theta = np.arctan2(yy_dif,  xx_dif)

    r = np.sqrt(xx_dif * xx_dif + yy_dif * yy_dif)
    r1 = r + A*col*0.01*np.sin(F*0.1*r)

    x_new = r1 * np.cos(theta) + center_x
    y_new = center_y - r1 * np.sin(theta)
    # 向下取整
    int_x = np.floor(x_new)
    int_x = int_x.astype(int)
    int_y = np.floor(y_new)
    int_y = int_y.astype(int)

    for ii in range(row):
        for jj in range(col):
            new_xx = int_x[ii, jj]
            new_yy = int_y[ii, jj]
            if x_new[ii, jj] < 0 or x_new[ii, jj] > col - 1:
                continue
            if y_new[ii, jj] < 0 or y_new[ii, jj] > row - 1:
                continue
            img[ii, jj, :] = image[new_yy, new_xx, :]

    return img


def relief_effect(image):
    # 浮雕特效
    img = cp.deepcopy(image)
    # 转化为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(img_gray.shape[0]):
        for j in range(img_gray.shape[1]-1):
            tmp = img_gray[i, j] - img_gray[i, j + 1]+128
            if tmp > 255:
                tmp = 255
            if tmp < 0:
                tmp = 0
            img_gray[i, j] = tmp

    return img_gray


if __name__ == "__main__":
    model_path = os.path.dirname(__file__)
    img = cv2.imread(model_path + '/example.png')
    relief = relief_effect(img)
    wave = wave_effect(img)

    plt.figure('effect')
    plt.subplot(121)
    plt.title('original')
    plt.imshow(img[..., ::-1])
    plt.axis('off')
    plt.subplot(222)
    plt.title('wave effect')
    plt.imshow(wave[..., ::-1])
    plt.axis('off')
    plt.subplot(224)
    plt.title('relief effect')
    plt.imshow(relief, cmap='gray')
    plt.axis('off')
    plt.show()
