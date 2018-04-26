# encoding:utf-8
# 线性回归:标准线性回归&局部加权线性回归

import numpy as nm
import matplotlib.pyplot as plt

dataMat = nm.mat(nm.random.uniform(1, 6, size=(10, 2)))
dataMat2 = nm.mat(nm.random.uniform(3, 8, size=(10, 2)))

sortDataMat = dataMat.copy()
sortDataMat.sort(0)

# 全1矩阵
labelOneMat = nm.mat(nm.ones((sortDataMat.shape[0], 1)))


# 损失函数
def lrLoss(yMat, yHatMat, showPlot=False, ws=None):
    e = yMat - yHatMat
    eSquare = nm.square(e)
    eSquareSum = nm.sum(nm.square(e))
    # print("Y:\n", yMat)
    # print("预测:\n", yHatMat)
    # print("残差:\n", e)
    # print("残差平方:\n", eSquare)
    print("残差平方和:", eSquareSum)

    if showPlot == True and ws is not None:
        x = sortDataMat[:, 0].flatten().A[0]
        y = sortDataMat[:, 1].flatten().A[0]
        # print("x =", x)
        # print("y =", y)

        plt.scatter(x, y, c='b', marker='x', s=50)

        plotX = nm.arange(-5, 5, 0.1)
        plotY = (-ws[0] - ws[1] * plotX) / ws[2]

        # plotX = labelOneMat[:, 0].flatten().A[0]
        plotY = yHatMat[:, 0].flatten().A[0]
        # plotX = sortDataMat[:, 0].flatten().A[0]
        # plotY = yHatMat[:, 0].flatten().A[0]
        print("plotX = ", plotX)
        print("plotY = ", plotY)

        plt.plot(plotX, plotY)

        plt.ylabel("Prediction")
        plt.xlabel("Target")
        plt.show()


# 标准线性回归
def standRegres(xMat, yMat):
    xTx = xMat.T * xMat
    if nm.linalg.det(xTx) == 0.0:
        return
    return xTx.I * (xMat.T * yMat)
    # return nm.linalg.solve(xTx, xMat.T * yMat)


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
    yHat = nm.mat(nm.zeros((m, 1)))
    for i in range(m):
        yHat[i, 0] = lwlr(xMat[i, :], xMat, yMat, k)
    return yHat


def test1():
    print("**********标准线性回归**********")
    ws = standRegres(sortDataMat, labelOneMat)
    y = sortDataMat * ws
    print("权重:\n", ws)
    lrLoss(labelOneMat, y, True, ws)


def test2():
    print("**********局部加权线性回归**********")
    y = lwlrTest(sortDataMat, labelOneMat, 0.33)
    lrLoss(labelOneMat, y, True)


print("数据:\n", sortDataMat)
# print("标签:\n", labelOneMat)

test1()
# test2()
