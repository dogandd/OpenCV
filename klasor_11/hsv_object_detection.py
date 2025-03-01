import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture("D:\\Videolar\\hsv.mp4")
cv2.namedWindow("Trackbar")
# trackbarlar oluşturuluyor
cv2.createTrackbar("LH","Trackbar",0,180,nothing)
cv2.createTrackbar("LS","Trackbar",0,255,nothing)
cv2.createTrackbar("LV","Trackbar",0,255,nothing)
cv2.createTrackbar("UH","Trackbar",0,180,nothing)
cv2.createTrackbar("US","Trackbar",0,255,nothing)
cv2.createTrackbar("UV","Trackbar",0,255,nothing)

while 1:
    _,frame = cap.read()
    frame = cv2.resize(frame,(400,300))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # trackbarlar getiriliyor ve değerleri tutuluyor
    lh = cv2.getTrackbarPos("LH","Trackbar")
    ls = cv2.getTrackbarPos("LS","Trackbar")
    lv = cv2.getTrackbarPos("LV","Trackbar")
    uh = cv2.getTrackbarPos("UH","Trackbar")
    us = cv2.getTrackbarPos("US","Trackbar")
    uv = cv2.getTrackbarPos("UV","Trackbar")

    # tutulan değerlerle alt ve üst sınır için dizi oluşturuluyor
    lower_blue = np.array([lh,ls,lv])
    upper_blue = np.array([uh,us,uv])

    # trackbarlardan gelen değerlere göre mask uyguluyor
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    # iki resim arasındaki farklar birbirleriyle kıyaslandı 
    bitwise = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()