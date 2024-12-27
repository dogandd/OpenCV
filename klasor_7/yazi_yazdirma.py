import numpy as np
import cv2

# zeros belirli bir alana siyah tuval oluşturur
canvas = np.zeros((512,512,3), dtype=np.uint8) + 255
# fontlerı oluşturuluyor
font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
# yazı yazdırmak için putText fonksiyonunu kulllanıyoruz
# içine sırayla oluşturduğumuz tuvali , yazının başlangıç konumunu, fontu, fontun büyüklüğü,yazının tipi
cv2.putText(canvas, "OpenCV", (30,100), font1, 4, (0,0,0), cv2.LINE_AA)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
