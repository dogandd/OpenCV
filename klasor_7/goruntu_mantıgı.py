import cv2
import numpy as np

# img = np.zeros((10,10,3),np.uint8)
# pikselleri tek tek boyuyoruz
# img[0,0] = (255,255,255)
# img[0,1] = (255,255,200)
# img[0,2] = (255,255,150)
# img[0,3] = (255,255,100)

# 3 kanal verisi renkli resimlerde kulanıldığı için siyah beyaz resim elde etmek için 3 kanal verisini kaldırıyoruz
img = np.zeros((10,10), np.uint8)
img[0,0] = (255,255,255)
img[0,1] = (255,255,200)
img[0,2] = (255,255,150)
img[0,3] = (255,255,100)

# yeniden boyutlandırmak için resize kullanılıyor
img  = cv2.resize(img, (1000,1000), interpolation=cv2.INTER_AREA)

cv2.imshow("canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()