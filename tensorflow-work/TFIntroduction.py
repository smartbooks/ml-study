# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

# GPU配置
config = tf.ConfigProto()
# 自动选择现有的受支持设备
config.allow_soft_placement = True
# 显示指令和张量被分配到哪个设备
config.log_device_placement = True
# 根据运行时的需要来分配 GPU 内存
config.gpu_options.allow_growth = True
# 每个可见 GPU 应分配到的内存占总内存量的比例
config.gpu_options.per_process_gpu_memory_fraction = 0.4


def testCpuLog():
    """
    a分配到cpu:0执行
    b分配到cpu:0执行
    c分配到gpu:0执行
    d由于未明确执行运行设备,优先使用Gpu:0执行

    运行输出:
    c: (MatMul): /job:localhost/replica:0/task:0/device:GPU:0
    d: (Pow): /job:localhost/replica:0/task:0/device:GPU:0
    b: (Const): /job:localhost/replica:0/task:0/device:CPU:0
    a: (Const): /job:localhost/replica:0/task:0/device:CPU:0

    :return:
    """
    with tf.device("/cpu:0"):
        a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')

    with tf.device("/cpu:0"):
        b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')

    with tf.device("/gpu:0"):
        c = tf.matmul(a, b, name="c")

    d = tf.pow(x=c, y=c, name="d")

    sess = tf.Session(config=config)

    print("c:", sess.run(c))
    print("d:", sess.run(d))


def testGpuLog():
    """
    测试Gpu设备执行日志,默认优选使用Gpu
    :return:
    """
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)

    sess = tf.Session(config=config)

    print(sess.run(c))


# testGpuLog()
testCpuLog()
