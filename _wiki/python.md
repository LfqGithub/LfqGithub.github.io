---
layout: wiki
title: Python
categories: Python
description: python 学习
keywords: python, basic
---

Python 基础知识学习、记录、理解, updating...

# 使用习惯
使用 Python 时，竟然遇到 package 安装不上、平台不兼容(如 WSL 平台的 Python 竟然出现安装不上 Python package 问题), 以及需要同时使用多个Python版本的情形，为了减少这些烦恼，
安装Python, Python package等操作，使用 Miniaconda, 以解决上述可能遇到的问题。

>> 1. Aconda 中的python版本一般领先于Ubuntu等系统中自带的版本.

# Python Interpreters

- [IPython](https://ipython.org/)
  - python交互式shell， 比python默认shell好用很多，支持变量自动补全、自动缩进、支持bash shell命令，内置了很多有用的功能和函数
- [Jupyter Notebook](https://jupyter.org/)
  - 原称IPython notebook, 交互式笔记本，支持40中编程语言，一般用来编写漂亮的交互式文档。

# Install and Config Python Environment

## Python2

```bash
$ sudo apt install python+packageName
$ sudo pip install packageName
```
## Python3

```bash
$ sudo pip3 install packageName
# sudo apt remove --purge python+packageName
$ sudo apt install python-packageName # 有时安装的 package 版本较老，推荐 pip3 安装
```

## Install Python Packages

### pip

```python
# uninstall all pip-installed packages
import pip
from subprocess import call
for dist in pip.get_installed_distributions():
    call("pip uninstall " + dist.project_name, shell=True)

# update all pip-installed packages
import pip
from subprocess import call
for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
```

- `pip show package-name`: Show information about installed packages.


#### Modify pip Source
```bash
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
```

- Update
	```bash
	# update your system
	$ sudo apt update && sudo apt upgrade
	# install pip
	$ sudo apt install python-pip
	# update pip
	$ pip install --upgrade pip
	```
- Pip Syntax
	```bash
    # python3
	$ pip search package
	$ pip install package
	$ pip uninstall package 
	$ pip --help
    python3
	pip3 replace pip
	```
- Install Packages of Python2/3 via Pip
	```bash
	# python2 
	$ sudo python2 -m pip install packageName
    # or 
	$ sudo pip install packageName
	# python3
	$ sudo python3 -m pip install packageName
	# or 
	$ sudo pip3 install packageName
	```
- pip install mayavi
  ```bash
  $ sudo apt install python-vtk python-qt4
  $ sudo python -m pip install mayavi
  ```

### Switch Python Versions

在使用python中，不可避免需要在python2和python3之间切换。需要我们在编程和配置环境时考虑到这一因素
- package的安装。利用[pip分别给python2和python3分别安装package](pip.md)方法安装package
- 在代码首行添加`#!python2`和`#!python3`来设置该脚本通过`python2/3`来运行
- 更加复杂的情况，如不同python程序需要不同版本的package，则使用虚拟环境来单独操作

### Avoid Python Cache

从`python 2.6`开始，为了加快程序运行速度，python在编译时会产生缓存文件，这样可以在多次运行该脚本时加快速度。[what is new in python 2.6](https://docs.python.org/dev/whatsnew/2.6.html#interpreter-changes)
但是，在不需要加速的使用场景，这些文件很让人讨厌。避免产生这些缓存文件的方法：
- 运行时使用命令`python -B'选项
- 在脚本中加入`import sys;sys.dont_write_bytecode=True`
- 设置当前用户变量，使上一句命令对当前用户所有脚本均生效。在文件`~/.local/lib/python xxx/site-packages/usercustomize.py`中加入
  ```python
  import sys;sys.dont_write_bytecode=True
  ```
- 如果需要引用其他文件中的函数，则需要在被引用文件中加入
  ```python
  import sys;sys.dont_write_bytecode=True
  ```

## Python Distributions
### Anaconda
#### 下载
[Anaconda 下载--清华大学镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

#### Modify Source Mirror
```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```

#### BugFix

1. 安装后`import mayavi`时，提示没有libGLU.so.1
```bash
sudo yum install libGlU*
```

### Conda

#### Basic Command

```bash
# search package
$ conda search packageName
# install package
$ conda install packageName
$ conda install -name myenv packageName
$ conda install packageName=package_version  # like scipy=0.15.0
$ conda install packageName1=package_1_version  packageName2=package_2_version
$ pip install packageName # conda list to see if the package are installed sucessfully
# list package
$ conda list
$ conda list -n myenv
# update package
$ conda update packageName
$ conda update python
$ conda update conda
$ conda update anaconda
# remove package
$ conda remove packageName1 packageName2
```




# Python Code Style

发布前，可以使用[autopep8](https://github.com/hhatto/autopep8)格式化自己代码(PEP: Python Enhancement Proposal)

```bash
$ python -m pip install autopep8 # install autopep8
$ autopep8 --in-place --aggressive --aggressive <filename.py>
$ autopep8 --in-place --recursive foo.py
```


# Attention

## 修改列表中元素
- 禁止使用下列方法修改元素(无效)
  -  ```python
	 >>> a=[1,2,3,4]
	 >>> for i in a:
	 >>>	    i=i*2
	 >>>print(a)
	  [1,2,3,4]
	 ```
  - 原因：`i`的id已经不是原来的id
- 避免使用下列方法修改元素
  - ```python
    >>> a=[1,2,3,4,5]
    >>> for i,el in enumerate(a):
    >>>	    if el==3:
	>>>		del a[i]
    >>>print(a)
    [1,2,4,5]
    ```
  - 原因：for 遍历过程中，如果删除了其中的一个元素，会导致后面元素前移，出现漏网之鱼
  - 涉及到列表的插入与删除，不要用`for`
- 正确做法
  -  ```python
	 >>> a=[1,2,3,4,5]
	 >>> for i in range(len(a)):
	 >>>     a[i]*=2
	 >>> print(a)
	  [2,4,6,8,10]
	 ```

# Syntax

## 变量

### 类变量

- 定义在类中且在函数体之外
- 一般不用作实例变量
- 在全部实例化对象中公用。
- 访问方式：`className.classVar`，如果使用`self.classVar`, 类变量会被实例变量的值覆盖，所以不建议使用这种方式访问类变量

### 实例变量
- 用self绑定到实例上
- 只作用于当前实例
- 类内部访问：`self.instanceVar`
- 类外部访问方式：`className.instanceVar`

## Python 类

##  Python 帮助系统

###	 Help()
- python环境中键入`help()`进入帮助系统， 键入`modules`查看当前安装所有模块
- `import math`模块后， `help(math)`查看`math`模块的帮助文档
- `dir(math)`查看`math`模块中所有函数

### 内建模块

```bash
$ import sys 
$ sys.builtin_modules_names
```

### Function

```bash
$ help(math.sin)
# or 
$ print(func_name.__doc__)
```

# Python中的坑
## 参数
- Python默认参数
  - ```python
    def foo(i,a=[]):
		for i in range(i):
			a.append(i)
		print(a)
#  the function foo works the same way as 
#   default_a=[]
#   def foo(i, a=default_a):
#		for i in range(i):
#			a.append(i)
#		print(a)
	foo(3)
	foo(3,[1,2])
	foo(3)
#  There are various workarounds, including
#   def foo(i, a=None):
#   if not s: s=[]
#		for i in range(i):
#			a.append(i)
#		print(a)
	```
  - 输出
    ```bash
	[0, 1, 2]
	[1, 2, 0, 1, 2]
	[0, 1, 2, 0, 1, 2]
	```
  - 现象：默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。 
  - 原因
	- Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。所以，定义默认参数要牢记一点：默认参数必须指向不变对象！--引自[廖雪峰的python教程](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738449338c8a122a7f2e047899fc162f4a7205ea3000)
  - 修改方法见程序注释，参考了[stackoverflow](https://stackoverflow.com/questions/13195989/default-values-for-function-parameters-in-python)


## bugFix
- [x] Latex - missing ".sty" package
  - `sudo apt install texlive-science texlive-extra texlive-fonts-recommond dvipng`
- [x] UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure
  - `sudo apt install python3-tk`

## Links
### Python教程
- [python3-cookbook](http://python3-cookbook-personal.readthedocs.io/zh_CN/latest/index.html)
- [Python 标准库](https://docs.python.org/zh-cn/3/library/index.html)
- [Python 类变量与实例变量](http://kuanghy.github.io/2015/12/19/python-variable)
- [Think Python2-中文版](https://cycleuser.gitbooks.io/think-python/content/)
- [SciPy Lecture Notes 中文版](https://wizardforcel.gitbooks.io/scipy-lecture-notes/content/index.html)
- [Pandas Notebook](https://amaozhao.gitbooks.io/pandas-notebook/content/%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C.html)
- [Jupyter Notebook快速入门](http://codingpy.com/article/getting-started-with-jupyter-notebook-part-1/)
- [Ipython介绍](https://blog.csdn.net/gavin_john/article/details/53086766)
- [Python代码格式规范--PEP8](https://www.python.org/dev/peps/pep-0008/)
- [Python Package--autopep8](https://github.com/hhatto/autopep8)
 


