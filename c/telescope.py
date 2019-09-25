# -*- coding: UTF-8 -*-
# 要求： 利用乘法、与、或实现特定多边形区域显示
#           设定循环，显示动画，生成视频
#           望远镜显示特效
#           不同的色彩通道显示（红外夜视模式）
import os
import cv2
import numpy as np 

telescope = np.zeros((900,1440,3),dtype='uint8')
telescope.fill(255)
cv2.circle(telescope,(425,450),400,(0,0,0),-1)
cv2.circle(telescope,(1025,450),400,(0,0,0),-1)
# cv2.imshow("Circle",telescope)
# cv2.waitKey(0)

model_path=os.path.dirname(__file__)
c2=cv2.imread(model_path+'/c2.jpg')
c2[:,:,0].fill(0)
c2[:,:,2].fill(0)
# print(c2.shape)
img=cv2.add(telescope,c2)
cv2.namedWindow("c2",cv2.WINDOW_NORMAL)
cv2.imshow("c2",img)
cv2.waitKey(0)