import numpy as np
import cv2

img = cv2.imread('sonic.jpg', cv2.IMREAD_COLOR)
img = img/255.0
h, w, d = img.shape
ksize = 11
krn = np.zeros((ksize,ksize))
krn[:,:] = 1.0 / (ksize*ksize)
krad = int(ksize/2)
framed = np.ones((h + 2*krad, w + 2*krad, d))
framed[krad:-krad, krad:-krad] = img

filtered = np.zeros(img.shape)
for i in range(0, h):
    for j in range(0, w):
        filtered[i][j] = (framed[i:i+ksize, j:j+ksize] * krn[:, :, np.newaxis]).sum(axis=(0, 1))

final = np.zeros((h, w*2+1, d))
final[:, 0: w] = img
final[:, w + 1: w*2 + 1] = filtered

cv2.imshow('sonic', final)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()