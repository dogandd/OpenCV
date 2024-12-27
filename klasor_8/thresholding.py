# thresholding resim öbeklendirme yöntemleridir

import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\araba.png",0)

# iki değişken kullanıyoruz returnden gelen ret ve threshold yapıldığı için th1
# 127 ile 255 değerleri arasında threshold yapıyor ve THRESH_BINARY kullanıyor
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,1)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,41,5)


# cv2.imshow("img",img)
cv2.imshow("img-th1",th1)
cv2.imshow("img-th2",th2)
cv2.imshow("img-th3",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
