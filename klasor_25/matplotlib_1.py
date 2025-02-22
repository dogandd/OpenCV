import matplotlib.pyplot as plt
import numpy as np

# arange fonksiyonu numpy.ndarray tipinde bir dizi oluşturur
# 0 dan başlayıp girilen sayıya kadar elemanlardan dizi oluşturur
x = np.arange(5)
y = x
print(x)
print(type(x))

# plot fonksiyonuyla fonksiyon grafiği çiziliyor
plt.plot(x,y,"o--")
plt.plot(x,-y)
plt.plot(-x,y,"--")

plt.show()