import cv2
import numpy as np

cap = cv2.VideoCapture("D:\\Videolar\\car.mp4")

_,first_frame = cap.read()
# videonun ilk framei tutuluyor
first_frame = cv2.resize(first_frame,(640,480))
first_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray,(5,5),0)
while 1:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # blur ekleniyor
    gray = cv2.GaussianBlur(gray,(5,5),0)   

    # absdiff fonksiyonuyla ilk frame ile güncel frame i karşılaştırılır 
    diff = cv2.absdiff(first_gray,gray)
    # kıyas yaptıktan sonra sadece siyah ve beyaz renkler kalması için threshold yapıldı
    _,diff = cv2.threshold(diff,50,255,cv2.THRESH_BINARY)

    cv2.imshow("frame",frame)
    cv2.imshow("first",first_frame)
    cv2.imshow("diff",diff)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()