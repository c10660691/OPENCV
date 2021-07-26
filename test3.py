import numpy as np
import cv2 as cv
import cv2
# 创建一个黑色的图像
img1 = cv2.imread("1unknown.png")
img = np.zeros((512, 512, 3), np.uint8)
# 画一条 5px 宽的蓝色对角线
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
cv2.imshow("test", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
