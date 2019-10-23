'''读取一幅图像，进行哈弗曼编码/解码'''
import os
import cv2
import numpy as np


class node:
    # 构造用以表示节点的类
    def __init__(self, right=None, left=None, parent=None, weight=0,
                 code=None):  # 节点构造方法
        self.left = left
        self.right = right
        self.parent = parent
        self.weight = weight
        self.code = code


def pixel_statistics(picdata):
    # 统计每个像素出现的次数,并按从小到大排序
    # 将数组转化为列表
    picdata = np.ravel(picdata).tolist()
    dict = {}
    for key in picdata:
        dict[key] = dict.get(key, 0)+1
    pix_sta_sorted = sorted(dict.items(), key=lambda item: item[1])
    return pix_sta_sorted


def construct_leaf_nodes(xiang_su_zhi):
    """
    构造叶子节点，分别赋予其像素点的值和像素点的权重
    code = 像素点的值
    weight = 像素点的权重
    :param xiang_su_zhi:
    :return:
    """
    nodes_list = [node(weight=xiang_su_zhi[i][1], code=str(xiang_su_zhi[i][0]))
                  for i in range(len(xiang_su_zhi))]
    # print node_list.__len__()    # 256
    # print node_list[0].code, node_list[0].weight   # 255 26
    return nodes_list


def huffman_tree(listnode):
    """
    根据叶子结点列表，生成对应的霍夫曼编码树
    :param listnode:
    :return:
    """
    # listnode = sort_by_weight(listnode)

    while len(listnode) != 1:
        low_node0, low_node1 = listnode[0], listnode[1]  # 每次取最小权值的两个像素点进行合并
        new_change_node = node()
        new_change_node.weight = low_node0.weight + low_node1.weight
        new_change_node.left = low_node0
        new_change_node.right = low_node1
        low_node0.parent = new_change_node
        low_node1.parent = new_change_node
        # remove() 函数用于移除列表中某个值的第一个匹配项
        listnode.remove(low_node0)
        listnode.remove(low_node1)
        listnode.append(new_change_node)
        listnode = sorted(listnode, key=lambda node: node.weight)
    return listnode  # 返回头结点


def huffman_encode(picture):
    # 哈夫曼编码

    height, width = picture.shape
    # 统计每个像素出现的次数并排序
    pix_sta_sorted = pixel_statistics(picture)

    # 构造叶子节点
    leaf_nodes_list = construct_leaf_nodes(pix_sta_sorted)

    # 根据叶子结点列表，生成对应的霍夫曼编码树
    head = huffman_tree(leaf_nodes_list)[0]  # 保存编码树的头结点return <node instance>

    # TODO:huffman 编码规则的正确性，不同角度去理解
    global bian_ma_biao
    # 遍历所有的叶子节点进行编码
    for e in leaf_nodes_list:  # 构造编码表
        new_change_node = e
        bian_ma_biao.setdefault(e.code, "")
        while new_change_node != head:
            if new_change_node.parent.left == new_change_node:
                bian_ma_biao[e.code] = "1" + bian_ma_biao[e.code]
            else:
                bian_ma_biao[e.code] = "0" + bian_ma_biao[e.code]
            new_change_node = new_change_node.parent
    for key in bian_ma_biao.keys():
        print("信源像素点 {0} Huffman编码后的码字为： {1}".format(key, bian_ma_biao[key]))
    result = ''  # 编码结果，对每个像素点进行霍夫曼编码
    for i in range(width):
        for j in range(height):
            for key, values in bian_ma_biao.iteritems():
                if str(im[i, j]) == key:
                    result = result + values
    with open('result.txt', 'w') as f:
        f.write(result)
    print("您的编码表为:", bian_ma_biao)


if __name__ == "__main__":
    model_path = os.path.dirname(__file__)
    img = cv2.imread(model_path + '/example.png', flags=0)
    # print(img.shape)
    # cv2.imshow("123",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # print(pixel_statistics(img))
    huffman_encode(img)
