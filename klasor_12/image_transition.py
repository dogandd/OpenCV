import cv2
import numpy as np

def nothing(x):
    pass

img1 = cv2.imread("D:\\Resimler\\aircraft.jpg")
img2 = cv2.imread("D:\\Resimler\\balls.jpg")

img1 = cv2.resize(img1,(640,480))
img2 = cv2.resize(img2,(640,480))

# görüntülenecek olan fotoğrafların ağırlığı belirlenir
output = cv2.addWeighted(img1,0.5,img2,0.5,0)
windowName = "Transition Program"
cv2.namedWindow(windowName)

cv2.createTrackbar("Alpha-Beta",windowName,0,1000,nothing)

# anlık olarak trackbarda gösterilen değere göre fotoğrafların ağırlığı değişeceği için while kullanılır
while 1:
    cv2.imshow(windowName,output)
    # trackbar değerini fotoğraf yoğunluğu olarak kullanmak için alpha değerinde tutuyor 
    alpha = cv2.getTrackbarPos("Alpha-Beta",windowName)/1000
    beta = 1-alpha
    output = cv2.addWeighted(img1,alpha,img2,beta,0)
    

    if cv2.waitKey(5) == 27:
        break

cv2.destroyAllWindows()