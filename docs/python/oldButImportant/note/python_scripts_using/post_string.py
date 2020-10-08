
from mplconf import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sciMat
from scipy import optimize
import sys, ConfigParser, glob, os, re

files = []
L = []
energy = []

def fitfun(fit,x,y):
	x,y = np.array(x), np.array(y)
	p0 = [0,0,0]
	errfunc = lambda p,x,y:fit(p,x) - y
	ps,success = optimize.leastsq(errfunc,p0[:],args = (x,y))
	return ps

def getName(_dir):
	[chiN,miuN,Beta] = re.findall('[0-9,\.]+',_dir)
	_pre = 'chiN'+str(chiN)+'miuN'+str(miuN)+'beta'+str(Beta)
	return glob.glob(os.path.join(_dir,_pre + '*.mat'))

def plot_str(_dir,Var):
	files = getName(_dir)
	if Var in ['X','Y','Z']:
		pass
	else:
		if Var in ['x','y','z']:
			Var = chr(ord(Var) - 32)
		else:
			print "Dimension can only be one of X, Y, Z.\n "

	for i in files:
		pmat = sciMat.loadmat(i)
		try:
			energy.append(float(pmat['energy'][-1]))
		except:
			energy.append(0)
		L.append(float(pmat['size'+Var][0]))

	po2 = lambda p,x : p[0]*pow(x,2) + p[1]*pow(x,1) + p[2]
	ext = lambda x:arange(x-2,x+2,0.1)
	min_id = energy.index(min(energy))
#	try:
#		ps = fitfun(po2,L[min_id-3:min_id+3],energy[min_id-3:min_id+3])
#	except:
#		ps = [1,-1,1,]
#	L_en = lambda x:po2(ps,x)
#	min_eng = optimize.fminbound(L_en,0,L[-1])

	fg = figure()
	ax = fg.add_subplot(111)
	xlabel('$L$')
	ylabel('$F$ / $K_{\\rm B} T$')
#	text(min_eng-1,L_en(min_eng)-0.03,\
#			'L='+"{0:.2f}".format(min_eng)+\
#			',energy='+"{0:.2f}".format(L_en(min_eng)),\
#			fontsize=24)
	#ax.set_xlim(0,1)
	ax.set_ylim(min(energy)-0.05,max(energy)+0.05)
	#px_line, = ax.plot(L,energy,'-',marker='',linewidth=1,color='blue')
	px_dot, = ax.plot(L,energy,'o',mfc='white',mew=1.5,mec='black',\
			markersize=13)
	px_dot, = ax.plot(L[min_id],energy[min_id],'o',mfc='red',mew=1.5,mec='red',\
			markersize=13)
	#plt.text(L[min_id],energy[min_id]*1.2,'L='+str(L[min_id])+', Energy= '+str(round(energy[min_id],2)))
	#  the min energy and its related size 
	plt.annotate('L='+str(L[min_id])+', Energy= '+str(round(energy[min_id],2)),xy=(L[min_id],energy[min_id]),xytext=(L[min_id],energy[min_id]+abs(energy[min_id]*0.1)),arrowprops=dict(facecolor='grey',shrink=0.05))  
#	px_fit, = ax.plot(ext(L[min_id]),L_en(ext(L[min_id])),'-',marker='',\
#			linewidth=3,color='red')
#	px_min = ax.vlines(min_eng, L_en(min_eng)-0.05, L_en(min_eng)+0.05,\
#			linestyle='--')
	#ax.annotate('Critical nucleus',xy=(0.52,0.59),xytext=(0.6,0.65), \
	#		arrowprops=dict(facecolor='b',shrink=0.05), \
	#		fontsize=20,family='sans-serif')
	tight_layout()
	#show()

	for index in range(len(L)):
		print L[index], round(energy[index],4)
	print  'minium energy'
	print  'size energy'
	print L[min_id], round(energy[min_id],4)
	show()

mplconf_adjust = {
		'axes.grid' : True,
		}
mpl.rcParams.update(mplconf_adjust)

plot_str(sys.argv[1],sys.argv[-1])
