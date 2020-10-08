import numpy as np
x=np.diag((1,3,9))
print('A',x)
a,b=np.linalg.eig(x)
print('lambda',a)
print('vector',b)

for i in range(3):
    print(np.dot(x,b[:][i])-a[i]*b[:][i])
