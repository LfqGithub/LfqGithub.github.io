import matplotlib.pyplot as plt
import numpy as np

markers = [
    ".",
    ",",
    "o",
    "v",
    "^",
    "<",
    ">",
    "1",
    "2",
    "3",
    "4",
    "8",
    "s",
    "p",
    "P",
    "*",
    "h",
    "H",
    "+",
    "x",
    "X",
    "D",
    "d",
    "|",
    "_"]
len_markers = len(markers)
markers_num = np.arange(len_markers)
fig, ax = plt.subplots(figsize=(len_markers, 4))

# darkmode figure
fig.set_facecolor('gray')
fig.patch.set_facecolor('gray')
fig.set_alpha(0.6)
fig.patch.set_alpha(0.6)
ax.set_alpha(0)
ax.patch.set_alpha(0)

for i in np.arange(len_markers):
    ax.plot(i, 1, markers[i], markersize=20)
    ax.text(i, 0.5, str(markers_num[i]), ha='center')
    ax.plot(i, 2, markers[i], markerfacecolor='None', markersize=20)
    # ax.plot(i,2,markers[i],markeredgewidth=1,markerfacecolor='None',markersize=20)
    ax.text(i, 1.5, str(markers_num[i]), ha='center')
ax.set_ylim([0, 3])
ax.set_axis_off()
plt.tight_layout()
plt.savefig('matplotlib_markers.png', dpi=600)
