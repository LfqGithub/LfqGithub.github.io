import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

times=4

period=10

fftw_size=1000 

sample_rate=fftw_size/(2*np.pi*period)

#fig, ax=plt.subplots(1,2,figsize=(4,3))
fig = plt.figure()


tx=np.arange(0,period*2*np.pi,1/sample_rate)
ty=np.arange(0,period*2*np.pi,1/sample_rate)

t_x,t_y=np.meshgrid(tx,ty)

tem_z=np.sin(2*t_x)+np.sin(4*t_y)
z=np.vstack((tem_z,tem_z))

zf=np.abs(np.fft.fft2(z))/(fftw_size**2)

zf_shifted=np.fft.fftshift(zf)

freqs_x=np.linspace(0, sample_rate/2, fftw_size/2+1)
freqs_y=np.linspace(0, sample_rate/2, fftw_size/2+1)

freqs,freqs_y=np.meshgrid(freqs_x,freqs_y)

ax = fig.add_subplot(121,projection='3d')
ax.plot_wireframe(z)
ax1 = fig.add_subplot(121,projection='3d')
im=ax1.plot_wireframe(zf_shifted)

#divider=make_axes_locatable(ax[1])
#cax =divider.append_axes("right",size="5%",pad=0.05)
#fig.colorbar(im,ax=ax[1],cax=cax)

plt.tight_layout()
#plt.show()
plt.savefig("fftw-schematic-2d.png", dpi=300)
