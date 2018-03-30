import numpy as np
a=[[[11,12,13],[14,15,16]],[[21,22,23],[24,25,26]]]
A=np.array(a)
print(A.shape)
B=A.reshape(4,3)
print(B.shape)