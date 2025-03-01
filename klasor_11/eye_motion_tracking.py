import cv2
import numpy as np

cap = cv2.VideoCapture("D:\\Videolar\\eye_motion.mp4")


while 1:
    ret,frame = cap.read()
    # roi alanı belirlendi
    roi = frame[80:210, 230:450]
    rows,cols,_ = roi.shape

    # gözün alanını belirtmek için dikdörtgen içine alınıyor
    cv2.rectangle(frame,(230,80),(450,210),(0,0,255),0)

    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    # göz bebeğini beyaz geri kalanı siyak yapmak için THRESH_BINARY_INV kullanılıyor
    _,threshold = cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV)

    contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # contour değerlerini lambda fonksiyonuna göre büyükten küçüğe sıralıyor
    contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse = True)

    for cnt in contours:
        # sol üst kordinat (x,y)
        # sağ alt kordinat (x+w,y+h)
        (x,y,w,h) = cv2.boundingRect(cnt)
        # gözbebeğinin etrafına belirtmek için dikdörtgen çizer
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)
        # gözbebeğinin merkezinden geçen birbirne dik iki çizgi oluşturulur
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)
        cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
        # contour değerleri sıralı olduğu için biz en büyük değer lazım o yüzden ilkini kullanıp döngüden çıkılıyor
        break

    frame[80:210, 230:450] = roi
    
    cv2.imshow("t_roi",threshold)
    cv2.imshow("roi",roi)
    cv2.imshow("frame",frame)

    if cv2.waitKey(80) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()