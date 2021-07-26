import numpy as np
import cv2 as cv
# 鼠标回调函数


def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img1, (x, y), 100, (255, 0, 0), 3)


# 创建一个黑色图像，一个窗口，然后和回调绑定
img1 = cv.imread("001.jpg")
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.setMouseCallback('image', draw_circle)
while(1):
    cv.imshow('image', img1)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
