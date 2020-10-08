# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

period=1
fftw_size=1000 # sample points
sample_rate=1000/(2*np.pi*period) # sample frequency, Hz 

fig, ax=plt.subplots(2,1,figsize=(4,3))
t=np.arange(0,period*2*np.pi,1/sample_rate)

#x=np.sin(2*t)+2*np.sin(4*2*t) # sine-wave
x=np.zeros(fftw_size)
x[::20]=1  # squarewave

xs=x[:fftw_size]
xf=np.abs(np.fft.rfft(xs))/fftw_size
freqs=np.linspace(0, sample_rate/2, fftw_size/2+1)

ax[0].plot(t[:fftw_size],xs)
ax[0].set_xlabel(r"$t$")
ax[1].plot(freqs,xf)
ax[1].set_xlabel(r"$\nu$")

plt.tight_layout()
#plt.show()
plt.savefig("output-fftw-schematic-one-d-square-wave.png", dpi=300)
