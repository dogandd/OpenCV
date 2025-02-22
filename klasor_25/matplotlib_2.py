import matplotlib.pyplot as plt
import numpy as np

N = 11
# linspace fonksiyonu girilen aralıkta (0,10) birbiriyle eşit uzaklıkta olan N tane sayı verir
x = np.linspace(0,10,N)
print(x)
y = x
plt.plot(x,y,"o--")
plt.show()


x = [2,5,12,7,3]
plt.plot(x)
plt.show()

# plot fonksiyonunun içine grafiğin fonksiyonu yazılabilir
x = [1,2,3,4,5]
plt.plot(x,[y**2 for y in x])
plt.show()