import cv2
import numpy as np 

img = cv2.imread("D:\\Resimler\\h_line.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# tespit edilen köşeli resim edges değişkeninde tutuluyor
# canny fonksyonuna gray resmi ve min max değerleri giriliyor
edges = cv2.Canny(gray,75,150)

# houghlinesp fonksiyonu çizgileri belirler
# parametreler olarak köşeleri tespit edilmiş resim, ρ ve θ değerleri, threshold değeri girilir
# çizgiler arası boşluğu da doldurmak için threshhold değerinden sonra maxlinegap diye bir değişken oluşturuluyor
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow("image",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()