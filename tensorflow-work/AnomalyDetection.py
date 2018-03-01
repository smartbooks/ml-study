# -*- coding: utf-8 -*-

import numpy as nm
import sklearn.preprocessing as sp


class ad:

    def __init__(self, maxIter=1000000, alpha=float(0.0001), minErrorSpan=float(0.000005), minErrorMean=float(1),
                 threshold=float(0.875)):
        self.maxIter = maxIter  # 最大迭代次数
        self.alpha = alpha  # 递增步长
        self.minErrorSpan = minErrorSpan  # 最小误差步长
        self.minErrorMean = minErrorMean  # 最小误差
        self.threshold = threshold  # 阈值

    def printParam(self):
        print("\n当前模型迭代参数:")
        print("maxIter:", self.maxIter)
        print("alpha:", self.alpha)
        print("threshold:", self.threshold)
        print("minErrorMean:", self.minErrorMean)
        print("minErrorSpan:", self.minErrorSpan)

    # 加载矩阵数据
    def loadData(self, file="machine_learning_in_action/data/testSet.txt"):
        fr = open(file)
        dataArray = []
        for line in fr.readlines():
            lineArray = line.strip().split()
            dataArray.append([float(x) for x in lineArray])
        return nm.mat(dataArray)

    def loadData2(self, file="C:/test/userinfo_train.csv", filter=False):
        fr = open(file)
        dataArray = []
        telArray = []
        for line in fr.readlines():
            # cf1_REG_PHONE_STD
            # cf1_ETL_30DAY_NUM
            # cf1_ETL_PV_NUM
            # cf1_ETL_STARTUP_NUM
            # cf1_KQMM_DOWNREPORT
            # cf1_KQMM_SOFTDOWN
            # cf1_ETL_USE_TIME
            lineArray = line.strip().split()
            numArray = [float(x) for x in lineArray[1:]]
            if (filter):
                if (numArray[0] < 1 and numArray[1] < 2 and numArray[2] < 1 and numArray[5] < 5):
                    dataArray.append(numArray)
            else:
                dataArray.append(numArray)
                telArray.append([int(float(x)) for x in lineArray[0:1]])
        return nm.mat(dataArray), nm.mat(telArray)

    # 归一化
    def normalization(self, dataMat):
        return sp.MinMaxScaler().fit_transform(dataMat)
        # return sp.scale(dataMat)

    # 定义激活函数
    def sigmoid(self, inMat):
        return 1 / (1 + nm.exp(-inMat))

    # 训练模型-梯度上升
    def train(self, data):
        dataMat = nm.mat(data)  # 数组转矩阵
        m, n = nm.shape(dataMat)  # 矩阵大小
        weights = nm.zeros((n, 1))  # 初始权重
        maxOptimizeWeight = nm.zeros((n, 1))  # 最优权重
        targetVar = nm.ones((m, 1))  # SUM目标和

        for k in range(self.maxIter):
            print("\n==========第 %d/%d 次迭代==========" % (k, self.maxIter))

            h = self.sigmoid(dataMat * weights)
            error = targetVar - h

            errorMean = error.mean()
            offset = self.minErrorMean - errorMean

            print("Sigmoid:\n", h)
            print("权重:\n", weights)
            print("误差:\n", error, "\n本次误差均值:", errorMean, "\n两次均值误差:", offset, "\n全局最小误差:",
                  self.minErrorMean, "\n最小误差步长:", self.minErrorSpan)

            if (errorMean <= self.minErrorMean):
                print("产生新的最小误差:", errorMean)
                maxOptimizeWeight = weights

                if (offset <= self.minErrorSpan):
                    print("最小误差步长终止 %s(当前误差步长) <= %s(最小误差步长)" % (offset, self.minErrorSpan))
                    return maxOptimizeWeight

                self.minErrorMean = errorMean

            # 上升梯度
            weights = weights + self.alpha * dataMat.transpose() * error

        print("最大迭代次数终止:%s" % (self.maxIter))
        return maxOptimizeWeight

    # 预测样本
    def pred(self, data, weight):
        dataMat = nm.mat(data)
        predResult = self.sigmoid(dataMat * weight)
        return predResult, predResult >= self.threshold


# cf1_ETL_30DAY_NUM
# cf1_ETL_PV_NUM
# cf1_ETL_STARTUP_NUM
# cf1_KQMM_DOWNREPORT
# cf1_KQMM_SOFTDOWN
# cf1_ETL_USE_TIME
"""
norData = nm.mat([[1, 0, 38, 0, 0, float(2554)], [16, 0, 16, 0, 0, 133], [4, 0, 2, 0, 0, 22], [11, 0, 66, 0, 0, 295]])
w = nm.mat([[1], [6.89218499], [1], [1.14422352], [1.15887943], [1]])
prob, lab = pred(normalization(norData), w)
print(prob, "\n\n", lab)
quit()
"""

# 初始化算法
algorithmModel = ad()

algorithmModel.printParam()

originData, _ = algorithmModel.loadData2(filter=True)
print("\n源数据:\n", originData, "\nsize:", nm.shape(originData))

# norData = algorithmModel.normalization(originData)
# print("\n归一化:\n", norData)

weight = algorithmModel.train(originData)
print("\n模型权重:\n", weight)

# 加载样本预测数据
predData, uid = algorithmModel.loadData2(filter=False)

predResult, label = algorithmModel.pred(predData, weight)
print("预测结果:\n", predResult, "\nlabel:\n", label)

for k, v in enumerate(predResult):
    print("uid:%s label:%s sigmoid:%s vector:%s" % (uid[k], label[k], v, predData[k]))
