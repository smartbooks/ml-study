# encoding:utf-8

import numpy as nm

dataMat = nm.mat([
    [0.478021561010024, 0.827661690820311, 0.956023977622685, 0.6767874489572, 0.092512422253237],
    [0.512314455751239, 0.871910584041342, 0.769302906087351, 0.237844864336621, 0.150698351432819],
    [0.919790611159201, 0.790811382739527, 0.148248906442396, 0.851233586913632, 0.75841281115937],
    [0.859063366709885, 0.059103796303627, 0.050316134198099, 0.499247425102873, 0.866106600893647],
    [0.6750847463637, 0.252612039984429, 0.884194546607854, 0.693952067396141, 0.540297926951868],
    [0.741044304838389, 0.971868847203081, 0.507215041445652, 0.627141398644459, 0.504117671585509],
    [0.491850888120081, 0.43044851789967, 0.483005292246538, 0.952516897105684, 0.164598900148496],
    [0.153370637073447, 0.624426296178164, 0.205781263258872, 0.407916165121405, 0.554119765362372],
    [0.56073559732117, 0.360857821538253, 0.655003392001228, 0.375033160852286, 0.626177980711413],
    [0.485555815451045, 0.324307919289746, 0.210449606580325, 0.202275808420108, 0.665492412984544]])

U, SIGMA, VT = nm.linalg.svd(dataMat)

print(("原始矩阵%s:\n%s\nU%s:\n%s\nSIGMA:\n%s\nVT%s:\n%s") % (
    nm.shape(dataMat), dataMat, nm.shape(U), U, SIGMA, nm.shape(VT), VT))

# 总能量
sigmaN = 1
totalEnergy = sum(SIGMA ** 2)
totalEnergy90 = totalEnergy * 0.98
for k in range(len(SIGMA)):
    kIt = k + 1
    kEnergy = sum(SIGMA[:kIt] ** 2)
    print(("总能量:%s 90:%s K能量:%s k:%s") % (totalEnergy, totalEnergy90, kEnergy, kIt))
    if kEnergy >= totalEnergy90:
        sigmaN = kIt
        break

restoreSigmaMat = nm.mat(nm.eye(sigmaN) * SIGMA[:sigmaN])

restoreMat = U[:, :sigmaN] * restoreSigmaMat * VT[:sigmaN, :]

print(("k:%s\nsigma:\n%s\n重建矩阵%s:\n%s\n[0]T:\n%s") % (
    sigmaN, restoreSigmaMat, nm.shape(restoreMat), restoreMat, restoreMat[0, :].T))

# 将物品转到低维空间
originMat1 = dataMat.T * U[:, :sigmaN] * restoreSigmaMat.I

# T:转置
# H:共轭
# I:逆矩阵

print(("原始数据转置%s:\n%s\nsigmaI:\n%s") % (nm.shape(dataMat.T), dataMat.T, restoreSigmaMat.I))

print(("Item与Item相似度:\n%s\n[0]T:\n%s") % (originMat1, originMat1[0, :].T))
