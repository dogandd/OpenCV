import numpy as np
import matplotlib.pyplot as plt

path = "D:\\Resimler\\smile.jpg"
img = plt.imread(path)

print(img)
# min en düşük değeri verir
print("min value:",img.min())
# max en yüksek değeri verir 
print("max value:",img.max())
# ortalamasını alır
print("mean:",img.mean())
# medyan değeri hesaplar
print("median:",np.median(img))
# avarage belirtilen eksen boyu ağırlıklı ortalamayı bulur
print("average:",np.average(img))
print("mean1:",np.mean(img))
