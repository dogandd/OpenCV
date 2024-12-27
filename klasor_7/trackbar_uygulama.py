import cv2
import numpy as np



# boş fonksiyon oluşturuluyor
def nothing(x):
    pass


img  = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("image")

# createTrackbar() fonksiyonuyla trackbar oluşturuluyor
# parametreler sırasıyla giriliyor kızağın adı, kızağın yerleşeceği pencerenin adı, kızağın başlangıç ve bitiş değerleri
# createTrackbar fonksiyonunun hatasız çalışması için boş fonksiyonun girilmesi lazım
# kızakların adları R(Red), G(Green), B(Blue) 
cv2.createTrackbar("R","image", 0, 255, nothing)
cv2.createTrackbar("G","image", 0, 255, nothing)
cv2.createTrackbar("B","image", 0, 255, nothing)
# switch oluşturuluyor
switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch,"image", 0, 1, nothing)


while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    # kızakların konumunu almak için getTrackbarPos fonksiyonu kullanılıyor
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image") 
    s = cv2.getTrackbarPos(switch, "image")
    if s == 0:
        img[:] = [0,0,0]
    if s == 1:
        img[:] = [b,g,r]
    # tüm piksel değerindeki renklere erişmek istediğimizi gönderiyoruz
    # img[:] = [b, g, r]


cv2.waitKey(0)
cv2.destroyAllWindows()
