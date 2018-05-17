
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

x=2; w=0; b=1; z=0.5;

while {
  s = sigmoid(x * w + b)    //s返回区间[0,1]
  #e = 1 - (s / z)          //未使用sigmoid函数采用
	e = z - s                 //梯度目标差
  w += e                    //梯度自动上升或下降
  print w,e
}

参数备注:
+e: 梯度上升
-e: 梯度下降
z : 目标阈值,通过w参数来控制
b : 调控w为0情况,合理调控该参数可以明显的缩短迭代次数
w : 一般默认为1,也可以给个0.00001,通过合理参数控制可以减少迭代次数
```