import sys,os
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sciMat

srcName = sys.argv[1]
pmat = sciMat.loadmat(srcName)
a=pmat['energy']
print a[-1]
b=abs(a[1:-1]-a[0:-2])
fig=plt.figure(figsize=(15,10))
fig.patch.set_color('W')# set the background color

plt.subplot(1,2,1)
plt.loglog(b,linewidth=2)
plt.xlabel('Steps',fontsize=15)
plt.ylabel('$\Delta Energy(k_BT)$',fontsize=15)
plt.grid()
plt.subplot(1,2,2)
plt.plot(pmat['energy'],linewidth=2)
plt.xlabel('Steps',fontsize=15)
plt.ylabel('$Energy(k_BT)$',fontsize=15)
plt.grid()
plt.show()

