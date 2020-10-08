
import ConfigParser, sys, os, socket, subprocess

def getPids(dir_path):
	pid_file = os.path.join(dir_path,'pid_log')
	conf = ConfigParser.ConfigParser()
	print pid_file
	conf.read(pid_file)
	pids = conf.items(socket.gethostname())
	pids = [i[1] for i in pids]
	return pids

def killall(dir_path,sec):
	pids = getPids(dir_path)
	for p in pids:
		subprocess.call(['kill',p])

dir_path = sys.argv[1]
host = socket.gethostname()
killall(dir_path,host)
