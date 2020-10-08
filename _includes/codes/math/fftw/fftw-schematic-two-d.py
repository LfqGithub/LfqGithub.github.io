# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

period=1
fftw_size=100
sample_rate=fftw_size/(2*np.pi*period) # sample points
fig, ax=plt.subplots(1,2,figsize=(4,3))

tx=np.arange(0,2*np.pi*period,1.0/sample_rate)
ty=np.arange(0,2*np.pi*period,1.0/sample_rate)

t_x,t_y=np.meshgrid(tx,ty)

z=np.sin(2*t_x)+np.sin(4*t_y) # sine-wave

# z=np.zeros((fftw_size,fftw_size))
# z=[::10,::10]=1 # squarewave


zf=2*np.abs(np.fft.fft2(z))/(fftw_size**2)

zf_shifted=np.fft.fftshift(zf)

xylim=sample_rate/2.0

im=ax[0].imshow(z,cmap ='gray')
divider=make_axes_locatable(ax[0])
cax =divider.append_axes("right",size="5%",pad=0.05)
fig.colorbar(im,ax=ax[0],cax=cax)

im=ax[1].imshow(zf_shifted,extent=[-xylim, xylim, -xylim, xylim],cmap ='gray')

divider=make_axes_locatable(ax[1])
cax =divider.append_axes("right",size="5%",pad=0.05)
fig.colorbar(im,ax=ax[1],cax=cax)

plt.tight_layout()
plt.show()
#plt.savefig("fftw-schematic-2d.png", dpi=300)
