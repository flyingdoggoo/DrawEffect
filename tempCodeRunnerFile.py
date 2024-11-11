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
    img_mat = cv2.imread(file_path, cv2.IMREAD_COLOR)
    if img_mat is None:
        print("Unable to read image.")
    else:
        print(img_mat.shape)
        _, img_mat = cv2.threshold(img_mat, 127, 255, cv2.THRESH_BINARY)
        img_mat = cv2.resize(img_mat, (int(img_mat.shape[1] / 2), int(img_mat.shape[0] / 2)))
        font = cv2.FONT_HERSHEY_SIMPLEX
        n, m, z = img_mat.shape
        newImg = np.full((n, m, z), 255, dtype=np.uint8)
        cv2.imshow("test", newImg)
        cnt = 0
        show = 80

        for i in range(0, n, 2):
            for j in range(0, m, 2):
                if img_mat[i, j, 0] or img_mat[i, j, 1] or img_mat[i, j, 2] :
                    newImg = cv2.putText(newImg, 'AAA', (j, i), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                        fontScale=0.1, color=(img_mat[i, j, 0], img_mat[i, j, 1], img_mat[i, j, 2]), thickness=1, lineType=cv2.LINE_AA)
                    cnt += 1
                    if cnt % show == 0:
                        cv2.imshow("AAA", newImg)
                        cv2.waitKey(1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
