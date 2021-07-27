import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def bgr2rbg(img):
    '''
        将颜色空间从BGR转换为RBG
    '''
    return img[:, :, ::-1]


img = cv.imread("001.jpg")

img1 = cv.resize(img, None, fx=1/2, fy=1/2, interpolation=cv.INTER_CUBIC)
img2 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
cv.namedWindow('img1')
img2 = img1[:, ::-1]
img3 = img1[::-1]
img4 = img1[::-1, ::-1]
plt.subplot(221)
plt.title('SRC')
plt.imshow(bgr2rbg(img1))

plt.subplot(222)
plt.title('Horizontally')
plt.imshow(bgr2rbg(img2))

plt.subplot(223)
plt.title('Vertically')
plt.imshow(bgr2rbg(img3))

plt.subplot(224)
plt.title('Horizontally & Vertically')
plt.imshow(bgr2rbg(img4))

plt.show()
