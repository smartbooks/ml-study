# encoding:utf-8

import numpy as nm
import cv2


def readImg(path, flags=None):
    return cv2.imread(path, flags)


def saveImg(path, imgmat):
    cv2.imwrite(path, imgmat)


def show(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def printMat(mat):
    print(("shape:\n%s\nmat:\n%s") % (nm.shape(mat), mat))


srcImg = "c:/test/001.jpg"
grayImg = "c:/test/001.gray.jpg"

img = readImg(srcImg, cv2.IMREAD_GRAYSCALE)

saveImg(grayImg, img)

printMat(img)

U, Sigma, VT = nm.linalg.svd(img)

sigmaN = 1
totalEnergy = sum(Sigma ** 2)
totalEnergy90 = totalEnergy * 0.99
for k in range(len(Sigma)):
    kIt = k + 1
    kEnergy = sum(Sigma[:kIt] ** 2)
    print(("总能量:%s 90:%s K能量:%s k:%s") % (totalEnergy, totalEnergy90, kEnergy, kIt))
    if kEnergy >= totalEnergy90:
        sigmaN = kIt
        break

svdSigma = nm.mat(nm.eye(sigmaN) * Sigma[:sigmaN])
svdImg = nm.around(U[:, :sigmaN] * svdSigma * VT[:sigmaN, :])

#show(svdImg)
printMat(svdImg)
saveImg("c:/test/0.99.jpg", svdImg)
