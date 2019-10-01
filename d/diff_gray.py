# -*- coding: UTF-8 -*-
# 要求： 指定灰度集进行直方图处理，分析不同灰度集的视觉效果
import os
import cv2
import numpy as np
import histogram_equalization as he
import matplotlib.pyplot as plt


if __name__ == "__main__":
    model_path = os.path.dirname(__file__)
    img = cv2.imread(model_path + '/example.png')
    _, img1 = he.hist_eq(img, 0, 85)
    _, img2 = he.hist_eq(img, 85, 170)
    _, img3 = he.hist_eq(img, 170, 255)

    htitch1 = np.hstack((_, img1))
    htitch2 = np.hstack((img2, img3))
    vtitch = np.vstack((htitch1, htitch2))

    cv2.namedWindow('original,0~85,85~170,170~255',flags=cv2.WINDOW_NORMAL)
    cv2.imshow('original,0~85,85~170,170~255', vtitch)
    cv2.imwrite('picture.png',vtitch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.figure('different gray')
    plt.subplot(4, 1, 1)
    plt.title('original')
    # plt.axis('off')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.hist(_.flatten(), bins=256, density=0,
             edgecolor='None', facecolor='black')
    plt.xlim([0, 256])

    plt.subplot(4, 1, 2)
    plt.title('0~85')
    # plt.axis('off')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.hist(img1.flatten(), bins=256, density=0,
             edgecolor='None', facecolor='black')
    plt.xlim([0, 256])
    plt.subplot(4, 1, 3)
    plt.title('85~170')
    # plt.axis('off')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.hist(img2.flatten(), bins=256, density=0,
             edgecolor='None', facecolor='black')
    plt.xlim([0, 256])
    plt.subplot(4, 1, 4)
    plt.title('170~255')
    # plt.axis('off')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.hist(img3.flatten(), bins=256, density=0,
             edgecolor='None', facecolor='black')
    plt.xlim([0, 256])
    plt.tight_layout()
    plt.show()
