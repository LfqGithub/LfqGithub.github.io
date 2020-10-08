
import json,sys
import numpy as np

fname = 'size.json'
hexname = ['HEX','Hex','hex']
hex2name = ['HEX2','Hex2','hex2']
lamname = ['LAM','Lam','lam']
cubename=['cube']
cuboidname=['cuboid']
squarename=['square']
squarexname=['squarex']
def HEX(l1,_l1,step=0.2):
# x = 0.5 y = l1 z = l1*sqrt(3)
	sz = lambda x:{'sizeX':'0.5',\
			'sizeY':'{0:.2f}'.format(x),\
			'sizeZ':'{0:.2f}'.format(x*np.sqrt(3))}
	bound = [l1,_l1] 
	bound.sort()
	print json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])
	return json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])

def CUBOID(l1,_l1,step=0.2):
# x = 0.5 y = l1 z = l1*sqrt(3)
	sz = lambda x:{'sizeX':'3',\
			'sizeY':'3',\
			'sizeZ':'{0:.2f}'.format(x*np.sqrt(3))}
	bound = [l1,_l1] 
	bound.sort()
	print json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])
	return json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])

def cube(l1,_l1,step=0.2):
# x = 0.5 y = l1 z = l1*sqrt(3)
	sz = lambda x:{'sizeX':'{0:.2f}'.format(x),\
			'sizeY':'{0:.2f}'.format(x),\
			'sizeZ':'{0:.2f}'.format(x)}
	bound = [l1,_l1] 
	bound.sort()
	print json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])
	return json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])

def square(l1,_l1,step=0.2):
# x = 0.5 y = l1 z = l1*sqrt(3)
	sz = lambda x:{'sizeX':'0.2',\
			'sizeY':'{0:.2f}'.format(x),\
			'sizeZ':'{0:.2f}'.format(x)}
	bound = [l1,_l1] 
	bound.sort()
	print json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])
	return json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])

def squarex(l1,_l1,step=0.2):
# x = 0.5 y = l1 z = l1*sqrt(3)
	sz = lambda x:{'sizeX':'0.2',\
			'sizeY':'{0:.2f}'.format(x*float(sys.argv[5])),\
			'sizeZ':'{0:.2f}'.format(x*float(sys.argv[6]))}
	bound = [l1,_l1] 
	bound.sort()
	print json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])
	return json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])


def HEX2(l1,_l1,step=0.2):
# x = 0.5 y = l1 z = l1*sqrt(3)
	sz = lambda x:{'sizeX':'0.5',\
			'sizeY':'{0:.2f}'.format(x*2),\
			'sizeZ':'{0:.2f}'.format(x*np.sqrt(3))}
	bound = [l1,_l1] 
	bound.sort()
	print json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])
	return json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])

def LAM(l1,_l1,step=0.2):
# x = 0.5 y = 0.5 z = l1
	sz = lambda x:{'sizeX':'0.5',\
			'sizeY':'0.5',\
			'sizeZ':'{0:.2f}'.format(x)}
	bound = [l1,_l1] 
	bound.sort()
	print json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])
	return json.dumps([sz(k) for k in np.arange(bound[0],bound[1],step)])

	
	
if sys.argv[1] in hexname:
	l1,_l1 = float(sys.argv[2]), float(sys.argv[3])
	try:
		step1 = float(sys.argv[4])
	except:
		pass
	with open(fname,'wb') as f:
		if len(sys.argv) == 4:
			f.write(HEX(l1,_l1))
		if len(sys.argv) == 5:
			f.write(HEX(l1,_l1,step1))

if sys.argv[1] in hex2name:
	l1,_l1 = float(sys.argv[2]), float(sys.argv[3])
	try:
		step1 = float(sys.argv[4])
	except:
		pass
	with open(fname,'wb') as f:
		if len(sys.argv) == 4:
			f.write(HEX2(l1,_l1))
		if len(sys.argv) == 5:
			f.write(HEX2(l1,_l1,step1))

if sys.argv[1] in lamname:
	l1,_l1 = float(sys.argv[2]), float(sys.argv[3])
	try:
		step1 = float(sys.argv[4])
	except:
		pass
	with open(fname,'wb') as f:
		if len(sys.argv) == 4:
			f.write(LAM(l1,_l1))
		if len(sys.argv) == 5:
			f.write(LAM(l1,_l1,step1))
if sys.argv[1] in cubename:
	l1,_l1 = float(sys.argv[2]), float(sys.argv[3])
	try:
		step1 = float(sys.argv[4])
	except:
		pass
	with open(fname,'wb') as f:
		if len(sys.argv) == 4:
			f.write(cube(l1,_l1))
		if len(sys.argv) == 5:
			f.write(cube(l1,_l1,step1))
if sys.argv[1] in squarename:
	l1,_l1 = float(sys.argv[2]), float(sys.argv[3])
	try:
		step1 = float(sys.argv[4])
	except:
		pass
	with open(fname,'wb') as f:
		if len(sys.argv) == 4:
			f.write(square(l1,_l1))
		if len(sys.argv) == 5:
			f.write(square(l1,_l1,step1))
if sys.argv[1] in squarexname:
	l1,_l1 = float(sys.argv[2]), float(sys.argv[3])
	try:
		step1 = float(sys.argv[4])
	except:
		pass
	with open(fname,'wb') as f:
		if len(sys.argv) == 6:
			f.write(squarex(l1,_l1))
		if len(sys.argv) == 7:
			f.write(squarex(l1,_l1,step1))

if sys.argv[1] in cuboidname:
	l1,_l1 = float(sys.argv[2]), float(sys.argv[3])
	try:
		step1 = float(sys.argv[4])
	except:
		pass
	with open(fname,'wb') as f:
		if len(sys.argv) == 4:
			f.write(CUBOID(l1,_l1))
		if len(sys.argv) == 5:
			f.write(CUBOID(l1,_l1,step1))
