import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\map.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
# kullandığımız resimde threshold yaparken istenilmeyen bazı yerlerinde thrshlendiği için değerleri ona göre ayarlıyoruz
ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY)


"""
cv2.imshow("img",img)
cv2.imshow("blur",blur)
cv2.imshow("thresh",thresh)
cv2.imshow("gray",gray)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()