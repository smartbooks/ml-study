# -*- coding: utf-8 -*-

import tensorflow.examples.tutorials.mnist.input_data as mn
import tensorflow as tf

# 加载数据
mnist = mn.read_data_sets("C:/test/MNIST", one_hot=True)

# 声明变量
x = tf.placeholder("float", [None, 784])
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 拟合算法
y = tf.nn.softmax(tf.matmul(x, w) + b)
y_ = tf.placeholder("float", [None, 10])

# 交叉熵
cross_entropy = - tf.reduce_sum(y_ * tf.log(y))

# 梯度下降迭代
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 初始化
init = tf.initialize_all_variables()

# 创建Session
with tf.Session() as session:
    session.run(init)
    for i in range(1000):
        # 随机梯度下降
        batch_xs, batch_ys = mnist.train.next_batch(100)
        # 迭代一次
        session.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        # 交叉预测
        correct_prediction = tf.equal(tf.arg_max(y, 1), tf.arg_max(y_, 1))
        # 均方误差
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
        # 打印准确率
        print(session.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

# 关闭it
session.close()
