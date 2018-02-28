# -*- coding: utf-8 -*-

import numpy as nm
import sklearn.preprocessing as sp


# 加载矩阵数据
def loadData(file="machine_learning_in_action/data/testSet.txt"):
    fr = open(file)
    dataArray = []
    for line in fr.readlines():
        lineArray = line.strip().split()
        dataArray.append([float(x) for x in lineArray])
    return nm.mat(dataArray)


# 归一化到0-1之间
def normalization(dataMat):
    return sp.MinMaxScaler().fit_transform(dataMat)


# 定义激活函数
def sigmoid(inMat):
    return 1 / (1 + nm.exp(-inMat))


# 训练模型
def train(data):
    dataMat = nm.mat(data)
    m, n = nm.shape(dataMat)
    weights = nm.ones((n, 1))
    targetVar = nm.ones((m, 1))
    alpha = float(0.0001)  # 步长
    maxIter = 10000  # 最大迭代
    minErrorSpan = float(0.000003)
    minErrorMean = float(1)
    maxOptimizeWeight = nm.zeros((n, 1))  # 最优梯度

    for k in range(maxIter):
        print("第 %d/%d 次迭代" % (k, maxIter))

        h = sigmoid(dataMat * weights)
        error = (targetVar - h)
        errorMean = error.mean()
        offset = minErrorMean - errorMean

        if (errorMean <= minErrorMean):
            print("产生最优解 curMean:%s minMean:%s curSpan:%s minSpan:%s" % (errorMean, minErrorMean, offset, minErrorSpan))
            maxOptimizeWeight = weights
            if (offset <= minErrorSpan):
                print("满足最小误差 %s <= %s" % (offset, minErrorSpan))
                return maxOptimizeWeight
            minErrorMean = errorMean

        # 上升梯度
        weights = weights + alpha * dataMat.transpose() * error

    return maxOptimizeWeight


def pred(data, weight, threshold=float(0.8)):
    dataMat = nm.mat(data)
    predResult = sigmoid(dataMat * weight)
    return predResult, predResult >= threshold


originData = loadData()
norMat = normalization(originData)
model = train(norMat)
predData, label = pred(norMat, model)

print("源数据:\n", originData)
print("归一化:\n", norMat)
print("训练结果:\n", model)
print("预测结果:\n", predData, "\nlabel:\n", label)
