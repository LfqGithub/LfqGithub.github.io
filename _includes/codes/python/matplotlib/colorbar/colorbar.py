import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

ax = plt.subplot(111)
ax.set_xlabel(u'你好')
im = ax.imshow(np.arange(100).reshape((10,10)))

# create an axes on the right side of ax. The width of cax will be 5%
# of ax and the padding between cax and ax will be fixed at 0.05 inch.
divider = make_axes_locatable(ax)
#cax = divider.append_axes("right", size="5%", pad=0.05)
cax = divider.append_axes("right", size=10/2.54, pad=0.05)
plt.colorbar(im, cax=cax)
plt.show()
