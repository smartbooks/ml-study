import numpy as nm


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open("data/testSet.txt")
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1 + nm.exp(-inX))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = nm.mat(dataMatIn)
    labelMat = nm.mat(classLabels).transpose()
    m, n = nm.shape(dataMatrix)
    alpha = 0.001
    maxCycles = 5
    weights = nm.ones((n, 1))

    print("dataMatrix:\n", dataMatrix, "\nlabelMat:\n", labelMat)
    print("m:", m, "n:", n, "alpha:", alpha, "maxCycles:", maxCycles, "\nweights:\n", weights)

    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error
        print("iter:", k, "\nh:\n", h, "\nerror:\n", error, "\nweights:\n", weights)

    return weights


dataMat, labelMat = loadDataSet()
w = gradAscent(dataMat, labelMat)

print("result:\ndataMat:", dataMat, "\nlabelMat:", labelMat, "\nw:\n", w)
