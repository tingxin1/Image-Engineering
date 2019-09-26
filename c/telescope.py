# -*- coding: UTF-8 -*-
# 要求： 利用乘法、与、或实现特定多边形区域显示
#           设定循环，显示动画，生成视频
#           望远镜显示特效
#           不同的色彩通道显示（红外夜视模式）
import os
import cv2
import numpy as np


def gen_polygon(high, width):
    # 生成望远镜形状的图片
    telescope = np.zeros((high, width, 3), dtype='uint8')
    telescope.fill(255)
    hi = high // 2
    wi = width // 2
    radius = min(hi, 3*width//10)
    cv2.circle(telescope, (wi-2*radius//3, hi), radius, (0, 0, 0), -1)
    cv2.circle(telescope, (wi+2*radius//3, hi), radius, (0, 0, 0), -1)
    # cv2.imshow("Circle",telescope)
    # cv2.waitKey(0)
    return telescope


def green_channel(image):
    # 只显示RGB图片中的G通道
    image[:, :, 0].fill(0)
    image[:, :, 2].fill(0)
    return image


if __name__ == "__main__":
    model_path = os.path.dirname(__file__)
    # 输入视频
    cap = cv2.VideoCapture(model_path + '/example.mp4')
    # 输出视频
    video_out = model_path + '/telescope.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(video_out, fourcc, 25.0, (852, 480))
    # 望远镜图片
    telescope = gen_polygon(480, 852)
    while (cap.isOpened()):
        rat, frame = cap.read()
        # 判断视频是否结束
        if not rat:
            break
        frame_new = cv2.add(telescope, green_channel(frame))
        cv2.imshow("processed", frame_new)
        out.write(frame_new)
        cv2.waitKey(50)
    cap.release()
    # out.release()
    cv2.destroyAllWindows()
