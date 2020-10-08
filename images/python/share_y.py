import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

fig.set_facecolor('gray')
fig.patch.set_facecolor('gray')
fig.set_alpha(0.6)
fig.patch.set_alpha(0.6)
ax.set_alpha(0)
ax.patch.set_alpha(0)

n = [3, 4, 6, 8, 12]
area = [np.sqrt(3) / 2, 1, 1.5 * np.sqrt(3), 2 +
        2 * np.sqrt(2), 3 * (2 + np.sqrt(3))]
beta = [0, 0, 0, 0, 0]

for i, el in enumerate(area):
    beta[i] = np.sqrt(1 / el)

ax.plot(n, area, 'ks-')
ax.set_xlabel('N')
ax.set_ylabel('S', color='k')
ax.tick_params('y', colors='k')

ax1 = ax.twinx()
ax1.plot(n, beta, 'rs--')
ax1.set_ylabel('L', color='r')
ax1.tick_params('y', colors='r')

plt.tight_layout()
plt.savefig('shareY.png', dpi=600)
