import numpy as np
import matplotlib.pyplot as plt

path = "D:\\Resimler\\map.jpg"
img = plt.imread(path)

r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

output = np.dstack((r,g,b))
plt.imshow(output)
plt.show()




"""
output = [img,r,g,b]
titles = ["image","red","green","blue"]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.axis("off")
    plt.title(titles[i])
    if i == 0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i],cmap='gray')
    plt.show()"""