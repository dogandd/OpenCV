import cv2
# resim oluşurken bir takım interpolasyonların önüne geçmek için inter tanımlıyoruz
def resizewithAspectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):
    dimension = None
    # resim boyutuna .shape[] fonksiyonuyla ulaşılır
    # shape in dödürdüğü değerlerden en başından ikincisine kadar ulaşmak istediğimiz için [:2] girildi
    
    (h,w) = img.shape[:2]

    if width is None and height is None:
        return img
    
    # en veya boy uzunluğu biliniyorsa 
    # bilinen uzunluktan ilk haline oranı çıkarılır
    # bilinmeyen uzunluğu o orana göre çıkarır
    if width is None :
        r = height/float(h)
        dimension = (int(w*r), height)
    else:
        r = width / float(w)
        dimension = (width, int(h*r))
    
    return cv2.resize(img, dimension, interpolation = inter)

img = cv2.imread("resim.jpg")
img1 = resizewithAspectRatio(img, width = None, height = 400, inter = cv2.INTER_AREA)
cv2.imshow("Orijinal",img)
cv2.imshow("Resized",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()