
import sys,os
import numpy as np
import scipy.io as sciMat

VARs = ['ADens','linksDens','BDens','uMinor','uPlus','M','Tau']
var = ['sizeX','sizeY','sizeZ','dim_x','dim_y','dim_z']  # x to 2*x

#doub = lambda x:np.tile(x,[2,1]) if len(x.shape) is 2 else \
doub = lambda x:np.tile(x,[3]) if len(x.shape) is 1 else \
		np.tile(x,[1,3])
double = lambda x: 3*x

srcName = sys.argv[1]
pmat = sciMat.loadmat(srcName,squeeze_me=1)
pmat['dim_z']=float(pmat['dim_z'])
for v in VARs:
	pmat[v] = doub(pmat[v])
for v in var: 
	pmat[v] = double(pmat[v])

h,t = os.path.split(srcName)
sciMat.savemat(os.path.join(h,'tri_'+t),pmat,oned_as='column')
	
