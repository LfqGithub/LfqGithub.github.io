
import numpy as np
import scipy.io as sciMat
import matplotlib.pyplot as plt
from   matplotlib import colors
import gyroid as gy
from scipy import interpolate
import sys

class HEXGenerate3d:
	"""
	Shape generator for 3D-SCFT initial condition.
	"""
	def __init__ (self,Nx,Ny,Nz,matname='HEX3d.mat',varname='HEX3d',Na=32,Nb=32):
		Nx += 0
		Ny += 0
		#print Nx,Ny
		uc = gy.UnitCell(2,gy.HEXAGONAL,np.array([1.0]))
		group = gy.Group(2,gy.BRAVAIS,uc.shape,"P6mm")
		grid = gy.Grid(np.array([Na,Nb]),group)
		basis = gy.Basis(group,grid)
		c = np.zeros(101)
		c[0],c[1],c[2],c[3],c[4] = 1,0.5,0.2,0.1,0.05
		struct = basis.generate_structure_by_fft((Na,Nb),c,grid)
		struct1 = np.tile(struct,[2,2])
		Na1,Nb1 = struct1.shape
		rx1 = np.zeros((Na1,Nb1))
		ry1 = np.zeros((Na1,Nb1))
		for (i,j) in np.ndindex(Na1,Nb1):
			x = (1.0*np.array([i,j])) / (Na1,Nb1)
			rx1[i,j],ry1[i,j] = np.dot(x,basis.shape.h)
		cx = np.zeros(Nx)
		cy = np.zeros(Ny)
		cx = np.linspace(0,0.5,Nx)
		cy = np.linspace(0,0.5*1.732,Ny)
		cxx,cyy = np.meshgrid(cx,cy)

		rx2,ry2,struct2 = rx1,ry1,struct1
		points = np.zeros((Na1*Nb1,2))
		values = np.zeros(Na1*Nb1)
		rx2.resize(Na1*Nb1)
		ry2.resize(Na1*Nb1)
		struct2.resize(Na1*Nb1)
		points[:,0],points[:,1],values = rx2,ry2,struct2
		struct2 = interpolate.griddata(points,values,(cxx,cyy),method='nearest')
		nor = (struct2.max() - struct2.min())*1.2
		for (i,j) in np.ndindex(Ny,Nx):
			struct2[i,j] = (struct2[i,j] - struct2.min()) / nor
		struct2 = struct2.transpose()
		struct3 = np.zeros([Nx,Ny,1])
		struct3[:,:,0] = struct2
		struct3 = np.tile(struct3,[1,1,Nz]);
		sciMat.savemat(matname,{varname:struct3},oned_as='column')

	def draw(self):
		dx = rx1.max() - rx1.min()
		dy = ry1.max() - ry1.min()

		w,h = plt.figaspect(float(dy/dx))
		fig = plt.figure(figsize=(w,h),frameon=False,dpi=80,facecolor='w')
		ax = fig.add_axes([0,0,1,1],frameon=False,axisbg='w')
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)

		step = (struct1.max() - struct1.min()) / 256
		levels = np.arange(struct1.min(),struct1.max()+step,step)

		clr = np.zeros((256,3))
		for i in np.arange(256):
			clr[i,0] = i / 255.0
		cmap = colors.ListedColormap(clr)
		#ax.contourf(rx1,ry1,struct1,levels=levels,cmap=cmap,antialiased=False)
		#plt.show()

		fig1 = plt.figure(figsize=(w,h),frameon=False,dpi=80,facecolor='w')
		ax = fig1.add_axes([0,0,1,1],frameon=False,axisbg='w')
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)
		plt.imshow(struct2)
		plt.show()

#print sys.argv[1], sys.argv[2], sys.argv[3]
shape1 = HEXGenerate3d(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))

#shape1.draw()
