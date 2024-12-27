import cv2
import numpy
import matplotlib

# cv2 kütüphanesiyle birlikte resmin matematiksel değerlerini okuyoruz
# imread fonksiyonuyla okumak istenilen resmin adı () içerisine yazılır
# img = cv2.imread("resim.jpg",0) şeklinde yazılıyorsa resmi gri tonlarda okur
img = cv2.imread("resim.jpg")
# img değişkenine atanılan resimin matematiksel değerleri yazdırılır
# print(img)


# herhangi bir yerdeki resmi çekmek için resmin bulunduğu adres "" içine yazılıyor yazılıyor
# açılan pencerenin boyutuyla oynayabilmek için namedwindow fonksiyonunda cv2.WINDOW_NORMAL kullanıldı
# açtığımız fonksiyonun boyutu değiştirilebilir olması için imshow fonksiyonunda verilen isimle aynı isimde olması lazım
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
# resmi imshow fonksiyonuyla görüntülenir
cv2.imshow("Image",img)
# resmi kaydetmek için vc2.imwriter() fonksiyonu
# resmi istenilen yere kaydetmek için "" içine istenilen adres yazılır
cv2.imwrite("Image.jpg",img)
# waitkey fonksiyonunun içine girilen değer kadar ekranda tutulur (milisaniye)
cv2.waitKey(0)
# tüm pencereleri kapatmak için kullanıllır
cv2.destroyAllWindows()