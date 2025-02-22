import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\frontalface.xml")
eye_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\eye.xml")



while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    frame2 = frame[y:y+h,x:x+w]
    gray2 = gray[y:y+h,x:x+w] 

    eyes = eye_cascade.detectMultiScale(gray2)

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame2,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)

    cv2.imshow('image',frame)

    if cv2.waitKey(5) == 27 :
        break


cap.release()
cv2.destroyAllWindows()
