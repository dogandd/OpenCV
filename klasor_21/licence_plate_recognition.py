import cv2
import numpy as np
import pytesseract
import imutils

img = cv2.imread("D:\\Resimler\\licence_plate")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# bilateral fitre uygulanıyor
filtered = cv2.bilateralFilter(gray,6,250,250 )
# kenarlar belirleniyor
edged = cv2.Canny(filtered,30,200)

# cotourlar belirlendi
contours = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)
# contourlar sıralanıyor
cnts = sorted(cnts,key=cv2.contourArea,reverse=True)[:10]
screen = None

for c in cnts:
    epsilon = 0.018*cv2.arcLength(c,True)
    # contourlara daha çok yaklaşılıyor
    approx = cv2.approxPolyDP(c,epsilon,True)
    # kenar sayısı 4 ise plaka tespit edilmiş demektir 
    if len(approx) == 4:
        screen = approx
        break

# plaka dışı her yer siyah yapılıyor
mask = np.zeros(gray.shape,np.uint8)
# plaka alanı beyaz yapıldı
new_img = cv2.drawContours(mask,[screen],0,(255,255,255),-1)
# yazı plaka alanına eklendi
new_img = cv2.bitwise_and(img,img,mask = mask)

# beyaz kısımların konumları tutuldu
(x,y) = np.where(mask == 255)
# min max (x,y) değerleri tutuldu 
(topx,topy) = (np.min(x),np.min(y))
(bottomx,bottomy) = (np.max(x),np.max(y))

# tutulan değerlerden kırpma işlemi yaptı plakayı çıkardı
cropped = gray[topx:bottomx + 1,topy:bottomy + 1]
print(np.where(mask == 255))

# plakayı okudu
text = pytesseract.image_to_string(cropped,lang = "eng")
print("detected text:",text)


cv2.waitKey(0)
cv2.destroyAllWindows()