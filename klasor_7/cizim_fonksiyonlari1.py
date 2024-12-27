import cv2
import numpy as np

# zeros fonksiyonuna girilen parametrelerle siyah bir portre oluşturur
# 3. parametre kanal verisidir renkli çizim yapmaya yarıyor
# uint8 çicim yapıldığında kullanılan veri tipidir
# + 255 ile tüm değerlerine 255 ekliyoruz ve bu sayede pencere beyaz oluyor
canvas = np.zeros((512,512,3), dtype=np.uint8) + 255

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

