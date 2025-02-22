import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
plt.plot(x,[y**2 for y in x])
plt.plot(x,[y**3 for y in x])
plt.plot(x,2*x)
plt.plot(x,5.2*x)

#  legend foksiyonuyla grafiğin fonksiyonu hangi çizgi olduğu belirlenir konumunu da girilen loc değeriyle belirleriz
plt.legend(['x**2','x**3','x*2','x*5.2'],loc = 'upper right')

# grid fonksiyonu grafiğe ızgara ekler
plt.grid(True)

# xlabel ve ylabel fonksiyonları x ve y eksenlerini adlandırır
plt.xlabel('x = np.arange(3)')
plt.ylabel('y = f(x)')

# axis fonksiyonu x ve y eksenlerinde maks min noktaları gösterir ve grafiği istenilen aralıkta ayarlayabilir 
plt.axis([0,2,0,10])
# title fonksiyonu grafiğe başlık ekler
plt.title("simple Plot")

# savefig fonksiyonu grafiği istenilen adrese kaydetmeye yarar
plt.savefig('D:\\plt.png')

plt.show()
