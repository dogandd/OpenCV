import cv2
import numpy as np

img1 = cv2.imread("D:\\Resimler\\bitwise_1.png")
img2 = cv2.imread("D:\\Resimler\\bitwise_2.png")

# bit düzeyinde ve işlemlerini gerçekleştirmek için bitwise_and kullanılır
# siyahlar 0 a karşılık gelir beyazlar 1 e karşılık gelir
# ikiresimde karşılıklı noktalar mantıksal ve bağlacıyla karşılaştırılıyor
bit_and = cv2.bitwise_and(img2,img1)
# bitwise_or ifadesi karşılıklı değerler 0sa 0 yapar diğer değerlerde 1 olarak kabul eder 
bit_or = cv2.bitwise_or(img1,img2) 
# bitwise_not ifadesiyle resimdeki değerleri tam tersine çeviriyor 1 --> 0    0 --> 1 oluyor
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)
# bitwise_xor ifadesi aynı iki değer karşılaşırsa 0 verir farklı değerler karşılaşırsa 1 verir
bit_xor = cv2.bitwise_xor(img1,img2)


cv2.imshow("bit_not",bit_not)
cv2.imshow("bit_not2",bit_not2)
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bitwise_1",img1)
cv2.imshow("bitwise_2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
