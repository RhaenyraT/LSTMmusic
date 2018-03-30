import numpy as np
a=np.array([[4, 3], [2, 1]])
b= np.zeros((a.shape[0], a.shape[1]), dtype=np.float32)
print(a)
for row in range(0,a.shape[0]):
    maxi=np.argmax(a[row,:])
    b[row,maxi]=1
