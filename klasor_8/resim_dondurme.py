import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\araba.png",0)
row,col = img.shape

# resim döndürme işlemi yaparken getRotationMatrix2D metodu kullanılır
# argüman girilir sırasıyla (sütun, satır), kaç derce döneceği, ölçeği  girilir 
# döndürme işlemini saat yönünün tersi olarak döndürür
# satır ve sütun oranını azalttıkça fotoğrafın kayma oranı artıyor siyah alanlar büyüyor
M = cv2.getRotationMatrix2D((col/2,row/2),90,1)

dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
