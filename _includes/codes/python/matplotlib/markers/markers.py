import matplotlib.pyplot as plt
import numpy as np

markers=[ ".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D", "d", "|", "_"]
#marknum=[ 1  , 2  , 3 ,  4,   5 ,  6 ,  7 ,  8 ,  9 ,  10,  11,  12, 13 ,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25]
len_markers=len(markers)
print(len_markers)
markers_num=np.arange(len_markers)
print(markers_num)
fig, ax=plt.subplots(figsize=(len_markers,4))
for i in np.arange(len_markers):
    ax.plot(i,1,markers[i],markersize=20)
    ax.text(i,0.5,str(markers_num[i]),ha='center')
    ax.plot(i,2,markers[i],markerfacecolor='None',markersize=20)
    #ax.plot(i,2,markers[i],markeredgewidth=1,markerfacecolor='None',markersize=20)
    ax.text(i,1.5,str(markers_num[i]),ha='center')
ax.set_ylim([0,3])
ax.set_axis_off()
plt.tight_layout()
#plt.show()
plt.savefig('python_markers.png',dpi=300)
