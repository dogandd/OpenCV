import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\frontalface.xml")
smile_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\smile.xml")



while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,9)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    roi_frame = frame[y:y+h,x:x+w]
    roi_gray = gray[y:y+h,x:x+w] 

    smiles = smile_cascade.detectMultiScale(roi_gray,1.2,9)

    for (sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_frame,(sx,sy),(sx+sw,sy+sh),(255,0,0),3)

    cv2.imshow('image',frame)

    if cv2.waitKey(30) == 27 :
        break


cap.release()
cv2.destroyAllWindows()
