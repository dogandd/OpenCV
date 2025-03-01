import cv2
import numpy as np
from collections import deque

cap = cv2.VideoCapture(0)

# çizim yapmak için maskelenecek rengin alt ve üst değerleri girildi
lower_blue = np.array([100,60,60])
upper_blue = np.array([140,255,255])

# renkler için nokta sayısı tutulacak liste oluşturuluyor
blue_points = [deque(maxlen=512)]
green_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]

# renklerin index değerleri tutuluyor
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

# renkler turuluyor
colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
color_index = 0

# resmin yapılacağı beyaz pencere ouşturuluyor
paint_window = np.zeros((471,636,3))+255

# seçilecek olan renklerin alanları belirleniyor
paint_window = cv2.rectangle(paint_window,(40,1),(140,65),(0,0,0),2)
paint_window = cv2.rectangle(paint_window,(160,1),(255,65),colors[0],-1)
paint_window = cv2.rectangle(paint_window,(275,1),(370,65),colors[1],-1)
paint_window = cv2.rectangle(paint_window,(390,1),(485,65),colors[2],-1)
paint_window = cv2.rectangle(paint_window,(505,1),(600,65),colors[3],-1)

font = cv2.FONT_HERSHEY_SIMPLEX
# belirlenen alanlara yazıları yazılıyor
cv2.putText(paint_window,"CLEAR ALL",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(paint_window,"BLUE",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paint_window,"GREEN",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paint_window,"RED",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paint_window,"YELLOW",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)



while 1 : 
    # anlık olarak çizim yapılacağı için frameler tutuluyor
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # webcamden gelen görüntüye de seçilecek renkler ekleniyor
    frame = cv2.rectangle(frame,(40,1),(140,65),(0,0,0),2)
    frame = cv2.rectangle(frame,(160,1),(255,65),colors[0],-1)
    frame = cv2.rectangle(frame,(275,1),(370,65),colors[1],-1)
    frame = cv2.rectangle(frame,(390,1),(485,65),colors[2],-1)
    frame = cv2.rectangle(frame,(505,1),(600,65),colors[3],-1)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame,"CLEAR ALL",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(frame,"BLUE",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"GREEN",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"RED",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,"YELLOW",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)

    if ret is False:
        break

    # çizim yapmak için algılanacak renk mask işlemiyle tutuluyor
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    # rengi daha iyi okuyabilmek için gürültüsünü azaltacak işlemler yapılır
    mask = cv2.erode(mask,(5,5),iterations=1)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,(5,5))
    mask = cv2.dilate(mask,(5,5),iterations=1)

    # contourları belirlenir
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    center = None

    # contour belirlendi mi kontrol yapar ona göre işlem yapar
    if len(contours) > 0:
        # contour alanlarını büyükten küçüğe sıralı şekilde tutar
        max_cnt = sorted(contours,key = cv2.contourArea,reverse=True)[0]
        # contour değerlerine göre etrafını sınırlayan bir çember değeri döndürür 
        ((x,y),radius)=cv2.minEnclosingCircle(max_cnt)
        # gelen değerlere göre etrafına çember çizerek belirler
        cv2.circle(frame,(int(x),int(y)),int(radius),(255,255,0),3)

        # merkez konumları tutulur
        M = cv2.moments(max_cnt)
        center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))

        # merkez 65den küçükse renk belirleneceği için renk belirler
        if center[1] <= 65:
            # değer 40-140 arasında ise her şeyi temizleyeceği alanda olur
            if 40<=center[0]<=140:
                blue_points = [deque(maxlen=512)]
                green_points = [deque(maxlen=512)]
                red_points = [deque(maxlen=512)]
                yellow_points = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0
                # renk seçim yerinin dışında tüm alanı tarar her pikselin rengini beyaza çevirir
                paint_window[67:,:,:] = 255
            # diğer konum aralığında bulunduğu yere göreordaki konumdaki renge göre indis değeri alır
            elif 160<=center[0]<=255:
                color_index = 0
            elif 275<=center[0]<=370:
                color_index = 1
            elif 390<=center[0]<=485:
                color_index = 2
            elif 505<=center[0]<=600:
                color_index = 3
        
        # çizim alanında bulunan noktaları konuma göre ekliyor
        else:
            if color_index == 0:
                blue_points[blue_index].appendleft(center)
            elif color_index == 1:
                green_points[green_index].appendleft(center)
            elif color_index == 2:
                red_points[red_index].appendleft(center)
            elif color_index == 3:
                yellow_points[yellow_index].appendleft(center)
    else:
        # her rengene ekleme yapacağı için indis değerleri de artar
        blue_points.append(deque(maxlen=512))
        blue_index += 1

        green_points.append(deque(maxlen=512))
        green_index += 1
        
        red_points.append(deque(maxlen=512))
        red_index += 1

        yellow_points.append(deque(maxlen=512))
        yellow_index += 1

    # noktalar bir liste olarak tutulur
    points = [blue_points,green_points,red_points,yellow_points]

    # iç içe listelerin içinde gezilir
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1,len(points[i][j])):
                # başlangıç ve bitiş değerleri var mı diye bakılıyor yoksa devam ediyor
                if points[i][j][k-1] is None or points[i][j][k] is None:
                    continue
                # noktaların konumlarına göre çizgiler eklenir
                cv2.line(frame,points[i][j][k-1],points[i][j][k],colors[i],2)
                cv2.line(paint_window,points[i][j][k-1],points[i][j][k],colors[i],2)
            



    cv2.imshow("frame",frame)
    cv2.imshow("paint",paint_window)

    if cv2.waitKey(20) == 27:
        break



cap.release()
cv2.destroyAllWindows()
