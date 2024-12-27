import cv2
import numpy as np

circle = np.zeros((512,512,3), np.uint8,) + 255
cv2.circle(circle, (256,256), 60 ,(255,0,0), -1)

rectangle = np.zeros((512,512,3), np.uint8,) + 255
cv2.rectangle(rectangle, (150,150), (350, 350), (0,0,255), -1)

# resimleri toplamak için add fonksiyonu kullanılıyor
# resimlerdeki toplama işlemlerinde her iki resimde aynı komdaki piksellerin renk değerlerinin toplayıp aynı piksele yazıyor
add = cv2.add(circle,rectangle)
print(add[256,256])
cv2.imshow("add",add)
cv2.imshow("rectange", rectangle)
cv2.imshow("circle", circle)

cv2.waitKey(0)
cv2.destroyAllWindows()