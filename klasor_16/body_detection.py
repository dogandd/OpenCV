import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\body.jpg")
# cascade dosyası çalışmaya ekleniyor
body_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\fullbody.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# tespit edilen insan konumları tutuluyor
bodies = body_cascade.detectMultiScale(gray,1.1,3)


# tespit edilen insanlar konumlarına göre dikdörtgen içine alınıyor
for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()