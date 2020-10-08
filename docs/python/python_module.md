# Python Module 基本知识
## Module 基本知识

1. 查看模块属性和方法
```bash
>>> dir(mayavi)
['ETSConfig', '__builtins__', '__doc__', '__extras_require__', '__file__', '__name__', '__package__', '__path__', '__requires__', '__version__', '_jupyter_nbextension_paths', 'sys']
```
2. Python默认搜索模块的位置
```bash
# 添加模块到sys.path
sys.path.append("xxx.py")
# 查看当前sys.path目录
>>> import sys
>>> import pprint
>>> pprint.pprint(sys.path)
['',
 '/share/home/liufaqiang/apps/anaconda2/lib/python27.zip',
 '/share/home/liufaqiang/apps/anaconda2/lib/python2.7',
 '/share/home/liufaqiang/apps/anaconda2/lib/python2.7/plat-linux2',
 '/share/home/liufaqiang/apps/anaconda2/lib/python2.7/lib-tk',
 '/share/home/liufaqiang/apps/anaconda2/lib/python2.7/lib-old',
 '/share/home/liufaqiang/apps/anaconda2/lib/python2.7/lib-dynload',
 '/share/home/liufaqiang/apps/anaconda2/lib/python2.7/site-packages']
```
3. 添加python环境变量PYTHONPATH
```bash
export PATH = dir_of_your_module:$PATH
```

4. 模块中的基本元素
```bash
# /usr/bin/env python
# coding:utf-8
__all__=['a','b'] # 告诉解释器，这两个东西是有权限被访问的，而且只有这两个东西。
```
## 参考内容
1. [跟老齐学Python之编写模块](http://www.infoq.com/cn/articles/Python-writing-module)
