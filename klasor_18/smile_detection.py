import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\smile.jpg")
# gülümseme yüzün tespit alanında olduğu için önce yüz tespit edilecek 
# bu yüzden 2 cascade dosyasını çalışmaya ekleniyor
face_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\frontalface.xml")
smile_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\smile.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)

# yüzlerin tespitinde bulunan konumlar alınır ve yüzler bir dikdörtgenle belirlenir
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    
# bulunan yüzlerin konumlarıyla roi belirlenir
roi_img = img[y:y+h,x:x+w]
roi_gray = gray[y:y+h,x:x+w] 

# roi içerisinde gülümsemenin konumları bulunur
smiles = smile_cascade.detectMultiScale(roi_gray,1.5,9)

# belirlenen roide gülümseme konumlarına göre dikdörtgen çiziçine alınır
for (ex,ey,ew,eh) in smiles:
    cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

