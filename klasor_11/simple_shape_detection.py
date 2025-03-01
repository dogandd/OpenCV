import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread("D:\\Resimler\\polygons.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# threshold değerleri alınır
_,threshold = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
# thrashol değerlerinden contourlar bulunur
contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # contourlara daha da yaklaşım işlemi yapılıyor
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    cv2.drawContours(img,[approx],0,(0),5)

    # tüm sütunları satıra dökmeye yarar
    # 0. index x e 1. index y ye eşit
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
    # approxdan gelen değerlere göre şekillere isim veriliyor
    if len(approx) == 3:
        cv2.putText(img,"triangle",(x,y),font1,1,(0))
    if len(approx) == 4:
        cv2.putText(img,"rectangle",(x,y),font1,1,(0))
    if len(approx) == 5:
        cv2.putText(img,"pentagon",(x,y),font1,1,(0))
    if len(approx) == 6:
        cv2.putText(img,"hexagon",(x,y),font1,1,(0))
    if len(approx) > 6:
        cv2.putText(img,"ellipse",(x,y),font1,1,(0))
    
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()