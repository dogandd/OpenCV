import cv2
import numpy as np

img = cv2.imread("D:\\Resimler\\contour.png")
img1 = cv2.imread("D:\\Resimler\\text.png")

# alınan resimler griye çevriliyor
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# gray i direk böyle kullanamadığım için önce float32 tipine döndürülmesi gerekir
gray = np.float32(gray)

# remin köşelerini goodFeaturesToTrack metoduyla buluyoruz
# metod içine 4 adet parametre alır bunlar sırasıyla resim, yakalayacağı köşe sayısı, kalite değeri(deneysel olarak 0.01 bulunmuş), köşeler arası min mesafe
corner = cv2.goodFeaturesToTrack(gray,1000,0.01,10)
# çemberler çizerken float sayılar kullanamıyoruz bu yüzden int64 tipine dönüşüm yapılması gerekir
corners = np.int64(corner)

# corners ın içindeki değerleri tek tek çekiyor
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img1, (x, y), 3, (0,0,255), -1)

cv2.imshow("Corners", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()