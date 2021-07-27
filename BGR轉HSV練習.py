import cv2 as cv
import numpy as np


def nothing(x):
    pass


img1 = cv.imread("001.jpg")
img2 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
cv.namedWindow('img1')
cv.createTrackbar('HM', "img1", 0, 255, nothing)
cv.createTrackbar('HH', "img1", 0, 255, nothing)
cv.createTrackbar('SM', "img1", 0, 255, nothing)
cv.createTrackbar('SH', "img1", 0, 255, nothing)
cv.createTrackbar('VM', "img1", 0, 255, nothing)
cv.createTrackbar('VH', "img1", 0, 255, nothing)
while(True):
    HM = cv.getTrackbarPos("HM", "img1")
    HH = cv.getTrackbarPos("HH", "img1")
    SM = cv.getTrackbarPos("SM", "img1")
    SH = cv.getTrackbarPos("SH", "img1")
    VM = cv.getTrackbarPos("VM", "img1")
    VH = cv.getTrackbarPos("VH", "img1")
    lower = np.array([HM, SM, VM])
    upper = np.array([HH, SH, VH])
    mask = cv.inRange(img2, lower, upper)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(img1, img1, mask=mask)
    cv.imshow("img1", img1)
    cv.imshow("img2", img2)
    cv.imshow("res", res)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
