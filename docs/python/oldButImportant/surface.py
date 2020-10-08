#!/usr/bin/evn python

import numpy as np
import scipy.linalg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import mpltex
from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource

def surface1():
# some 3-dim points
    beta=np.array([7,7,7,7,7,7.25,7.25,7.25,7.25,7.25,7.5,7.5,7.5,7.5,7.5,7.75,7.75,7.75,7.75,7.75,8,8,8,8,8])
    D=np.array([0.4,0.45,0.5,0.55,0.6,0.4,0.45,0.5,0.55,0.6,0.4,0.45,0.5,0.55,0.6,0.4,0.45,0.5,0.55,0.6,0.4,0.45,0.5,0.55,0.6])
    z=np.array([0.5856,0.5813,0.5696,0.5666,0.5545,0.6067,0.5941,0.5818,0.5687,0.5561,0.6111,0.6078,0.5948,0.5805,0.5677,0.6239,0.6115,0.5980,0.5945,0.5713,0.6290,0.6244,0.6104,0.5960,0.5818])
    data=np.c_[beta,D,z]
    
    mn=np.min(data,axis=0)
    mx=np.max(data,axis=0)
    print('mn',mn)
    print('mx',mx)
    X,Y=np.meshgrid(np.linspace(mn[0]*0.99,mx[0]*1.01,20),np.linspace(mn[1]*0.95,mx[1]*1.05,20))
    XX = X.flatten()
    YY = Y.flatten()
    
    order = 2    # 1: linear, 2: quadratic
    if order == 1:
        # best-fit linear plane
        A = np.c_[data[:,0], data[:,1], np.ones(data.shape[0])]
        C,_,_,_ = scipy.linalg.lstsq(A, data[:,2])    # coefficients
        
        # evaluate it on grid
        Z = C[0]*X + C[1]*Y + C[2]
        
        # or expressed using matrix/vector product
        #Z = np.dot(np.c_[XX, YY, np.ones(XX.shape)], C).reshape(X.shape)
    
    elif order == 2:
        # best-fit quadratic curve
        A = np.c_[np.ones(data.shape[0]), data[:,:2], np.prod(data[:,:2], axis=1), data[:,:2]**2]
        C,_,_,_ = scipy.linalg.lstsq(A, data[:,2])
        
        # evaluate it on a grid
        Z = np.dot(np.c_[np.ones(XX.shape), XX, YY, XX*YY, XX**2, YY**2], C).reshape(X.shape)
    
    # plot points and fitted surface
    fig = plt.figure(figsize=(3.25,3.25))
    ax = fig.gca(projection='3d')

    ls = LightSource(270, 45)
#    rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')

#ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.5,color='k',facecolors=rgb,linewidth=0, antialiased=False, shade=False)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.5)
    ax.scatter(data[:,0], data[:,1], data[:,2], facecolor='k',edgecolor='none', s=50)
    plt.xlabel(r'$\beta(R_g)$')
    plt.ylabel('$D$')
    ax.set_zlabel(r'$P_L$')
    ax.set_zticks([0.55,0.6])
    ax.set_yticks([0.4,0.5,0.6])
    ax.set_xticks([7,7.5,8])
    ax.set_zlim(0.52,0.635)
    ax.set_xlim(6,9)
    ax.set_ylim(0.35,0.65)
    ax.axis('equal')
    ax.axis('tight')
    ax.view_init(30,110)
# plt.savefig('betaDSurface.png',dpi=300)
    plt.show()

surface1()
