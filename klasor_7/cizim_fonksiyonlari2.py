import numpy as np
import cv2

# zeros belirli bir alana siyah tuval oluşturur
canvas = np.zeros((512,512,3), dtype=np.uint8) + 255
# line fonksiyonuna önce oluşturduğumuz pencereyi veriyoruz
# sırasıyla başlangıç ve bitiş noktası belirliyoruz
# thickness la birlikte çizginin kalınlığını belirliyoruz
cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5)
cv2.line(canvas, (100,50), (200,250), (0,0,255), thickness=5)

# dikdörtgen oluşturmak için rectangle fonksiyonunu kullanılır
# konum girilirken önce sol üst sonra sağ alt köşelerinin konumu girilir
# dikdörtgenin içinin dolu olması için thickness = -1 olmalı
cv2.rectangle(canvas, (20,20), (50,50), (0,255,0), thickness=-1)
cv2.rectangle(canvas, (50,50), (150,150), (0,255,0), thickness=-1)

# çember çizmek için circle fonksiyonu oluşturulur
# ilk çemberin meerkezinin konumu sonra yarı çapı girilir
cv2.circle(canvas, (250,250), 100, (0,0,255), thickness=-1)

# üçgen için ayrı özel bir fonksiyon yok onun yerine üçtane çizgi çekilir
p1 = (100,200)
p2 = (50,50)
p3 = (300,100)
renk = (0,0,0)
cv2.line(canvas,p1,p2,renk,thickness=5)
cv2.line(canvas,p2,p3,renk,thickness=5)
cv2.line(canvas,p3,p1,renk,thickness=5)

# çizgileri tek tek tanımlamak yerine polylines kullanılabilir
points = np.array([[[110,200], [330,200], [290, 220], [100,100]]])
# şeklin kapalı bir şekil olması için True girildi
cv2.polylines(canvas, [points], True, (0,0,100), 5)

# elips çizmek için  ellipse fonksiyonu kullanılır
# sırayla elipsin (merkezi),(genişlik,yükseklik), yatay eksenle yapılan açı, hangi dereceler arasında çizim yapılacağı,renk,kalınlık girilir
cv2.ellipse(canvas, (300, 300), (80, 20), 0, 0 ,360, (255,255,0), -1)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
