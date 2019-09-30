# -*- coding: UTF-8 -*-
# 要求： 指定灰度集进行直方图处理，分析不同灰度集的视觉效果
import os
import cv2
import histogram_equalization as he


if __name__ == "__main__":
    model_path = os.path.dirname(__file__)
    img = cv2.imread(model_path + '/example.png')
    _, img1 = he.hist_eq(img, 0, 64)
    _, img2 = he.hist_eq(img, 64, 128)
    _, img3 = he.hist_eq(img, 128, 192)
    _, img4 = he.hist_eq(img, 192, 255)

    cv2.imshow("img1", img1)
    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)
    cv2.imshow('img4', img4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
