import cv2
import numpy as np

cap = cv2.VideoCapture("D:\\Videolar\\car.mp4")
# createBackgroundSubtractorMOG2 fonksiyonuna history olarak frame değeri giriliyor
subtractor = cv2.createBackgroundSubtractorMOG2(history = 100, varThreshold = 50, detectShadows = True)



while 1:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    # apply fonksiyonuyla subtractordaki özellikleri her bir frame uyguluyor 
    mask = subtractor.apply(frame)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()