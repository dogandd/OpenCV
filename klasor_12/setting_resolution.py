import cv2
import numpy as np

windowName = "Live Video"
cv2.namedWindow(windowName)

cap = cv2.VideoCapture(0)

# get fonksiyonuna 3 girilince görüntünün enini verir 
print("witdh:" + str(cap.get(3)))
# get fonksiyonuna 4 girilince görüntünün yüksekliğini verir 
print("height:" + str(cap.get(4)))

# set fonksiyonuyla birlike görüntünün en ve boy değerleri değiştiriliyor
cap.set(3,1280)
cap.set(4,720)


while 1:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow(windowName,frame)

    if cv2.waitKey(1) == 27:
        break