# -*- coding: UTF-8 -*-
'''
使用算数编码对图像进行编码和解码
'''
import os
import cv2
import numpy as np
from decimal import *
from decimal import localcontext


def encode(picdata):
    dict = {}
    for key in picdata:
        dict[key] = dict.get(key, 0)+1
    sorted_key = sorted(dict.keys())
    # print(dict[sorted_key[0]])

    # 计算概率值
    suma = 0
    for i in range(len(dict)):
        suma += dict[sorted_key[i]]
        dict[sorted_key[i]] = suma/len(picdata)
    # 保存字典
    f = open('temp.txt', 'w')
    f.write(str(dict))
    f.close()
    # print(sorted(dict.items(), key=lambda obj: obj[0]))

    result = []
    low = 0
    high = 1
    for i in picdata:
        if i != 0:
            L = Decimal(dict.get(i-1, 0))
        else:
            L = 0
        H = Decimal(dict.get(i, 0))
        # 更新low和high
        low = low+(high-low)*L
        high = low+(high-low)*H
        # 缩放
        low, high, ex = zoom(low, high)
        result = result+ex
    s = ''
    for i in result:
        s += str(i)
    # print(s)
    return s


def zoom(low, high):
    exlist = []
    while(low*10//1 == high*10//1):
        exlist.append(low*10//1)
        low = low*10-low*10//1
        high = high*10-high*10//1
    return low, high, exlist


def decode(string):
    f = open('temp.txt', 'r')
    a = f.read()
    dict = eval(a)
    f.close()

    s = "0."+string
    # print((len(s)))
    getcontext().prec = len(s)
    pdata = Decimal(s)
    low = Decimal('0')
    high = Decimal('1')
    arr = []
    while(1):
        for i in range(256):
            H = Decimal(dict.get(i, 0))
            tmp = low+(high-low)*H
            if(pdata < tmp):
                high = tmp
                L = Decimal(dict.get(i-1, 0))
                low = low+(high-low)*L
                print(i)
                arr.append(i)
                break
        # print(len(arr))
        if(len(arr) == 8000):
            pic = np.array(arr)
            pic = np.reshape(pic, (100, -1)).astype(np.uint8)
            print(pic)
            cv2.imshow("123", pic)
            cv2.waitKey(0)
            break


if __name__ == "__main__":
    model_path = os.path.dirname(__file__)
    img = cv2.imread(model_path+'/example.png', flags=0)
    cv2.imshow('123', img)
    cv2.waitKey(0)
    imgdata = np.ravel(img).tolist()
    sdata = encode(imgdata)
    f = open('str.txt', 'w')
    f.write(sdata)
    f.close()
    f = open('str.txt', 'r')
    sdata = f.read()
    decode(sdata)
    # print(imgdata)
    # cv2.imshow('123', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # a, b, c = zoom(Decimal('0.12345'), Decimal('0.12356'))
    # print(a, "\n\n", b, "\n\n", c)
    # print(Decimal('0.12345')*Decimal('0.1'))
