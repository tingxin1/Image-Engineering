# Image-Engineering
- [Image-Engineering](#image-engineering)
  - [a.py](#apy)
  - [b.py](#bpy)
  - [c.py](#cpy)
  - [遇到的问题](#%e9%81%87%e5%88%b0%e7%9a%84%e9%97%ae%e9%a2%98)
    - [关于openCV](#%e5%85%b3%e4%ba%8eopencv)
    - [关于matplotlab](#%e5%85%b3%e4%ba%8ematplotlab)
## a.py

**要求：打开一BMP文件，将其转存为RGB三通道图像;将图像量化为0.5/0.25灰度范围的图像**

使用openCV打开BMP文件，读取的直接就是RGB三通道的图像（opencv的三通道顺序为BGR）。

之后使用了两种方法将图像灰度化，一种是openCV的内置方法cvtColor，另一种是根据公式gray=0.299×R+0.587×G+0.114×B进项计算。得到灰度图之后，将灰度图量化到了0.25~0.5范围内。

## b.py

**要求：生成图像文件，要求颜色等阶渐变，观察人眼最小分辨率**

使用一个三维矩阵[400, 700, 3]直接生成一幅图像，通过调整RGB三个通道的灰度值来达到色彩渐变的效果。

一共四个条带，从左到右分别为灰度渐变、灰度等阶变化、彩色渐变、彩色等阶变化。

渐变的条带每1行为一个灰度值，等阶的条带每32行为一个灰度值，相邻两阶之间灰度值差32

## c.py

**要求**：
- **图像减法**
- **利用乘法、与、或实现特定多边形区域显示**
  - **设定循环，显示动画，生成视频**
  - **望远镜显示特效**
  - **不同的色彩通道显示（红外夜视模式）**

1. 图像减法
   
   opencv里规定RGB通道的上限为255，下限为0，超过255或小于0的数全变成255和0，所以图像的算术运算不能直接使用下面的语句：

    ```
    img=img1-img2
    img=img1+img2
    ```
    因为这两条语句会使灰度值“越界”，超过255值会从0循环，负数的值则从255开始循环。比如300会变成300-255=45。

    所以在减法中要手动判断差是否越界（小于0），如果是，对应为是就应该设为0.
2. 

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
