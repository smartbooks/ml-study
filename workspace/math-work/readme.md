
# 数学知识

### DNN深度学习
- https://zhuanlan.zhihu.com/p/24801814
- http://galaxy.agh.edu.pl/~vlsi/AI/backp_t_en/backprop.html
- https://iamtrask.github.io/2015/07/12/basic-python-network/
- http://neuralnetworksanddeeplearning.com/chap1.html
- http://deeplearning.stanford.edu/wiki/index.php/Backpropagation_Algorithm
- http://deeplearning.stanford.edu/wiki/index.php/UFLDL%E6%95%99%E7%A8%8B
- [NG的课程]:http://cs229.stanford.edu/
- http://deeplearning.stanford.edu/tutorial/
- http://cs229.stanford.edu/proj2017/

### 梯度更新
```

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