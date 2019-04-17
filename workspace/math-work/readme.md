
# 数学知识

## DNN深度学习

- https://zhuanlan.zhihu.com/p/24801814
- http://galaxy.agh.edu.pl/~vlsi/AI/backp_t_en/backprop.html
- https://iamtrask.github.io/2015/07/12/basic-python-network/
- http://neuralnetworksanddeeplearning.com/chap1.html
- http://deeplearning.stanford.edu/wiki/index.php/Backpropagation_Algorithm
- http://deeplearning.stanford.edu/wiki/index.php/UFLDL%E6%95%99%E7%A8%8B
- [NG的课程]:http://cs229.stanford.edu/
- http://deeplearning.stanford.edu/tutorial/
- http://cs229.stanford.edu/proj2017/

## 梯度更新

```text

#多层神经网络JAVA版本实现(BP反向传播版):https://github.com/smartbooks/spark-example/blob/master/spark-example-base/src/test/java/com/github/smartbooks/base/bp/NeuralNetworksTest.java

e = y - h
w = w - step * a.T * e

参数备注:
w    = 权重
step = 梯度更新步子
a.T  = 特征矩阵
e    = 残差
y    = 目标
h    = 预测目标

#快速计算矩阵与向量的欧式距离
a = np.mat([[1,2,3],[4,5,6]])
w = np.mat([7,8,9])
np.linalg.norm(a[1,:]-w[0])
np.linalg.norm(a-w,axis=1)

#批量修改特征
a[:,0] = 0
```

## matrix

```text
Scalar:标量,一个单独的数.
Vector:向量,一列有序的数.
Matrix:矩阵,一个二维数组.
Tensor:张量,两维以上数组.
1d-Tensor:vector.
2d-Tensor:matrix.
3d-Tensor:cube.
4d-Tensor:vector of cubes.
5d-Tensor:matrix of cubes.
6d-Tensor:cube of cubes.


#矩阵概念
单位矩阵
矩阵的迹
对角矩阵
正定矩阵
增广矩阵
奇异值
复矩阵
阶数
矩阵的秩
病态矩阵
矩阵的逆和伪逆
奇异矩阵
协方差矩阵

```

## 矩阵类型

```text
增广矩阵:
逆矩阵:
伴随矩阵:
满秩矩阵:
关联矩阵:
初等矩阵:
实对称矩阵:
正交矩阵:
不可约矩阵:
转置矩阵:
可达矩阵:
对称矩阵:
伪逆矩阵:
列矩阵:
反对称矩阵:
矩阵式组织结构:
```

## 矩阵变换

- Translation:平移
- Rotation:旋转
- Scaling:缩放
