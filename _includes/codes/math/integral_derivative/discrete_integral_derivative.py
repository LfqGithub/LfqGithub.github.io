import numpy as np
import random
import matplotlib.pyplot as plt


def discrete_derivative(x,y,deltax):
    return 1

def discrete_integral(x,y):
    return 1



x=np.arange(0,2*np.pi,0.001)
y=[np.sin(i)+random.uniform(0,0.01) for i in x] # Wrong expression: y=np.sin(x)+random.uniform(0,0.01)


fig,ax=plt.subplots()
ax.plot(x,y)

plt.show()

