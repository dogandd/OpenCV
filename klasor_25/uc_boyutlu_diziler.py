import numpy as np
# üç boyutlu diziler bu şekilde oluşturulur
x = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],np.uint16)
print(x)
print(x[0,0,0])
print(x[0,1,0])
print(x[1,1,1])