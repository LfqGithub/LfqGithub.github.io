import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
for i, label in enumerate(('(a)','(b)','(c)','(d)')):
    ax=fig.add_subplot(2,2,i+1)
    ax.text(0.05,0.05,label,transform=ax.transAxes,bbox=dict(facecolor='red',alpha=0.5)) # transform : the default trasform specifies that text is in data coords, alternatively, you can specify text in axis coords(0,0 is lower-left and 1,1 is upper-right )
plt.show()
