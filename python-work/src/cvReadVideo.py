# encoding:utf-8

import cv2

simpleVideo = "D:\\temp\\20180407_142409.mp4"

# 打开摄像头
cap = cv2.VideoCapture(0)


# cap = cv2.VideoCapture(simpleVideo)


def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]

    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (h / 2, w / 2)

    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (h, w))

    # 返回旋转后的图像
    return rotated


if cap.isOpened():

    isRead = True
    frameCount = 0
    keyFrameMod = 5

    while isRead:
        isRead, frame = cap.read()
        frameCount += 1
        if frameCount % keyFrameMod == 0:
            print(isRead)

            # 裁剪
            dstImage = cv2.resize(frame, (512, 512))

            # 旋转
            # dstImage = rotate(dstImage, -90)

            # 灰度化
            dstImage = cv2.cvtColor(dstImage, cv2.COLOR_BGR2GRAY)

            # 二值化
            ret, dstImage = cv2.threshold(dstImage, 127, 255, cv2.THRESH_BINARY)

            # 保存
            filename = "D:\\temp\\" + str(frameCount) + ".jpg"
            # cv2.imwrite(filename, dstImage, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

            # 显示图像
            cv2.imshow("real", dstImage)
            cv2.waitKey(100)
else:
    print("video not open")

cap.release()
cv2.destroyAllWindows()
