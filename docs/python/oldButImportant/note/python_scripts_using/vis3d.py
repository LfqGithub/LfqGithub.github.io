
import numpy as np
import scipy.io as sciMat
import mayavi.mlab as mlab
import sys


__all__ = [
		'_times','_filename','c_r','c_g','cont',
		]

class vis3d:
	def __init__(self):
		self.c_r = (0.687,0.163,0)
		self.c_g = (0.163,0.687,0)
		self.cont = [0.65,]

	def surface3d(self,filename,times=2):
		_times = times
		dot_index = filename.find('.mat')
		_filename = filename[0:dot_index]
		pmat = sciMat.loadmat(_filename+'.mat')
		da = np.tile(pmat['ADens'],[_times,_times,_times])
		db = np.tile(pmat['BDens'],[_times,_times,_times])
		d = da.shape
		dim = (d[0]+2,d[1]+2,d[2]+2)
		dA = np.zeros((dim[0],dim[1],dim[2]))
		dB = np.zeros((dim[0],dim[1],dim[2]))

		dA[1:-1,1:-1,1:-1] = np.tile(pmat['ADens'],[_times,_times,_times])
		dB[1:-1,1:-1,1:-1] = np.tile(pmat['BDens'],[_times,_times,_times])

		sX, sY, sZ = float(pmat['sizeZ']), \
				float(pmat['sizeY']), \
				float(pmat['sizeX'])

		X = np.zeros((dim[0],dim[1],dim[2]))
		Y = np.zeros((dim[0],dim[1],dim[2]))
		Z = np.zeros((dim[0],dim[1],dim[2]))

		x,y,z = np.arange(0,dim[0]),np.arange(0,dim[1]),np.arange(0,dim[2])
		x = sX * _times / dim[0] * x
		y = sY * _times / dim[1] * y
		z = sZ * _times / dim[2] * z

		for (i,j) in np.ndindex(dim[1],dim[2]):
			X[:,i,j] = x
		for (i,j) in np.ndindex(dim[0],dim[2]):
			Y[i,:,j] = y
		for (i,j) in np.ndindex(dim[0],dim[1]):
			Z[i,j,:] = z

# 		mlab.engine.current_scene.scene.off_screen_rendering = True
#		mlab.options.offscreen = True
		mlab.clf()
		mlab.contour3d(X,Y,Z,dB,color=self.c_r,contours=self.cont)	
		mlab.contour3d(X,Y,Z,dA,color=self.c_g,contours=self.cont)	
		mlab.savefig(_filename+'.png')

v = vis3d()
v.surface3d(sys.argv[1])
