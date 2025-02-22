import cv2
import numpy as np

video = cv2.VideoCapture("D:\\Videolar\\faces.mp4")
face_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\frontalface.xml")

while 1:
    ret,frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("frame",frame)

    if cv2.waitKey(30) == 27:
        break


video.release()
cv2.destroyAllWindows()