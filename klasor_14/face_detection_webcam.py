import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Cascade dosyası çalışmaya ekleniyor
face_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\frontalface.xml")

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # bulunan yüzlerin kordinatlarını faces değişkeninde tutuluyor
    faces = face_cascade.detectMultiScale(gray,1.3,6)

    # yüzlerin tespitinde bulunan konumlar alınır ve yüzler bir dikdörtgenle belirlenir
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("frame",frame)

    if cv2.waitKey(30) == 27:
        break


cap.release()
cv2.destroyAllWindows()