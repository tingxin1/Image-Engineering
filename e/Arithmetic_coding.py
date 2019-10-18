# -*- coding: UTF-8 -*-
'''
使用算数编码对图像进行编码和解码
'''
import os
import cv2
import numpy as np
from decimal import Decimal
from decimal import localcontext

# def encode(picdata):
#     dict = {}
#     for key in picdata:
#         dict[key] = dict.get(key, 0)+1
#     sorted_key = sorted(dict.keys())
#     # print(dict[sorted_key[0]])

#     # 计算概率值
#     suma = 0
#     for i in range(len(dict)):
#         suma += dict[sorted_key[i]]
#         dict[sorted_key[i]] = suma/len(picdata)
#     # print(sorted(dict.items(), key=lambda obj: obj[0]))
#     result = []
#     for i in picdata:


def zoom(low, high):
    exlist = []
    while(low//0.1 == high//0.1):
        exlist.append(low//0.1)
        low = low*10-low//0.1
        high = high*10-high//0.1
    return low, high, exlist


if __name__ == "__main__":
    # model_path = os.path.dirname(__file__)
    # img = cv2.imread(model_path+'/example.png', flags=0)

    # imgdata = np.ravel(img).tolist()
    # encode(imgdata)
    # print(imgdata)
    # cv2.imshow('123', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    a, b, c = zoom(Decimal('0.12345'), Decimal('0.12356'))
    print(a, "\n\n", b, "\n\n", c)
