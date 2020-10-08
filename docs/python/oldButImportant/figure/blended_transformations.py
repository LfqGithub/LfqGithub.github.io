import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
import numpy as np

fig =plt.figure()
ax=fig.add_subplot(111)
x=np.random.randn(1000)
ax.hist(x,10) # (x,bins), bins: divide the data to be bins parts
ax.set_title(r'$\sigma=1 \/\dots \/ \sigma=2$')
trans=transforms.blended_transform_factory(ax.transData,ax.transAxes)
rect=patches.Rectangle((1,0),width=1,height=1,transform=trans,color='yellow',alpha=0.5)
ax.add_patch(rect)
plt.show()
