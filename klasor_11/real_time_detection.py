import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("settings")
# trackbarlar oluşturuluyor
cv2.createTrackbar("Lower-Hue","settings",0,180,nothing)
cv2.createTrackbar("Lower-Saturation","settings",0,255,nothing)
cv2.createTrackbar("Lower-Value","settings",0,255,nothing)
cv2.createTrackbar("upper-Hue","settings",0,180,nothing)
cv2.createTrackbar("upper-Saturation","settings",0,255,nothing)
cv2.createTrackbar("upper-Value","settings",0,255,nothing)

font = cv2.FONT_HERSHEY_COMPLEX

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # trackbarlar getiriliyor ve değerleri tutuluyor
    lh = cv2.getTrackbarPos("Lower-Hue","settings")
    ls = cv2.getTrackbarPos("Lower-Saturation","settings")
    lv = cv2.getTrackbarPos("Lower-Value","settings")
    uh = cv2.getTrackbarPos("upper-Hue","settings")
    us = cv2.getTrackbarPos("upper-Saturation","settings")
    uv = cv2.getTrackbarPos("upper-Value","settings")

    # tutulan değerlerle alt ve üst sınır için dizi oluşturuluyor
    lower_color = np.array([lh,ls,lv])
    upper_color = np.array([uh,us,uv])

    # trackbarlardan gelen değerlere göre mask uyguluyor
    mask = cv2.inRange(hsv,lower_color,upper_color)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.erode(mask, kernel)

    # mask dan bakılarak konturları belirleniyor
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # contour alanları alınır
        area = cv2.contourArea(cnt)
        epsilon = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)

        # tüm sütunları satıra dökmeye yarar
        # 0. index x e 1. index y ye eşit
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        # contour alanlarına göre şekillere isim yazıyor
        if area > 400:
            cv2.drawContours(frame,[approx],0,(0,0,0),5)
            if len(approx) == 3:
                cv2.putText(frame,"triangle",(x,y),font,1,(0,0,0))
            elif len(approx) == 4:
                cv2.putText(frame,"rectangle",(x,y),font,1,(0,0,0))
            elif len(approx) > 6:
                cv2.putText(frame,"circl",(x,y),font,1,(0,0,0))
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(3) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()