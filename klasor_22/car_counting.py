import cv2
import numpy as np

vid = cv2.VideoCapture("D:\\Videolar\\traffic.avi")
# arka plan çıkarıldı
backsub = cv2.createBackgroundSubtractorMOG2()
# araba sayacı ilk başta 0 olarak belirlendi
c = 0

while 1:
    ret,frame = vid.read()
    # frameler doğru alındıysa işlem yapmaya devam edecek
    if ret:
        # arkaplan siyah yapıldı
        fgmask = backsub.apply(frame)
        # arabaların geçişi iiçin sınır çizgileri belirlendi
        cv2.line(frame,(50,0),(50,300),(0,255,0),2)
        cv2.line(frame,(70,0),(70,300),(0,255,0),2)

        # contourlar alındı
        countours,hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # hata alınması durumunda da hierarchy boş kalacak
        try: hierarchy = hierarchy[0]
        except:hierarchy = []

        for contour,hier in zip(countours,hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            # okunan contour değerlerinde w ve h istenilen değerlerden büyükse oradan arab geçtiğini anlıyoruz
            if w>40 and h>40:
                # bulunan contour dikdörtgenle belirleniyor 
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                # çizgiler arasından geçtiği kontrol ediliyor
                if x>50 and x<70:
                    c += 1
        # geçen araç sayısı yazılıyor
        cv2.putText(frame,"car:" + str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)

        cv2.imshow("car counter",frame)
        cv2.imshow("fgmask",fgmask)



    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()