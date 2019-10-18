'''读取一幅图像，进行哈弗曼编码/解码'''
import os
import cv2
import numpy as np


class node:
    """
    构造用以表示节点的类
    """

    def __init__(self, right=None, left=None, parent=None, weight=0,
                 code=None):  # 节点构造方法
        self.left = left
        self.right = right
        self.parent = parent
        self.weight = weight
        self.code = code


if __name__ == "__main__":
    model_path = os.path.dirname(__file__)
    img = cv2.imread(model_path+'example.png', flags=)
