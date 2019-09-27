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


def night_vision(image):
    # 制造夜视效果，绿色通道不变，蓝色、红色通道减半
    image[:,:,0]=image[:,:,0]//2
    image[:,:,2]=image[:,:,2]//2
    return image


if __name__ == "__main__":
    model_path = os.path.dirname(__file__)
    # 输入视频
    cap = cv2.VideoCapture(model_path + '/example.mp4')
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_high = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 输出视频
    video_out = model_path + '/telescope.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(video_out, fourcc, 25.0, (video_width, video_high))
    # 望远镜图片
    telescope = gen_polygon(video_high, video_width)
    while (cap.isOpened()):
        rat, frame = cap.read()
        # 判断视频是否结束
        if not rat:
            break
        frame_new = cv2.add(telescope, night_vision(frame))
        cv2.imshow("processed", frame_new)
        out.write(frame_new)
        cv2.waitKey(50)
    cap.release()
    out.release()
    cv2.destroyAllWindows()
