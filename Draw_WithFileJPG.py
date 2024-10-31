import cv2
import os
import numpy as np
from tkinter import Tk, filedialog
def upload_file():
    root = Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif")]
    )
    return file_path
    
file_path = upload_file()

if not file_path:
    print("No file selected.")
else:
    img_mat = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img_mat is None:
        print("Unable to read image.")
    else:
        _, img_mat = cv2.threshold(img_mat, 127, 255, cv2.THRESH_BINARY)
        img_mat = cv2.resize(img_mat, (int(img_mat.shape[1] / 3), int(img_mat.shape[0] / 3)))
        font = cv2.FONT_HERSHEY_SIMPLEX
        n, m = img_mat.shape
        z = 1
        newImg = np.full((n, m, z), 255, dtype=np.uint8)
        cnt = 0
        show = 20

        for i in range(0, n, 4):
            for j in range(0, m, 4):
                if img_mat[i, j] == 0:
                    newImg = cv2.putText(newImg, 'Wibu', (j, i), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                        fontScale=0.2, color=(0,0,0), thickness=1, lineType=cv2.LINE_AA)
                    cnt += 1
                    if cnt % show == 0:
                        cv2.imshow("Wibu", newImg)
                        cv2.waitKey(1)

        cv2.imshow("Wibu", newImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
