import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\car.jpg")
car_cascade = cv2.CascadeClassifier("D:\\haar_cascade\\car.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

bodies = car_cascade.detectMultiScale(gray,1.1,1)


for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()