import cv2

cap = cv2.VideoCapture("D:\\Videolar\\line.mp4")
circles = []
def mouse(event,x,y,flags,params):
    # EVENT_LBUTTONDOWN ile mouseun sol tuşuna basıldığını kontrol eder
    # mouse tıklandığı yerin konumlarını alır 
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))

# daire oluşturulacak pencere açıllıyor
cv2.namedWindow("Frame")
# setMouseCallback fonksiyonuyla girilen parametreler sırayla işlem yapacağı pencere ismi,yapılacak işlem
cv2.setMouseCallback("Frame",mouse)

while 1:
    _,frame = cap.read()
    frame = cv2.resize(frame,(400,300))
    # mouse konumunun içinden merkezi alır ve frame de o konuma daire oluşturur
    for center in circles:
        cv2.circle(frame,center,20,(255,0,0),-1)
    
    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("h"):
        circles = []

cap.release()
cv2.destroyAllWindows()