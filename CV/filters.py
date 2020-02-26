import numpy as np
import cv2

img = cv2.imread('sonic.jpg', cv2.IMREAD_COLOR)
img = img/255.0
w = img.shape[1]
h = img.shape[0]
csum = np.zeros(img.shape)
for i in range(0, w):
    for j in range(0, h):
        csum[i][j] = img[i][j]*(1/(w*h))

cv2.imshow('sonic', csum)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()