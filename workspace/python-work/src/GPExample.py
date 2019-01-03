# encoding:utf-8
# 制图系统示例

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# **********生成样本数据**********

exampleDataMat1 = np.mat(np.random.uniform(1, 6, size=(5, 2)))
exampleDataMat2 = np.mat(np.random.uniform(3, 8, size=(5, 2)))

exampleDataMat1.sort(0)
exampleDataMat2.sort(0)

print("示例数据1:\n", exampleDataMat1)
print("示例数据2:\n", exampleDataMat2)

data1PlotX = exampleDataMat1[:, 0].flatten().A[0]
data1PlotY = exampleDataMat1[:, 1].flatten().A[0]

data2PlotX = exampleDataMat2[:, 0].flatten().A[0]
data2PlotY = exampleDataMat2[:, 1].flatten().A[0]

print("data1PlotX = ", data1PlotX)
print("data1PlotY = ", data1PlotY)
print("data2PlotX = ", data2PlotX)
print("data2PlotY = ", data2PlotY)

# **********绘图系统开始**********
plt.figure(figsize=(8, 20))

# 子图1
sp1 = plt.subplot(511)

# 标记图的题目,x轴,y轴,显示网格
plt.tight_layout()
plt.ylabel("Prediction")
plt.xlabel("Target")
plt.title("-1号子图+")
plt.grid(False)

# 这里b表示blue，g表示green，r表示red，-表示连接线，--表示虚线链接
sp1.plot(data1PlotX, np.sqrt(data1PlotX), 'bo', label='line1')
sp1.plot(data1PlotX, data1PlotX * 8, 'rD-', label='line2')
sp1.plot(data1PlotX, data1PlotX * 2, 'ch-', label='line3')
sp1.plot(data1PlotX, data1PlotX * 3, 'mH-', label='line4')
sp1.plot(data1PlotX, data1PlotX * 4, 'g*-', label='line5')
sp1.plot(data1PlotX, data1PlotX * 5, 'y8--', label='line6')
sp1.plot(data1PlotX, data1PlotX * 6, 'k^', label='line7')
sp1.plot(data1PlotX, data1PlotX * 7, 'w+-', label='line8')

# 直方图
# sp.hist(plotX)

# 散点图
sp1.scatter(data1PlotX, data1PlotY, marker='x', color='r', s=50)

# 显示图例
aliasHandles, aliasLabels = sp1.get_legend_handles_labels()
sp1.legend(aliasHandles[::-1], aliasLabels[::-1])

# 指定坐标绘制文本
sp1.text(4.5, 35, r'$\mu=0\ \Sigma=2$')

plt.tight_layout()

# *************子图2*****************
sp2 = plt.subplot(512)

plt.tight_layout()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("2号子图")
plt.grid(True)

# 绘制散点图
sp2.scatter(data1PlotX, data1PlotY, marker='x', color='b', s=50)
sp2.scatter(data2PlotX, data2PlotY, marker='o', color='r', s=50)

# 拟合曲线
sp2.plot(data2PlotY, 'g^--')

# *************子图3*****************
sp2 = plt.subplot(513)
plt.tight_layout()

# *************子图4*****************
sp2 = plt.subplot(514)
plt.tight_layout()

# *************子图5*****************
sp2 = plt.subplot(515)
plt.tight_layout()

plt.show()
plt.close()
