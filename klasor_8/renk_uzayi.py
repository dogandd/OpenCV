import cv2

img_bgr = cv2.imread("resim.jpg")
# cvtColor fonksiyonuyla girilen resimin renk uzayının değişmesini sagşar
# ilk parametre olarak resim girilir diğer parametre olarak istenilen resim uzayı dönüşüm ifadesi girilir
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

cv2.imshow("image BGR", img_bgr)
cv2.imshow("image RGB", img_rgb)
cv2.imshow("image HSV", img_hsv)
cv2.imshow("image GRAY", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()