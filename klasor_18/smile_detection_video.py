import cv2
import numpy as np

cap = cv2.VideoCapture("D:\\Videolar\\smile.mp4")

# gülümseme yüzün tespit alanında olduğu için önce yüz tespit edilecek 
# bu yüzden 2 cascade dosyasını çalışmaya ekliyoruz
face_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\frontalface.xml")
smile_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\smile.xml")



while 1:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(960,540))

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,9)

    # yüzlerin tespitinde bulunan konumlar alınır ve yüzler bir dikdörtgenle belirlenir
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    # bulunan yüzlerin konumlarıyla roi belirlenir
    roi_frame = frame[y:y+h,x:x+w]
    roi_gray = gray[y:y+h,x:x+w] 

    # roi içerisinde gülümsemenin konumları bulunur
    smiles = smile_cascade.detectMultiScale(roi_gray,1.5,3)
    # belirlenen roide gülümseme konumlarına göre dikdörtgen içine alınır
    for (sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_frame,(sx,sy),(sx+sw,sy+sh),(255,0,0),3)

    cv2.imshow('image',frame)

    if cv2.waitKey(30) == 27 :
        break


cap.release()
cv2.destroyAllWindows()
