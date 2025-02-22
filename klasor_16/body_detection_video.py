import cv2
import numpy as np

cap = cv2.VideoCapture("D:\\Videolar\\body.mp4")
body_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\fullbody.xml")

while 1:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(gray,1.1,3)


    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("video",frame) 

    if cv2.waitKey(5) == 27:
        break

cap.release()
cv2.destroyAllWindows()