# -*- coding: UTF-8 -*-
# 要求： 实现两种图片特效
import os
import cv2
import copy as cp
import numpy as np


def wave_effect(image):
    img = cp.deepcopy(image)


def relief_effect(image):
    # 浮雕特效
    img = cp.deepcopy(image)
    # 转化为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(img_gray.shape[0]):
        for j in range(img_gray.shape[1]-1):
            tmp = img_gray[i, j] - img_gray[i, j + 1]+150
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
    cv2.imshow('relief effect', relief)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
