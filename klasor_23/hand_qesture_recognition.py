import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

while 1: 

    try:
        # frameler çekiliyor
        ret, frame = cap.read()
        frame=cv2.flip(frame,1)
        kernel = np.ones((3,3),np.uint8)
        # roi alanı belirleniyor
        roi =frame[100:300, 100:300]
        
        # belirlenen roi alanı kameradan gelen görntüde alanları çiziliyor
        cv2.rectangle(frame,(100,100),(300,300),(0,0,255),0)
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        

        # ten rengimize göre alt ve üst değerler belirlenir
        lower_skin = np.array([0,20,70],dtype=np.uint8)
        upper_skin = np.array([20,255,255],dtype=np.uint8)

        # roi alanına mask işlemi uygulanıyor
        mask = cv2.inRange(hsv,lower_skin,upper_skin)
        mask = cv2.dilate(mask,kernel,iterations = 4)
        mask = cv2.GaussianBlur(mask, (5,5),100)

        # contourlar belirleniyor
        countours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # contour alanlarından en büyüğü döndürülcek
        cnt = max(countours, key = lambda x:cv2.contourArea(x))

        epsilon = 0.0005*cv2.arcLength(cnt,True)
        # contourlara daha da yaklaşılıyor
        approx = cv2.approxPolyDP(cnt,epsilon,True)

        # contourun dışbükey gövdesi oluşturuldu
        hull = cv2.convexHull(cnt)

        # hull bölgesinin alanı hesaplandı 
        areaHull = cv2.contourArea(hull)
        # elimizin alanı hesaplandı 
        areaCnt = cv2.contourArea(cnt)
        # boş alanın elimize oranı hesaplandı
        areaRatio = ((areaHull-areaCnt)/areaCnt)*100

        # konturların indislerine erişilde (false olduğu için indisleri döndürülür yoksa konturları döndürülür)
        hull = cv2.convexHull(approx,returnPoints=False)
        # contourlardaki kusurlar bulundu
        defects = cv2.convexityDefects(approx,hull)

        # başlangıç kusur değeri 0
        l = 0

        # kusurlarda geziniyor
        for i in range(defects.shape[0]):
            # her elemanın ilk indisi alınıyor
            s,e,f,d = defects[i,0]
            # approx ile değerleri çekiyoruz 
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])

            # bulunan değerlerle üçgenin kenarları hesaplanıyor
            a = math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)
            b = math.sqrt((far[0]-start[0])**2+(far[1]-start[1])**2)
            c = math.sqrt((end[0]-far[0])**2+(end[1]-far[1])**2)

            # üçgenin alanı hesaplandı
            s = (a+b+c)/2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            # noktalar ve dışbükey noktalar arasındaki noktalar hesaplandı
            d = 2*area/a
            
            # kenarlar arası açı hesaplanıyor
            angle = math.acos((b**2+c**2-a**2)/(2*b*c))*57
            #açı doksandan küçük ve d 30dan büyükse kusur var demek
            if angle<=90 and d>30 :
                l+=1
                # kusurlara daire çizer
                cv2.circle(roi,far,3,[255,0,0],-1)
            
            cv2.line(roi,start,end,[255,0,0],2)
        
        l+=1

        font = cv2.FONT_HERSHEY_SIMPLEX

        # bulunan kusur sayısına göre işlem yapar (l kusur sayısı)
        if l ==1:
            # el roide bulunmuyorsa elin alanı algılamaz 
            if areaCnt < 2000:
                cv2.putText(frame,"put your hand in the box",(0,50),font,1,(0,0,255),3,cv2.LINE_AA)
            else:
                # elin roide bulunma yüzdesine göre ekrana yazı yazı yazdırılıyor
                if areaRatio < 12:
                    cv2.putText(frame,"0",(0,50),font,2,(0,0,255),3,cv2.LINE_AA)
                elif areaRatio < 17.5:
                    cv2.putText(frame,"best luck",(0,50),font,2,(0,0,255),3,cv2.LINE_AA)
                else:
                    cv2.putText(frame,"1",(0,50),font,2,(0,0,255),3,cv2.LINE_AA)
        elif l ==2:
                cv2.putText(frame,"2",(0,50),font,2,(0,0,255),3,cv2.LINE_AA)
        elif l ==3:
            if areaRatio < 27:
                cv2.putText(frame,"3",(0,50),font,2,(0,0,255),3,cv2.LINE_AA)
            else:
                cv2.putText(frame,"ok",(0,50),font,2,(0,0,255),3,cv2.LINE_AA)
        elif l ==4:
                cv2.putText(frame,"4",(0,50),font,2,(0,0,255),3,cv2.LINE_AA)
        elif l ==5:
                cv2.putText(frame,"5",(0,50),font,2,(0,0,255),3,cv2.LINE_AA)
        elif l ==6:
                cv2.putText(frame,"reposition",(0,50),font,2,(0,0,255),3,cv2.LINE_AA)

        cv2.imshow('mask',mask)
        cv2.imshow('frame',frame)

    except:
        pass




    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
