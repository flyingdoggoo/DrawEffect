import cv2
import os
import numpy as np
img = cv2.imread("463300893_532633549720211_3262292791778244347_n.jpg", cv2.IMREAD_GRAYSCALE)
_, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
img = cv2.resize(img, (int(1580/3), int(2048/3)))
font = cv2.FONT_HERSHEY_SIMPLEX
n = img.shape[0]
m = img.shape[1]
z = 1 #rgb
newImg = np.ones((n, m, z)) * 255
cnt = 0
show = 20
for i in range(0, n, 4):
    for j in range(0, m, 4):
        if img[i, j] == 0:
            newImg = cv2.putText(newImg, 'Wibu', (j, i), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.2, color=(0,0,0), thickness=1, lineType = cv2.LINE_AA)
            cnt += 1
            if cnt % show == 0:
                cv2.imshow("Wibu", newImg)
                cv2.waitKey(1)
cv2.imshow("Wibu", newImg)
cv2.waitKey()
