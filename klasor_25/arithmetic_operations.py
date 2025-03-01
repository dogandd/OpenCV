import numpy as np
import matplotlib.pyplot as plt

path = "D:\\Resimler\\map.jpg"
img = plt.imread(path)

# birden çok grafiği birlikte göstermek için subplot kullanılır (4 satır, 2 sütun,1.grafik) gibi
plt.subplot(4,2,1)
plt.title("original image")
plt.imshow(img)

plt.subplot(4,2,2)
plt.title("image + image")
plt.imshow(img + img)

plt.subplot(4,2,3)
plt.title("image - image")
plt.imshow(img - img)

plt.subplot(4,2,4)
plt.title("np.flip(img,0)")
plt.imshow(np.flip(img,0))# ikinci parametre değerliri 0,1,2 

plt.subplot(4,2,5)
plt.title("np.flip(img,1)")
plt.imshow(np.flip(img,1))

plt.subplot(4,2,6)
plt.title("np.flip(img,2)")
plt.imshow(np.flip(img,2))

plt.subplot(4,2,7)
plt.title("np.fliplr") # left to right
plt.imshow(np.fliplr(img))

plt.subplot(4,2,8)
plt.title("np.flipud")
plt.imshow(np.flipud(img)) # updown









plt.show()