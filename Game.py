import cv2
import os
import numpy as np
img = cv2.imread("463300893_532633549720211_3262292791778244347_n.jpg", cv2.IMREAD_GRAYSCALE)
_, img = cv2.threshold(img, 135, 255, cv2.THRESH_BINARY)
img = cv2.resize(img, (int(1580/3), int(2048/3)))
font = cv2.FONT_HERSHEY_SIMPLEX

newImg = np.ones((img.shape[0], img.shape[1], 1), np.uint8) * 255
cnt = 0
show = 10
for i in range(0, img.shape[0], 4):
    for j in range(0, img.shape[1], 4):
        if img[i, j] == 0:
            newImg = cv2.putText(newImg, 'Wibu', (j, i), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=0.2, color=(0,0,0), thickness=1, lineType = cv2.LINE_AA)
            cnt += 1
            if cnt % show == 0:
                cv2.imshow("Wibu", newImg)
                cv2.waitKey(1)
cv2.imshow("Wibu", newImg)
cv2.waitKey()