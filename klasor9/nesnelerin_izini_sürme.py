import cv2
import numpy as np

cap = cv2.VideoCapture("D:\\Videolar\\dog.mp4")

while 1: 
    # .read le frame ve true false değeri dönüyor true false değerini _ şeklinde tutuyoruz
    _,frame = cap.read()
    # nesnelerin izini sürmek için hsv tipine döndürmek gerekiyor
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # videoda beyaz nesnelerin takibi yapılacağından renk aralığını belirlemk gerekiyor
    # hsv için beyaz renk aralığını aşağıda alıyoruz
    # duyarlılık 15 olarak belirlendi
    sensitivity = 15
    lower_white = np.array([0,0,255-sensitivity]) 
    upper_white = np.array([255,sensitivity,255])
    # inRange metoduyla girilen hsv görüntüsüne girilen sınırlar için maske uyguluyor
    mask = cv2.inRange(hsv,lower_white,upper_white)
    # bitwise_and metodunda bir framei kullanıp diğerini kazıdığı için içine iki tane frame mask parametresi girildi
    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
