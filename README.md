# Image-Engineering
- [Image-Engineering](#image-engineering)
  - [a/a.py](#aapy)
  - [b.py](#bpy)
  - [c](#c)
    - [img_subtract.py](#imgsubtractpy)
    - [telescope.py](#telescopepy)
  - [d](#d)
    - [non-linear.py](#non-linearpy)
    - [effect.py](#effectpy)
    - [histogram_equalization.py](#histogramequalizationpy)
  - [遇到的问题](#%e9%81%87%e5%88%b0%e7%9a%84%e9%97%ae%e9%a2%98)
    - [关于openCV](#%e5%85%b3%e4%ba%8eopencv)
    - [关于matplotlab](#%e5%85%b3%e4%ba%8ematplotlab)
## a/a.py

**要求：打开一BMP文件，将其转存为RGB三通道图像;将图像量化为0.5/0.25灰度范围的图像**

使用openCV打开BMP文件，读取的直接就是RGB三通道的图像（opencv的三通道顺序为BGR）。

之后使用了两种方法将图像灰度化，一种是openCV的内置方法cvtColor，另一种是根据公式gray=0.299×R+0.587×G+0.114×B进项计算。得到灰度图之后，将灰度图量化到了0.25~0.5范围内。

## b.py

**要求：生成图像文件，要求颜色等阶渐变，观察人眼最小分辨率**

使用一个三维矩阵[400, 700, 3]直接生成一幅图像，通过循环调整RGB三个通道的灰度值来达到色彩渐变的效果，最后使用opencv中的函数将图像显示出来。

一共四个条带，从左到右分别为灰度渐变、灰度等阶变化、彩色渐变、彩色等阶变化。

渐变的条带每1行为一个灰度值，等阶的条带每32行为一个灰度值，相邻两阶之间灰度值差32

## c

**要求：**
- **图像减法**
- **利用乘法、与、或实现特定多边形区域显示**
  - **设定循环，显示动画，生成视频**
  - **望远镜显示特效**
  - **不同的色彩通道显示（红外夜视模式）**
  
### img_subtract.py

**图像减法**  

opencv里规定RGB通道的上限为255，下限为0，超过255或小于0的数全变成255和0，所以图像的算术运算不能直接使用下面的语句：

```
img=img1-img2
img=img1+img2
```
因为这两条语句会使灰度值“越界”，超过255值会从0循环，负数的值则从255开始循环。比如300会变成300-255=45。

所以在减法中要手动判断差是否越界（小于0），如果是，对应为是就应该设为0.

### telescope.py

**望远镜效果**
   
“特效”原理：

首先生成一幅包含望远镜形状的图片（两个白色的⚪部分重合，周边是黑色的。）

其次，将图片的RGB三通道中的R和B通道中的值减小（或者直接设置为零），从而营造绿色的夜视效果。

最后将两幅图片做“与”操作，从而得到望远镜特效。


使用opencv读取视频*example.mp4*，逐帧添加上述特效之后，再写入*telescope.mp4*视频中。

缺点：没有做放大特效。


## d

**要求：**
- **图像点操作（线性、非线性）**
- **实现两种图片特效**
- **直方图增强：图像点操作处理之后：**
  - **原始图像/处理后的图像/均衡化后图像的直方图比较**
  - **统计分析视觉观感与直方图的关系**
  - **指定灰度集进行直方图处理，分析不同灰度集的视觉效果**

### non-linear.py

**实现图片灰度的线性变化和非线性变化**

针对示例图片*example.png*的RGB三通道的灰度值进行线性（x/3)和非线性（x^2/200)变化，并比较与原图的差别。

### effect.py

**实现水波特效和浮雕特效**

1. 水波特效
2. 浮雕特效
   
   当前象素和它右下方象素之间的差值并加上一个常量（128），从图像左上方开始处理。

### histogram_equalization.py

## 遇到的问题

### 关于openCV

### 关于matplotlab

1. 中文显示问题
   首先需要下载中文字体，以黑体(SimHei.ttf)为例，需要将字体复制到matplotlib的字体文件夹下(例如```/home/zx/anaconda3/lib/python3.7/site-packages/matplotlib/fonts/ttf/```)使用下面两行代码可以查询文件夹位置：

    ```Python
    import matplotlib
    print (matplotlib.matplotlib_fname())
    ```
    注意：必须要复制到matplotlib的字体目录下，复制到系统的字体目录下不管用。

    接下来有两种方法：

    - 方法一

        在代码中添加下面三行代码
        ```python
        import matplotlib.pyplot as plt
        
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
        ```
        之后再有中文的地方使用**u'中文内容'**
    - 方法二

        修改/matplotlib/mpl-data/matplotlibrc文件（这个文件应该在前面查询的目录下），修改内容如下：
        ```
        font.family : sans-serif

        font.sans-serif : SimHei, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
        axes.unicode_minus:False，#作用就是解决负号'-'显示为方块的问题
        ```
        最后在Python中运行下面的代码重新加载一下字体
        ```python
        from matplotlib.font_manager import _rebuild

        _rebuild()
        ```
> 参考文章[matplotlib图例中文乱码](https://www.zhihu.com/question/25404709)
