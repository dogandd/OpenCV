import cv2
import numpy as np

img_median = cv2.imread("D:\\Resimler\\_median.png")
img_filter = cv2.imread("D:\\Resimler\\_filter.png")
img_bilateral = cv2.imread("D:\\Resimler\\_bilateral.png")

# blur ekleniyor pozitif tek sayı olmak zorunda
blur = cv2.blur(img_filter,(5,5))
blur2 = cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)
blur_m = cv2.medianBlur(img_median,9)
blur_b = cv2.bilateralFilter(img_bilateral, 9,95,75)

cv2.imshow("orijinal", img_filter )
cv2.imshow("blur", blur)
cv2.imshow("orijinal median", img_median )
cv2.imshow("blur median", blur_m)
cv2.imshow("orijinal bilateral", img_bilateral )
cv2.imshow("blur bilateral", blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()