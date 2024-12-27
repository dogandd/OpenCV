import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("D:\\Resimler\\araba.png")
# split rasmin bgr değerlerine ayırır
b,g,r = cv2.split(img)
# 500 e 500lük siyah ekran oluşturuluyor
# img = np.zeros((500,500),np.uint8) + 50
#cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
#cv2.rectangle(img,(250,170),(350,200),(255,255,255),-1)

cv2.imshow("img",img)

# hist metoduyla histogram oluşturuyor 3 parametre alır
# ravel metodu girilen resmin tüm piksel değerlerini bir satıra döker
# 256 ile kaç değer olduğunu ve [0,256] ile değer aralığını belirliyoruz
#plt.hist(img.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()