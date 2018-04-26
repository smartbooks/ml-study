# encoding:utf-8
# 线性回归:标准线性回归&局部加权线性回归

import numpy as nm
import matplotlib.pyplot as plt

dataMat = nm.mat([
    [0.478, 0.827],
    [0.512, 0.871],
    [0.919, 0.790],
    [0.859, 0.059],
    [0.675, 0.252],
    [0.741, 0.971],
    [0.491, 0.430],
    [0.153, 0.624],
    [0.560, 0.360],
    [0.485, 0.324]])

sortDataMat = dataMat.copy()
sortDataMat.sort(0)

# 全1矩阵
labelOneMat = nm.ones((sortDataMat.shape[0], 1))


# 全0矩阵
# labelZeroMat = nm.zeros((sortDataMat.shape[0], 1), dtype=nm.int)

# 单位矩阵
# eyeMat = nm.eye(sortDataMat.shape[1])


# 损失函数
def lrLoss(yMat, yHatMat, showPlot=False):
    e = yMat - yHatMat
    eSquare = nm.square(e)
    eSquareSum = nm.sum(nm.square(e))
    print("预测:\n", yHatMat)
    print("残差:\n", e)
    print("残差平方:\n", eSquare)
    print("残差平方和:", eSquareSum)

    if showPlot == True:
        x = sortDataMat[:, 0].flatten().A[0]
        y = sortDataMat[:, 1].flatten().A[0]

        print("x =", x)
        print("y =", y)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(x, y)

        yLab = sortDataMat[:, 0].flatten().A[0]
        yHat = yHatMat[:, 0].flatten().A[0]

        print("yLab = ", yLab)
        print("yHat = ", yHat)

        ax.plot(yHat, yLab)
        plt.show()


# 标准线性回归
def standRegres(xMat, yMat):
    xTx = xMat.T * xMat
    if nm.linalg.det(xTx) == 0.0:
        return
    # return xTx.I * (xMat.T * yMat)
    return nm.linalg.solve(xTx, xMat.T * yMat)


# 局部加权线性回归
def lwlr(testPoint, xMat, yMat, k=1.0):
    m = xMat.shape[0]
    weights = nm.mat(nm.eye((m)))

    # 高斯核函数权重衰减
    for j in range(m):
        diffMat = testPoint - xMat[j, :]
        weights[j, j] = nm.exp(diffMat * diffMat.T / (-2.0 * k ** 2))

    xTx = xMat.T * (weights * xMat)
    if nm.linalg.det(xTx) == 0.0:
        return

    ws = xTx.I * (xMat.T * (weights * yMat))

    return testPoint * ws


def lwlrTest(xMat, yMat, k=1.0):
    m = nm.shape(xMat)[0]
    yHat = nm.zeros(m)
    for i in range(m):
        yHat[i] = lwlr(xMat[i, :], xMat, yMat, k)
    return yHat


def test1():
    print("**********标准线性回归**********")
    ws = standRegres(sortDataMat, labelOneMat)
    y = sortDataMat * ws
    print("权重:\n", ws)
    lrLoss(labelOneMat, y, True)


def test2():
    print("**********局部加权线性回归**********")
    y = lwlrTest(sortDataMat, labelOneMat, 0.33)
    lrLoss(labelOneMat.T, y)


print("数据:\n", sortDataMat)
print("标签:\n", labelOneMat)

test1()
# test2()
