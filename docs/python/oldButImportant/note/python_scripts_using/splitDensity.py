#program
#  plot the density of every single blocks
#usage
#  python splitDensity.py xxx.mat A/B, A mean plot the A(coil) density, B means plot B(rod) density 
#history 
#  Mon May 30 23:53:10 CST 2016 liufaqiang
import sys,os
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sciMat

srcName = sys.argv[1]
pmat = sciMat.loadmat(srcName)
ADensSplit=pmat['ADensSplit'][0:,1,1,0:]
BDensSplit=pmat['BDensSplit'][0:,1,1,0:]
block_num=len(ADensSplit[1,0:])
print block_num
fig=plt.figure(figsize=(15,10))
fig.patch.set_color('W')# set the background color
if sys.argv[2]=='A':
	for i in range(1,block_num):
		plt.plot(ADensSplit[0:,2],label=str(i),linewidth=2)
else:
	for i in range(1,block_num):
		plt.plot(BDensSplit[0:,2],label=str(i),linewidth=2)

#plt.plot(densityA,label=str(i),linewidth=2)
#plt.plot(densityB,label='Rod',linewidth=2)
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
plt.xlabel('Lattice',fontsize=15)
plt.ylabel('Density',fontsize=15)
plt.legend()
plt.grid()
plt.show()

