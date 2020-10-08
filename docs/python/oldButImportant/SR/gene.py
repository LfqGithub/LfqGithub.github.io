# get the disctetize queue of parameter of size, beta, and so on
# liufaqiang
# history
#   Fri Apr 14 15:09:08 DST 2017
#       code reconsitution 
#   Fri Apr 14 16:18:18 DST 2017
#       add beta

import json,sys
import numpy as np

fname = 'size.json'

# [x1,x0,y1,y0,z1,z0], sizem=m1*x+m0, m=x,y,z
size={} 
size['hex']  = [0,0.5,1,0,round(np.sqrt(3),2),0] 
size['lam']  = [0,0.5,0,0.5,1,0]
size['cube'] = [1,0,1,0,1,0]

print(size)

def setSize(start,end,step):
        coe=size[sys.argv[1]]
        sz = lambda x:{'sizeX':'{:.2f}'.format(x*coe[0]+coe[1]),\
                'sizeY':'{0:.2f}'.format(x*coe[2]+coe[3]),\
                'sizeZ':'{0:.2f}'.format(x*coe[4]+coe[5])}
        bound =[start,end]
        bound.sort()
        print(json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)]))
        return json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])
def setSizeBeta(startSize,endSize,stepSize,startBeta,endBeta,stepBeta):
        coe=size[sys.argv[1]]
        sz = lambda x,y:{'sizeX':'{:.2f}'.format(x*coe[0]+coe[1]),\
                'sizeY':'{0:.2f}'.format(x*coe[2]+coe[3]),\
                'sizeZ':'{0:.2f}'.format(x*coe[4]+coe[5]),\
                'Beta':'{0:.2f}'.format(y)}
        boundSize =[startSize,endSize]
        boundSize.sort()
        boundBeta=[startBeta,endBeta]
        boundBeta.sort()
        print(json.dumps([sz(k,m) for k in np.arange(boundSize[0],boundSize[1],stepSize) for m in np.arange(boundBeta[0],boundBeta[1],stepBeta)]))
        return json.dumps([sz(k,m) for k in np.arange(boundSize[0],boundSize[1],stepSize) for m in np.arange(boundBeta[0],boundBeta[1],stepBeta)])


startSize,endSize,stepSize = float(sys.argv[2]), float(sys.argv[3]),float(sys.argv[4])
startBeta,endBeta,stepBeta = float(sys.argv[6]), float(sys.argv[7]),float(sys.argv[8])
print('start,end,step of Beta',startBeta,endBeta,stepBeta)

with open(fname,'w') as f:
	if len(sys.argv) == 5:
		f.write(setSize(startSize,endSize,stepSize))
	if len(sys.argv) == 9:
		f.write(setSizeBeta(startSize,endSize,stepSize,startBeta,endBeta,stepBeta))




