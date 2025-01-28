import cv2
import numpy as np 

video = cv2.VideoCapture("D:\\Videolar\\line.mp4")

while True:

    ret,frame = video.read()
    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # sarı renk için min ve max hsv değerleri alındı 
    lower_yellow = np.array([18,94,140],np.uint8)
    upper_yellow = np.array([48,255,255],np.uint8)

    # sarı şerit belirlendi
    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    # sarı şeritin köşeleri belirlendi
    edges = cv2.Canny(mask,75,250)
    
    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200)

    for line in lines:
        (x1,y1,x2,y2) = line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
    cv2.imshow("img",frame)


    if cv2.waitKey(20) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()