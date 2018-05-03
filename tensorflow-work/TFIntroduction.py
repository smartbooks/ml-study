# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf


def testLog():
    """

    :return:
    """
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    print(sess.run(c))


testLog()
