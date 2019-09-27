import os
import cv2
import copy as cp
import numpy as np
import matplotlib.pyplot as plt


def Linear(image):
    # 线性变化
    img = cp.deepcopy(image)    # 深拷贝，为保证不对原图进行修改
    rows, cols, channals = img.shape
    for c in range(channals):
        for i in range(rows):
            for j in range(cols):
                img[i, j, c] = img[i, j, c]//3
    return img


def Nonlinear(image):
    img = cp.deepcopy(image)
    img = np.power(img.astype(np.int32), 2)//252
    # rows, cols, channals = img.shape
    # for c in range(channals):
    #     for i in range(rows):
    #         for j in range(cols):
    #             img[i, j, c] = 30*math.log(img[i, j, c])
    return img


if __name__ == "__main__":
    model_path = os.path.dirname(__file__)
    img = cv2.imread(model_path + '/example.png')
    img_linear = Linear(img)
    img_nonlinear = Nonlinear(img)

    plt.figure()
    plt.subplot(1, 3, 1)
    plt.title('original')
    plt.axis('off')
    plt.imshow(img[..., ::-1])
    plt.subplot(1, 3, 2)
    plt.title('Linear x/3')
    plt.axis('off')
    plt.imshow(img_linear[..., ::-1])
    plt.subplot(1, 3, 3)
    plt.title('Nonlinear x^2//252')
    plt.axis('off')
    plt.imshow(img_nonlinear[..., ::-1])
    plt.show()
