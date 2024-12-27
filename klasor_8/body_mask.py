import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def nothing():
    pass

cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar", 500, 500)

cv2.createTrackbar("Lower - H", "trackbar", 0, 100, nothing)
cv2.createTrackbar("Lower - S", "trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower - V", "trackbar", 0, 255, nothing)

cv2.createTrackbar("Upper - H", "trackbar", 0, 100, nothing)
cv2.createTrackbar("Upper - S", "trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper - V", "trackbar", 0, 255, nothing)

cv2.setTrackbarPos("Upper - H", "trackbar", 100)
cv2.setTrackbarPos("Upper - S", "trackbar", 255)
cv2.setTrackbarPos("Upper - V", "trackbar", 255)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower - H", "trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S", "trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V", "trackbar")
    upper_h = cv2.getTrackbarPos("Upper - H", "trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S", "trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V", "trackbar")
    
    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])
     
    mask = cv2.inRange(frame_hsv, lower_color, upper_color)

    cv2.imshow("orijinal", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()