import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\face.png")
# gözler yüzün tespit alanında olduğu için önce yüz tespit edilecek 
# bu yüzden 2 cascade dosyasını çalışmaya ekliyoruz
face_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\eye.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# tespit edilen yüzlerin konumları alınır
faces = face_cascade.detectMultiScale(gray,1.3,5)

# yüzlerin tespitinde bulunan konumlar alınır ve yüzler bir dikdörtgenle belirlenir
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

# bulunan yüzlerin konumlarıyla roi belirlenir
img2 = img[y:y+h,x:x+w]
gray2 = gray[y:y+h,x:x+w] 

# roi içerisinde gözlerin konumları bulunur
eyes = eye_cascade.detectMultiScale(gray2)

# belirlenen roide gözlerin konumlarına göre dikdörtgen çiziçine alınır
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
