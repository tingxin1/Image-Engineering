# -*- coding: utf-8 -*-
import os
import cv2
import numpy
import pickle
import sys
from PIL import Image

class node():
    def __init__(self, right=None, left=None, parent=None, weight=0, code=None, length=0):
        self.left = left
        self.right = right
        self.parent = parent
        self.weight = weight
        self.code = code
        self.length = length


def pixelStat(listP):
    static = {}
    for i in listP:
        if i not in static.keys():
            static[i] = 1
        else:
            static[i] += 1
    return static


def buildTree(pic):
    width, height = pic.shape
    listP = [pic[i][j] for i in range(width) for j in range(height)]
    freq = pixelStat(listP)
    freq = sorted(freq.items(), key=lambda x: x[1])
    # print(freq)
    global nodeList
    nodeList = [node(weight=freq[i][1], code=freq[i][0])
                for i in range(len(freq))]
    nodeListC = nodeList
    while(len(nodeList) != 1):
        newNode = node()
        node1, node2 = nodeList[0], nodeList[1]
        newNode.weight = node1.weight + node2.weight
        newNode.left = node1
        newNode.right = node2
        node1.parent = newNode
        node2.parent = newNode
        nodeList.remove(node1)
        nodeList.remove(node2)
        nodeList.append(newNode)
        nodeList = sorted(nodeList, key=lambda x: x.weight)
    # print(len(nodeList))
    root = nodeList[0]
    # print(freq)
    codeTable = {}
    for e in nodeListC:
        nowNode = e
        codeTable.setdefault(e.code, '')
        while(nowNode != root):
            if nowNode.parent.left == nowNode:
                codeTable[e.code] = "1" + codeTable[e.code]
                e.length += 1
            else:
                codeTable[e.code] = "0" + codeTable[e.code]
                e.length += 1
            nowNode = nowNode.parent
    # print(codeTable)
    k = 0
    result = ''
    for i in range(width):
        for j in range(height):
            for key, value in codeTable.items():
                # print(type(key))
                # print(pic[i][j],key)
                if pic[i][j] == key:
                    # print(pic[i][j],key)
                    # print(1)
                    result = result + value
                    k += 1

    with open('result.txt', 'w') as f:
        f.write(result)
    f.close()
    with open('codeTable.pkl', 'wb') as f:
        pickle.dump(codeTable, f)
    with open('eNumber.txt', 'w') as f1:
        f1.write(str(k))
    f1.close

    # 计算平均编码长度
    avrLength = 0
    all = width*height
    for e in nodeListC:
        # print(e.length,e.weight,all)
        avrLength += e.length * e.weight / all
    print("平均编码长度为：", avrLength)
    return k, codeTable
    # print(codeTable)
    # print(root.code,codeTable[root.code],root.weight)


def recover(width, height, eN):
    with open('result.txt', 'r') as p:
        zifuchuan = p.readlines()[0].strip('\n')
    # print(width,height)
    with open('codeTable.pkl', 'rb+') as codeTable1:
        codeTable = pickle.load(codeTable1, encoding='UTF-8')
    # print(codeTable)
    i = 0
    Sao_miao = ''
    Huan_yuan_xiang_su = []
    while i != zifuchuan.__len__():  # Decode using the encoding table
        Sao_miao = Sao_miao + zifuchuan[i]
        for key in codeTable.keys():
            if Sao_miao == codeTable[key]:
                Huan_yuan_xiang_su.append(key)
                Sao_miao = ''
                break
        i += 1
    # print(len(Huan_yuan_xiang_su))
    y = width
    x = height
    c = Image.new('L', (x, y))
    k = 0
    for i in range(x):
        for j in range(y):
            c.putpixel((j, i), (int(Huan_yuan_xiang_su[k])))
            k += 1
            if k == eN:
                break
    c.save('huffman_restore_photo' + '.bmp')
    print("Your decoding is complete:" +
          "The image is stored as huffman_restore_photo.bmp")


if __name__ == '__main__':
    pic = cv2.imread(os.path.dirname(__file__) + "/example.png", flags=0)
    width, height = pic.shape
    eNumber, codeTable = buildTree(pic)
    print("Your encoding is complete")
    width =130
    height =130 
    with open('eNumber.txt', 'r') as p:
        zifuchuan = p.readlines()[0].strip('\n')
    eNumber = int(zifuchuan)
    recover(width, height, eNumber)
