import cv2
import numpy as np

path_img = "D:\\Resimler\\starwars.jpg"
path_temp = "D:\\Resimler\\starwars2.jpg"

img = cv2.imread(path_img)
# template imread ,0 olarak girildiği için gri formata okuyor  
# , cv2.IMREAD_GRAYSCALE olarak da kullanılabilir
template = cv2.imread(path_temp,0)
# gri tonlarda olduğunu template.shape değeri 2 elemanlı olduğu zaman anlaşılabilir
 
w,h = template.shape[::-1]

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# matchTemplate fonksiyonuna başlıca sırasıyla eşleştirme yapılacak resim , şablon giriliyor
result = cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)
# result değerleri ne kadar 1 e yakınsa şablona o kadar yakınlaşıyor
location = np.where(result >= 0.95)

# anlamlı kordinatlar elde etmek için uygulanıyor
for point in zip(*location[::-1]):
    cv2.rectangle(img, point,(point[0]+w,point[1]+h),(0,255,0),3)




cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()