import numpy as np
# empty fonksiyonu rastgele sayılarla belirlenen ölçülerde matris oluşturur
x = np.empty([3,3],np.uint16)
print("x:",x)
print("-------")


# full fonksiyonuyla matrisin boyutları girilerek hangi sayıyla doldurulmak isteniyorsa o sayılarla bir matris oluşturuyor
y = np.full((10,10),dtype=np.int16,fill_value= 10)
print("y:",y)
print("-------")

# ones fonksiyonu 1 lerden oluşan bir matris oluşturur
z = np.ones((2,5,5),dtype=np.int8)
print("z:",z)

# zeros fonksiyonu 0 lardan oluşan bir matris oluşturur
j = np.zeros((2,5,5),dtype=np.int8)
print("j:",j)