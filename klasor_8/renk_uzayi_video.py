import cv2

cap = cv2.VideoCapture("D:\\Videolar\\antalya.mp4")

while True:
    ret, frame = cap.read()
    # videonun framelerini BGR dan GRAy e dönüştürüyor
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False:
        break

    cv2.imshow("video",frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()