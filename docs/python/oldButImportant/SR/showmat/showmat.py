#program

import sys,os
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sciMat

srcName = sys.argv[1]
pmat = sciMat.loadmat(srcName)
linksDens=pmat['linksDens'][0:,1,1,0:]
links_num=len(linksDens[1,0:])
print links_num
fig=plt.figure(figsize=(15,10))
fig.patch.set_color('W')# set the background color
for i in range(1,links_num):
	plt.plot(linksDens[0:,i],label='links'+str(i),linewidth=2)


plt.xlabel('Lattice',fontsize=15)
plt.ylabel('Density',fontsize=15)
plt.legend()
plt.grid()
plt.show()

