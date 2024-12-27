import cv2
import numpy as np

img = cv2.imread("resim.jpg")
# remin ölçülerini alıyor
dimension = img.shape
print(dimension)
# 150 ye 200 pikselindeki BGR değerlerini color değişkenine atıyor
# resmin boyutunun dışında bir piksel aranırsa index hatası alınır
color = img[150,200]
print("BGR:",color)

# herhangi bir konumdaki mavi değeri için aşağıdaki içlem yapılır
blue = img[150,200,0]
print("blue:", blue)
# herhangi bir konumdaki yeşil değeri için aşağıdaki içlem yapılır
green = img[150,200,1]
print("blue:", green)
# herhangi bir konumdaki kırmızı değeri için aşağıdaki içlem yapılır
red = img[150,200,2]
print("blue:", red)

# herhangi bir pikseldeki bir rengin değiştirilmesi için o piksele yeni renk değeri verilir
img[150,200,0] = 15
print("new blue:",img[150,200,0])
# piksel rengini değiştimek için bu şekilde de kullanılabilir
# blue1 = img.item(150,200,0)
# print("blue1:",blue1)
# img.itemset((150,200,0),193)
# print("new blue1:",img[150,200,0])
cv2.imshow("resim.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()