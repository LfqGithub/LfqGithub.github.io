import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

t=np.array([0,3,5,6,8,10,12,14,16,18,19,21,25,26,28,30])
#x=np.linspace(-30,61,100)
print(t)
y=np.array([1,3.376564804,3.824655237,4.937971609,6.836609905,9.482581167,15.54173292,25.90180404,33.69751944,44.97531007,55.11917083,64.65564197,73.12689005,77.4996097,78.4681257,79.86137211])
y1=np.array([0.69178 ,2.33584 ,2.64582 ,3.41599 ,4.72943 ,6.55986 ,10.75146 ,17.91835 ,23.31127 ,31.11302 ,38.13034 ,44.72748 ,50.58772 ,53.61268 ,54.28268 ,55.2465]) 
print(y)

def func(t,nc,lam): # the function you want to fit, unkown parameters: nc, lambda
    incos=lam*t*np.sqrt(nc/2.0)
    deno=(np.cos(incos))**(2.0/nc)
    y=(nc-1.0)/deno+1
    return y
popt, pcov = curve_fit(func,t,y)
nc,lam=popt[0],popt[1]
print(popt)
y_fit=func(t,nc,lam)
fig,ax=plt.subplots()
ax.plot(t,y,'*',label='original data')
ax.plot(t,y_fit,'-',label='fit values')
plt.legend()
plt.show()


