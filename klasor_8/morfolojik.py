import cv2 
import numpy as np

img = cv2.imread("D:\\Resimler\\araba.png",0)
# ones metoduyla 1lerden oluşan matrisler oluşturulur
# o matrisleri resmin üzerine getirip resmi değiştiriyor
kernel = np.ones((5,5), np.uint8)
# resi erezyona uğratmak için erode metodu kollanılır
# sırayla fonksiyona resim, bir matrix dizini(kernel), iterasyon girilir
# iterations resmi kaç kere matrislerle değiştireceğini belirliyor
#erosion = cv2.erode(img,kernel,iterations=1)
# dilation metodu kalınlaştırma işlemi yapar
#dilation = cv2.dilate(img,kernel,iterations=2)
# openning metoduyla resimdeki bozulmaları düzenliyor(gürültüleri siliyor)
#opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)
# gradiand metodu resmin en dışını çiziyor
gradiand = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

cv2.imshow("img",img)
cv2.imshow("tophat",tophat)
#cv2.imshow("gradiand",gradiand)
#cv2.imshow("opening",opening)
#cv2.imshow("dilation",dilation)
#cv2.imshow("eresion",erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
