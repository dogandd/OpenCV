import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\starwars.jpg")

blurry_img = cv2.medianBlur(img,7)

# Laplacian fonksiyonu içine girilen resimle birlikte değer döndürüyor (cv2.CV_64F sabit)
laplacian = cv2.Laplacian(blurry_img,cv2.CV_64F).var()

# laplacian fonksiyonundan gelen değer düştükçe resimdeki blur daha da azalır bu yüzden kıyas yapılarak blur kontrolü yapılır
if laplacian < 500 :
    print("blurry image")

cv2.imshow("image",img)
cv2.imshow("blur",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()