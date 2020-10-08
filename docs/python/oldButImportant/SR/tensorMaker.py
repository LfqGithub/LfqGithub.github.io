import numpy as np


A=np.diag((0.5,-0.25,-0.25))
lambdaAll,vectorAll=np.linalg.eig(A)
# A*x=lambda*x
for i in range(3):  
    if (np.dot(A,vectorAll[:][i])==lambdaAll[i]*vectorAll[:][i]).all():
        print('right')
    else:
        print('wrong')

print(A)
print(lambdaAll)
print(vectorAll)
