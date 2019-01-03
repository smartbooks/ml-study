# encoding:utf-8
# 线性回归:标准线性回归&局部加权线性回归

import numpy as nm
import matplotlib.pyplot as plt

rowCount = 1000

dataMat = nm.mat(nm.random.uniform(0, 1, size=(rowCount, 1)))
dataMat.sort(0)
labelOneMat = nm.mat(nm.random.uniform(0, 1, size=(rowCount, 1)))


# 损失函数
def lrLoss(yMat, yHatMat, showPlot=False):
    e = yMat - yHatMat
    eSquare = nm.square(e)
    eSquareSum = nm.sum(nm.square(e))
    # print("Y:\n", yMat)
    # print("预测:\n", yHatMat)
    # print("残差:\n", e)
    # print("残差平方:\n", eSquare)
    print("残差平方和:", eSquareSum)

    if showPlot == True:
        # 散点图
        scatterPointX = nm.arange(0, 1, 1 / labelOneMat.shape[0])
        scatterPointY = labelOneMat[:, 0].flatten().A[0]
        plt.scatter(x=scatterPointX, y=scatterPointY, c='b', marker='x', s=20)

        # 曲线图
        plotPoint = yHatMat[:, 0].flatten().A[0]
        plt.plot(scatterPointX, plotPoint, 'r--')

        # 目标点与观测点之间连线
        """
        ax = plt.axes()
        for i in range(len(scatterPointX)):
            ax.arrow(scatterPointX[i], plotPoint[i],
                     scatterPointX[i], scatterPointY[i],
                     head_width=0.05,
                     head_length=0.2,
                     fc='g',
                     ec='b',
                     length_includes_head=True)
        """

        plt.ylabel("Prediction")
        plt.xlabel("Simple")
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
    ws = standRegres(dataMat, labelOneMat)
    y = dataMat * ws
    print("权重:\n", ws)
    lrLoss(labelOneMat, y, True)


def test2():
    print("**********局部加权线性回归**********")
    y = lwlrTest(dataMat, labelOneMat, 0.33)
    lrLoss(labelOneMat, y, True)


# print("数据:\n", dataMat)
# print("标签:\n", labelOneMat)

test1()
test2()
