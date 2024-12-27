import cv2

cv2.namedWindow("image",cv2.WINDOW_NORMAL)  
img = cv2.imread("resim.jpg")

# resmi yeniden boyutlandırmak için aşağıdaki şekilde kullanılır
img = cv2.resize(img,(640,280))

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()