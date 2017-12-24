# -*- coding: utf-8 -*-

# 代数库包
import numpy as np

# 机器学些库
import tensorflow as tf

# 图形库
import matplotlib.pyplot as plt
# 图形库显示中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

print(tf.__version__)
print(tf.__path__)
print("你好")

# 代数库示例
x = np.arange(20)
y = np.sin(x)
z = np.cos(x)

# marker数据点样式，linewidth线宽，linestyle线型样式，color颜色
plt.plot(x, y, marker="*", linewidth=3, linestyle="--", color="orange")
plt.plot(x, z)
plt.title("matplotlib +6的飞起")
plt.xlabel("高")
plt.ylabel("宽")

# 图形库绘图示例
plt.legend(["Y", "Z"], loc="upper right")
plt.grid(True)
plt.show()
