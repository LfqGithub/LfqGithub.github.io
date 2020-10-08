
import scipy.io
#import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

bench = scipy.io.loadmat("bench/DB_chiN20miuN10beta10x0.5y3.8z5.mat")
res = scipy.io.loadmat(sys.argv[1])

print 'Bench: ' + '\n'
print "ADens: ", bench['ADens'][1, :, 1], '\n'
print "BDens: ", bench['BDens'][1, :, 1], '\n'

print sum(sum(sum(bench['ADens']))) / sum(sum(sum(bench['BDens'])))

print 'Res: ' + '\n'
print "ADens: ", res['ADens'][:, 1, 1], '\n'
print "BDens: ", res['BDens'][:, 1, 1], '\n'

print sum(sum(sum(res['ADens']))) / sum(sum(sum(res['BDens'])))

plt.plot(range(res['ADens'].shape[0]), res['ADens'][:, 1, 1])
plt.plot(range(res['BDens'].shape[0]), res['BDens'][:, 1, 1])
plt.plot(range(res['ADens'].shape[0]),
         res['ADens'][:, 1, 1] + res['BDens'][:, 1, 1])
plt.ylim([0, 1])
plt.show()
plt.barbs
