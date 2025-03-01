import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\face.png")
# CascadeClassifier kullanarak cascade dosyası çalışmaya ekleniyor
face_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\frontalface.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# bulunan yüzlerin kordinatlarını faces değişkeninde tutuluyor
faces = face_cascade.detectMultiScale(gray,1.3,7)

# yüzlerin tespitinde bulunan konumlar alınır ve yüzler bir dikdörtgenle belirlenir
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
