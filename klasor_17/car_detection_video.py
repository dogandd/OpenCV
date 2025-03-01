import cv2
import numpy as np

cap = cv2.VideoCapture("D:\\Videolar\\car.mp4")
# cascade dosyası çalışmaya ekleniyor
car_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\car.xml")

while 1:
    ret,frame = cap.read()
    # büyük olduğu için frameler yeniden boyutlandırıldı
    frame = cv2.resize(frame,(960,540))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # her framede bulunan araba konumları tutuluyor
    bodies = car_cascade.detectMultiScale(gray,1.2,3)

    # araba konumlarına göre dikdörtgen içine alınıyor
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("video",frame) 

    if cv2.waitKey(5) == 27:
        break

cap.release()
cv2.destroyAllWindows()