import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('001.jpg')
img1 = cv.imread('001.jpg', 0)
color = ('b', 'g', 'r')
histr = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.xlim([0, 256])

plt.show()
