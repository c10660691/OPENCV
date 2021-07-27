import cv2 as cv
import numpy as np
img1 = cv.imread("001.jpg")
img2 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
mask = cv.inRange(img1, lower_blue, upper_blue)
# Bitwise-AND mask and original image
res = cv.bitwise_and(img1, img1, mask=mask)
cv.imshow("test", img1)
cv.imshow("test2", img1)
cv.imshow("res", res)
cv.waitKey(0)
cv.destroyAllWindows()
