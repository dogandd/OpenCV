import cv2
import numpy as np
import math

def findMaxContour(contours):
    max_i = 0
    max_area = 0

    for i in range(len(contours)):
        area_face = cv2.contourArea(contours[i])

        if max_area < area_face :
            max_area = area_face
            max_i = i

        try:
            c = contours[max_i]
        except:
            contours = [0]
            c = contours[0]
        return c

cap = cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    roi = frame[50:250, 170:400]

    cv2.rectangle(frame,(170,50),(400,250),(0,0,255),0)

    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,45,79],dtype = np.uint8)
    upper_color = np.array([17,255,255],dtype = np.uint8)
    
    mask = cv2.inRange(hsv,lower_color,upper_color)
    kernel = np.ones((3,3),np.uint8)
    # görüntünün bulanıklığı azaltıldı daha net bir görüntü elde edildi
    mask = cv2.dilate(mask,kernel,iterations=1)
    mask = cv2.medianBlur(mask,15)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0 :
        c = findMaxContour(contours)
        
        # en küçük x değeri
        extleft = tuple(c[c[:,:,0].argmin()][0])
        # en büyük x değeri
        extright = tuple(c[c[:,:,0].argmax()][0])
        # en küçük y değeri y olduğu için 1
        exttop = tuple(c[c[:,:,1].argmin()][0])
        # en büyük y değeri 
        extbot = tuple(c[c[:,:,1].argmax()][0])

        # bulunan uç noktalara çember çiziyor
        cv2.circle(roi,extleft,5,(0,255,0),2)
        cv2.circle(roi,extright,5,(0,255,0),2)
        cv2.circle(roi,exttop,5,(0,255,0),2)
        cv2.circle(roi,extbot,5,(0,255,0),2)

        # belirlenen noktaları birleştiriyor
        cv2.line(roi,extleft,exttop,(0,255,0),2)
        cv2.line(roi,exttop,extright,(0,255,0),2)
        cv2.line(roi,extleft,exttop,(0,255,0),2)
        cv2.line(roi,extbot,extleft,(0,255,0),2)

        # bulunan noktaların arasındaki mesafelerle açıları hesaplama
        a = math.sqrt((extright[0]-exttop[0])**2 + (extright[1]-exttop[1])**2 )
        b = math.sqrt((extbot[0]-extright[0])**2 + (extbot[1]-extright[1])**2 )
        c = math.sqrt((extbot[0]-exttop[0])**2 + (extbot[1]-exttop[1])**2 )
        

        # değerlerin 0 olma durumunda 0 a bölümden hata çıkması durumu için try kulanılıyor
        try:
            angle_ab = math.acos((a**2+b**2-c**2)/(2*b*c))*57
            cv2.putText(roi,str(angle_ab),(extright[0]-10,extright[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
        except:
            cv2.putText(roi,"?",(extright[0]-10,extright[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)



    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()