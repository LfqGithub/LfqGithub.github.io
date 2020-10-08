# -*- coding:utf-8 -*-  
import numpy as np 
import matplotlib.pyplot as plt

ax1=plt.subplot2grid((3,3),(0,0),colspan=2) # 第一行的子图占据两列
ax2=plt.subplot2grid((3,3),(1,0))
ax3=plt.subplot2grid((3,3),(1,1),rowspan=2) # 第二列子图占据两行
ax4=plt.subplot2grid((3,3),(2,0))
ax5=plt.subplot2grid((3,3),(0,2),rowspan=3)

for i, ax in enumerate(plt.gcf().axes):
    ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
plt.suptitle('GridSpec example')
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig('grid-example.png',dpi=300)
#plt.show()
