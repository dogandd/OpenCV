import cv2
import matplotlib.pyplot as plt

path = "D:\\Resimler\\smile.jpg"
img = cv2.imread(path) # cv2 kütüphanesi resmi BGR olarak okur
# plt kütüphanesi resmi RGB yansıtır bu yüzden resim olması gerektiği gibi gözükmez
# buyüzden resmin formtı değiştiriliyor
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# resim farklı formatta sergilenmek isteniyorsa o farmatta anahtar kelimelri girilir
plt.imshow(img,cmap='gray',interpolation='BICUBIC')
plt.show()
