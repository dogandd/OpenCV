import cv2
import numpy as np

path1 = "D:\\Resimler\\aircraft.jpg"
path2 = "D:\\Resimler\\aircraft1.jpg"

img1 = cv2.imread(path1)

img1 = cv2.resize(img1,(640,550))

img2 = cv2.imread(path2)
img2 = cv2.resize(img2,(640,550))

img3 = cv2.medianBlur(img1,7)

if img1.shape == img2.shape:
    print("same size")
else:
    print("not same")

# subtract fonksiyonu iki resmi karşılaştırır ve farklı olan yerlerin rengini değiştirir
diff = cv2.subtract(img1,img3)
b,g,r = cv2.split(diff)

# countNonZero fonksiyonu girilen değişkende 0dan farklı değerler var mı onu kontrol eder
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0 :
    print("completerly equal")
else:
    print("not completerly equal")
    


# iki resim arasında fark olmadığı için siyah ekran olarak bir çıktı alınıyor
cv2.imshow("diff",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()