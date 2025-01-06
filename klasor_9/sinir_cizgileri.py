import cv2

img = cv2.imread("D:\\Resimler\\contour1.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
# threshold yaparken iki değişkene eşitliyoruz ilk değişken hiç bir zaman kullanılmadığı için "_" olarak atıyoruz

_,thrsh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

# findCountours metodu toplamda 3 değer döndürür
# dönen 3 değerden ilk ve sonuncu değerler bu uygulama için hiç kullanmayacağımız değerler olduğu için "_" ile gösterildi
# fonksiyona girilen son iki parametrenin bu şekilde girilmesi daha sağlıklı bir program sağlar
contours,__ = cv2.findContours(thrsh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# bulunan noktaların kordinatları yazdırıyoruz
# print(countours)

# bulunan konumlarla çizim yapmak için drawCountours kullanılır
# 5 parametre alıyor sırayla resim, çizim yapılacak kordinatlar, -1, renkler, kalınlık
cv2.drawContours(img,contours,-1,(0,0,255),3)
cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()