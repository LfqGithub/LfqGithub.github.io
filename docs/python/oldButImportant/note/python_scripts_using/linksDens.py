import sys,os
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import scipy.io as sciMat

srcName = sys.argv[1]
pmat = sciMat.loadmat(srcName,squeeze_me=1)
linksDens=pmat['linksDens']
densityA=pmat['ADens']
densityB=pmat['BDens']
print len(densityB)
size=pmat['sizeZ']
print size
dim=pmat['dim_z']
print dim
sizeDivideDim=size/float(dim)
print sizeDivideDim
x_coordinate=np.arange(0,size,sizeDivideDim)
print len(x_coordinate)
print x_coordinate
fig=plt.figure(figsize=(15,10))
#fig.patch.set_color('W')# set the background color
plt.plot(linksDens[1:dim,sys.argv[2]],label='linksDens',linewidth=3)
#plt.plot(x_coordinate,densityA,label='Coil',linewidth=3)
#plt.plot(x_coordinate,densityB,label='Rod',linewidth=3)
#fig=plt.figure(figsize=(15,10))
#fig.patch.set_color('W')# set the background color
#fig=plt.figure(figsize=(15,10))
#fig.patch.set_color('W')# set the background color
#b=abs(a[1:-1]-a[0:-2])
#fig=plt.figure(figsize=(15,10))
#fig.patch.set_color('W')# set the background color
#
#plt.subplot(1,2,1)
#plt.loglog(b,linewidth=2)
#plt.xlabel('Steps',fontsize=15)
#plt.ylabel('$\Delta$ Energy($k_BT$)',fontsize=15)
#plt.grid()
#plt.subplot(1,2,2)
#plt.plot(pmat['energy'],linewidth=2)
xmin,xmax=x_coordinate.min(),x_coordinate.max()
#ymin,ymax=min(densityB.min(),densityA.min()),max(densityB.max(),densityA.max())
#dx=(xmax-xmin)*0.1
#dy=(ymax-ymin)*0.1
#xlim(xmin-dx,xmax+dx)
#ylim(ymin-dy,ymax+dy)
plt.xlabel('$L(R_g)$',fontsize=15)
plt.ylabel('$links_Density$',fontsize=15)
plt.legend()
plt.grid()
plt.show()

