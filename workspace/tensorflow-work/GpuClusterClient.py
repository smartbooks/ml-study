# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

train_X = np.linspace(-1, 1, 101)
train_Y = 2 * train_X + np.random.rand(*train_X.shape) * 0.33 + 10

X = tf.placeholder("float")
Y = tf.placeholder("float")
W = tf.Variable(0.0, name="weight")
B = tf.Variable(0.0, name="reminder")

init_op = tf.global_variables_initializer()
cost_op = tf.square(Y - tf.multiply(X, W) - B)
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost_op)

with tf.Session("grpc://localhost:2222") as sess:
    with tf.device("/job:workerr/task:0"):
        sess.run(init_op)

        for i in range(1000):
            print(i)
            for (x, y) in zip(train_X, train_Y):
                sess.run(train_op, feed_dict={X: x, Y: y})

        print(sess.run(W))
        print(sess.run(B))
