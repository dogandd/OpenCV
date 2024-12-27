import cv2 
import numpy as np

# resmi gri tonlarda almak için 0 koyuluyor
img = cv2.imread("D:\\Resimler\\araba.png",0)
row,col = img.shape

# float32 içnde girilen matrixler aslında fotoğrafın dışında kalan siyah alanı ifade ediyor
# 1,0 ile başlayan matrisin 3. elemanını arttırdıkça yatayda siyah alan artar
# 0,1 ile başlayan matrisin 3. elemanını arttırdıkça düşeyde siyah alan artar
M = np.float32([[1,0,10],[0,1,500]])
dst = cv2.warpAffine(img,M,(row, col))

cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()