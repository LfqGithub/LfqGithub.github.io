---
layout: wiki
title: Prgparse
---

#  Syntax

```python
import argparse
# 添加脚本功能概述
parser=argparse.ArgumentParser(description="fftw analysis of density distribution")
# 添加参数
parser.add_argument("-t","--times") # -t: 简写， --times: 全称，调用时使用args.times
# 添加参数含义, python pythonScriptName.py -h 显示参数信息
parser.add_argument("-t","--times",help="number of copies of original density")
# 预设参数类型
parser.add_argument("-t","--times",help="number of copies of original density",type=int) 
# 设定参数默认值
parser.add_argument("-t","--times",help="number of copies of original density",default=4,type=int) # type： float, int, string(default) 
# 布尔型参数
parser.add_argument("-out","--ifoutput",help="output the figure",action="store_false",default=True)
# 固定选项型参数
parser.add_argument("-d","--density",help="show density, 0: coilA, 1: coilB, 2: coilC, 3: junction",type=int,choices=[0,1,2,3])

args=parser.parse_args()
# args.times 调用times参数
```

## example1

```python
import argparse
parser=argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here")
#parser.add_argument("square", help="display a square of a given number", type=int)
parser.add_argument("x", help="the base", type=int)
parser.add_argument("y", help="the exponent", type=int)
#parser.add_argument("-v", "--verbosity",help="increase output verbosity",type=int, choices=[0,1,2])
parser.add_argument("-v", "--verbosity",help="increase output verbosity", action="count",default=0)
args=parser.parse_args()

#answer=args.square**2
answer=args.x**args.y

if args.verbosity>=2:
    print(" Running'{}'".format(__file__))
if args.verbosity>=2:
    print(" {} to the power {} equals {}".format(args.x, args.y, answer))
elif args.verbosity>=1:
    print("{}^{} =={}".format(args.x, args.y, answer))
else: 
    print(answer)
```
## example2

```python
import argparse
parser=argparse.ArgumentParser()
group=parser.add_mutually_exclusive_group()
group.add_argument("-v","--verbose",action="store_true")
group.add_argument("-q","--quiet",action="store_true")
parser.add_argument("x",type=int, help="the base")
parser.add_argument("y",type=int, help="exponent")

args=parser.parse_args()

answer=args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(" {} to the power {} equals {}".format(args.x, args.y, answer))
else: 
    print("{}^{} == {}".format(args.x, args.y, answer))

```

## Links
- [argparse tutorial](https://docs.python.org/3.6/howto/argparse.html#id1)
- [argparse API reference information](https://docs.python.org/3.6/library/argparse.html#module-argparse)
- [argparse - 命令行选项与参数解析（译）](http://blog.xiayf.cn/2013/03/30/argparse/)
