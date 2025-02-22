# ndarray ---> n-dimesioanl array
# uint --> unsigned int (negatif sayılar bulunmaz)
import numpy as np
x = np.array([[[-2,-1,0,5],[9,4,5,-7]],[[-2,-1,0,5],[9,4,5,-7]]],np.int16)
print(x)
# shape matrisin kaça kaç matris olduğunu verir
print(x.shape)
# ndim matrisin boyutunu verir
print(x.ndim)
# dtype veri tipini verir
print(x.dtype)
# size eleman sayısını veriyor
print(x.size)
# T matrisin transpozunu alır
print(x.T)
