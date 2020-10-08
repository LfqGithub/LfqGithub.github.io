import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('test')
matplotlib.rc('font',family='sans-serif') 
matplotlib.rc('font',serif='Times') 
matplotlib.rc('font',sans-serif='Helvetica')

a=np.linspace(0,6,100)
b=np.sin(a)
plt.plot(a,b)
plt.show()
