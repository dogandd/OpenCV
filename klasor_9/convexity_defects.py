import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\star.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# kullandığımız resimde threshold yaparken istenilmeyen bazı yerlerinde thrshlendiği için değerleri ona göre ayarlıyoruz
ret,thresh = cv2.threshold(gray,127,255,0)

contours,_ = cv2.findContours(thresh,2,1)

cnt = contours[0]
# dış bükey örtü oluşturabilmek için bazı değerlerin tutulması gerekiyor bunları convexHull metoduyla hull değişkeninde tutuluyor
# returnPoints= False olduğu zaman convexHulldan gelen değerlerin indisleri döner
hull = cv2.convexHull(cnt, returnPoints= False)

# kusurları covexityDefects metoduyla arıyoruz
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    # s(start point), e(end point), f(farthest point)(en uzak mesafe), distance(mesafe)
    # s,e noktalarını kullanarak dış bükey çizgiler çekilir
    # f ile içde kalan kusur noktaları belirleniyor
    s,e,f,d = defects[i,0] 
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,255,0],-1)

cv2.imshow("img",img)

"""
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()