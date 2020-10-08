
import ConfigParser,json,errno
import os,shutil,subprocess,socket,sys,glob

ALL = ['N','NA','chiN','miuN','delta_tW','delta_tS','delta_tY',\
		'delta_tP','sizeX','sizeY','sizeZ','dim_x','dim_y','dim_z',\
		'max_it','Rg2','Beta','meshfile','srcFile','shapeFile','shapeName',\
		'fieldMethod','interpScript','recordname','isAutoSubmit',\
		'listName','topology']
KEYS = ['chiN','miuN','Beta','listName','topology','srcFile']
FILELIST = ['scfRigid','DeMesh.mat','GYROID.mat','HEX3d.mat','LAM3D.mat',
		'ResizeField.m']
sz = ['sizeX','sizeY','sizeZ']

def generatePara(filename):
	_config = ConfigParser.ConfigParser()
	_config.optionxform=str
	_config.read(filename)
	_filenames = []
	sec = 'modelABrc'
	Vals, sizes, = {}, []
	for k in KEYS:
		Vals[k] = _config.get(sec,k)
	_path =	'c'+Vals['chiN']+'m'+Vals['miuN']+'b'+Vals['Beta']+'topo'+Vals['topology']
	if not os.path.exists(_path):
		os.makedirs(_path)
	with open(Vals['listName'],'r') as f:
		for l in f.readlines():
			sizes = json.loads(l)
	count = len(glob.glob(os.path.join(_path,'Para*.ini')))
	for k in sizes:
		for name in sz:
			_config.set(sec,name,k[name])
		_fn = 'Para_' + str(count) + '.ini'
		count += 1
		with open(_path + '//' + _fn,'wb') as f:
			_config.write(f)
		_filenames.append(_fn)
	a=Vals['srcFile']
	FILELIST.append(a)
	for ff in FILELIST:
		if not os.path.isfile(os.path.join(_path,ff)):
			try:
				os.symlink(os.path.join(os.path.realpath('.'),ff), os.path.join(_path,ff))
			except OSError, e:
				if e.errno == errno.EEXIST:
					os.remove( os.path.join(_path,ff))
					os.symlink(os.path.join(os.path.realpath('.'),ff), os.path.join(_path,ff))
	return _path, _filenames

def runRoutines(path,names):
	os.chdir(path)
	fh = open('/dev/null','w')
	pids = []
	sec = socket.gethostname()
	_config = ConfigParser.ConfigParser()
	_config.optionxfrom=str
	_config.add_section(sec)
	CMD = 'nuhup '

	for k in names:
		pid = subprocess.Popen(['./scfRigid',k],\
				shell=False,stderr=fh,stdin=fh,stdout=fh,close_fds=True).pid
		pids.append(pid)
		_config.set(sec,k,pid)
	with open('pid_log','a+') as fp:
		_config.write(fp)

path,names = generatePara(sys.argv[1])
runRoutines(path,names)


