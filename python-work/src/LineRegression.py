# encoding:utf-8
# 线性回归:标准线性回归&局部加权线性回归

import numpy as nm
import matplotlib.pyplot as plt

dataMat = nm.mat(nm.random.uniform(0, 10, size=(50, 2)))

sortDataMat = dataMat.copy()
sortDataMat.sort(0)

# 全1矩阵
labelOneMat = nm.ones((sortDataMat.shape[0], 1))


# 损失函数
def lrLoss(yMat, yHatMat, showPlot=False):
    e = yMat - yHatMat
    eSquare = nm.square(e)
    eSquareSum = nm.sum(nm.square(e))
    print("Y:\n", yMat)
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
    lrLoss(labelOneMat, y, True)


def test2():
    print("**********局部加权线性回归**********")
    y = lwlrTest(sortDataMat, labelOneMat, 0.33)
    lrLoss(labelOneMat, y, True)


print("数据:\n", sortDataMat)
print("标签:\n", labelOneMat)

test1()
test2()
