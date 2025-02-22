import numpy as np

# çok boyutlu diziler
# çok boyutlu dizi oluşturulması için [] içerisinde [] olarak dizi eklenir
y = np.array([[1,2,3],[4,5,6]],np.uint16)

print(y)
print("------")
print(y[0]);print(y[0,0]);print(y[0,2])
print(y[1]);print(y[1,1]);print(y[1,2])

# :,0 ifadesinde : hepsini tara 0. idisteki değeri al demek 
print(y[:,0]);print(y[:,1]);print(y[:,2])
# 0,: ifadesinde : 0. indisi tara anlamında 
print(y[0,:]);print(y[1,:])