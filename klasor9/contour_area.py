import cv2

img = cv2.imread("D:\\Resimler\\contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ter, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# contours da kullanmak istediğimiz değer cnt olarak tutuyoruz
cnt = contours[0] 
# contourArea metoduna cnt yi vererek alan hesaplıyoruz
area = cv2.contourArea(cnt)
print(area)
# moments metoduyla oluşturulan Mde m00 keyinde de alan buluyoruz
M = cv2.moments(cnt)
print(M["m00"])

perimeter = cv2.arcLength(cnt,True)
print(perimeter)


cv2.waitKey(0)
cv2.destroyAllWindows()