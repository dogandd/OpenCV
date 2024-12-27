# ROI --> region of interest --> ilgi alanı
import cv2

img = cv2.imread("resim.jpg")

# print(img.shape)
# resimde incelemek istediğimiz alanı çıkarıyoruz
roi = img[200:700,350:750]

cv2.imshow("image", img)
cv2.imshow("ROI",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()