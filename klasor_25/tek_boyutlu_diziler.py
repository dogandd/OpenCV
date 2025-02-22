import numpy as np

# tek boyutlu diziler
# np.array() fonksiyonu dizi oluşturur
# np.uint16 ile dizinin data tipi belirtiliyor
x = np.array([1,2,3],np.uint16)
print(x)
print(type(x))
print(x[0]);print(x[1]);print(x[2])

print(x[-1])
print(x[-2])
print(x[-3])