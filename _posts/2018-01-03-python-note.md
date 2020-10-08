---
layout: post
title: Python Note
categories: Python
description: Python 语法
keywords: Python, Grammer,  语法
---

Updating......

廖雪峰 Python [教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000) 学习笔记

# 交互式命令

## 转义字符
- `\n` 换行
- `\b`退格
- `\f`换页
- `\r`换行，光标在上一行
- `\t` 制表符,八个空格
- `\\` \
- `r'xx'`则````中的内容默认不转义
- `b'xx'`默认````中的内容为utf8编码

## 多行输入

```python
print('''xxx
...xxx
...xxx
...xxx''')
```
## 编码
```python
print('中文')
ord('中')
chr(66)
chr(25991)
```
## 中文输入
文件中带中文，需要在文件开头加
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
## 格式化输出

```python
>>> 'hello,%s' % 'world!'
hello, world!
>>>'Hi, %s, you have $%d.' % ('Michel',10000)
Hi, Michel, you have $1000.
```

## 占位符

```python
%d  #整数
%f  #浮点数
%s  #字符串
%x  #十六进制整数
```
## 输出浮点数

```python
>>>'%2d-%02d' % (3,1)
'3-01'
>>>'%.2f' % 3.1415926
'3.14'
```
## List
```python
len() #list长度
list[-1]
list.append()
list.insert(x,'xxx') # 将'xxx'放到list的x位置，list下标从0开始
list.pop() #删除末尾元素
list.pop(i)
list[i]='xxx'
L=['Apple',123,True,['hello','world']]
```
## tuple

```python
#tuple: inmutable
#无类似于append, insert等方法
classmate=('a','b','c')
t=(1,) #定义只有一个元素的tuple时，要在第一个元素后加`,`，来避免歧义如果定义成t=(1),则我们定义的不是一个tuple，而是t=1,因为python默认将（）认为是数学公式中的小括号
>>>t=('a','b',['A','B'])
>>>t[2][0]='X'
>>>t[2][1]='Y'
>>>t 
('a','b',['X','Y'])
```

## 条件判断

```python
age=18 
if age>18:
    print('adult')
elif age>=6:
    print('teenager')
else:
    print('kid')
if x: #ｘ为非零数值、字符串、list时，就判断为True，否则为False
    print('True')
```

```python
youYear=input('the year of you birthday:')
s = int(youYear)
if birth >2000
    print('00前')
else:
    print('00后')
```

## 循环
```python
sum=0
for i in range(101):
    sum=sum+i
print(sum)
```
```python
sum=0
while i<101:
    sum=sum+i
    n=n+1
print(sum)
```
```python
n=0 
while n<10:
    n=n+1
    if n % 2 ==0:
        continue 
    print(n)
```
	    
## dict & set 
```python
# dict查找速度不会随着dict长度变大而变慢
# dict会占用大量内存
# dict是用空间换取时间的方法
>>>d={"michel":95,"bob": 75, "tracy":85}
>>>d["michel"]
95
>>>'tomas' in d
False
>>>d.pop('michel')
```
```python
#set可以看做数学中无重复、无序的集合
>>>s=set([1,2,3,2,3,1])
>>>s
{1,2,3}
>>>s.remove(1)
>>>s
{2,3}
```
## 可变对象和不可变对象
- list：可变对象
- str： 不可变对象
## 函数
```python
>>>from function_my_abs import my_abs # 前提是my_abs已经被定义在function_my_abs.py中并且该文件在当前目录
>>>my_abs(-19)
19
```
```python
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad openrand type')
    if  x>=0:
        print(x)
    else:
        print(-x)
```
```pytho
#### 返回多个参数
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
```
```python
#python返回多个值是作为一个tuple返回的
>>>x,y=move(0,0,3,20)
print(x,y) # 当tuple只有两个值时，可以省略括号(实际上完整的应该写成print((x,y))
```
## 默认参数
```python
def add_end(L=[]): # 默认参数必须为不可变对象，否则多次调用后会出现不同的结果
    L.append('end')
    return L
def add_end1(L=None):# 不可变对象
    if L is None:
        L=[]
    L.append('end')
    return L
```
## 可变参数
```python
def calc_sum(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum
#如果已经有一个list，希望将该list中所有元素作为可变参数输入函数，可以用calc_sum(*list)将list或者tuple中元素作为可变参数输入函数中
```
## 关键字参数
```python
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Michael',30)
person('Bob',25,city='Beijing')
extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)
```
```python
>>>python key_para.py
('name:', 'Michael', 'age:', 30, 'other:', {})
('name:', 'Bob', 'age:', 25, 'other:', {'city': 'Beijing'})
('name:', 'Jack', 'age:', 24, 'other:', {'city': 'Beijing', 'job': 'Engineer'})
```
```python
def function(argv1,argv2='beijing',*args,**kw) # argv1:必选参数，argv2:默认参数，*args:可变参数，函数接收的是一个tuple或者list，**kw：关键字参数，函数接收的是一个dict
```
## 递归函数
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1) #上述函数容易引起栈溢出
def fact1(n): # 改函数在经过优化的解释器中可以避免栈溢出
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
```
## 高级特性
### 切片

```python
L=['Michael','Sarah','Tracy','Bob','Jack']
L[0:3] 
L[:3]
L[1:3]
L[-2:]
num=list(range(100))
num[:10:2]
num[::5]
num[:]
```

### 迭代

```python
for i in 'abc':
    print(i)
for i, value in enumerate(['a','b','c']) #enumerate函数可以将一个list变成索引-元素对
    print(i,value)
```

## 列表生成式

```python
list(range(1,11))

[x*x for x in range(1,11)]

[x*x for x in range(1,11) if x%2==0]

[m + n for m in 'abc' for n in 'xyz']

import os 
[d for d in os.listdir('.')]

d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print (k,'=',v)
[k + '=' + v for k, v in d.items()]

L=['Hello','World','IBM','Apple']
[s.lower() for s in L]
```

## 生成器（generator)
```python
def fib(x):
    n,a,b=0,0,1
    while n<x:
        yield b # 当语句中出现yield时，该函数就不是一个函数，而是一个generator
        a,b=b,a+b
        n=n+1
    return
print(fib(3))
>>>python fib.py
<generator object fib at 0x7f900fab0780> #调用函数返回值，调用generator返回一个genetator对象

```
```python
def triangles(n):
    L=[1]
    while len(L)<n:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
for t in triangles(10):
    print(t)
>>>python yang_triangles.py
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
```
## 迭代器
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
#可以用for便历元素的数据类型, 一类是集合数据类,如list,tuple,dict,set, str等，一类是genetrator,包括生成器和带yield的 generator function,这些可以直接作用于for，成为iterable
print(isinstance({},Iterable))
print(isinstance([],Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))
#而生成器不仅可以作用于for循环，还可以用next()函数不断调用并返回下一个值，一直到抛出StopIteration错误
#可以被next()函数调用并不断返回下一个对象的，成为迭代器Iterator
from collections import Iterator
print(isinstance({},Iterator))
print(isinstance([],Iterator))
print(isinstance('abc',Iterator))
print('\n')
print(isinstance(iter({}),Iterator))
#生成器表示一个惰性计算的序列
>>>python iterator.py
True
True
True
True
False
False
False
False


True
```

## 函数式编程
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(abs)
f=abs
print(f)

print('\n')
def add(x,y,f): # 将函数作为参数输入函数，该函数成为高阶函数
    return f(x)+f(y)
print(add(-5,6,abs))
>>>python  functional_program.py
<built-in function abs>
<built-in function abs>
11
```
## map/reduce

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def f(x):
    return x*x
list1=range(10)
r=map(f,list1) # r是一个Iterator, Iterator 为惰性求值，需要用list（）函数让其将整个序列都求出来。
print(list(r))
>>>python map_test.py
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce 
def add(x,y):
    return x+y
list2=range(10)
print(reduce(add,list2)) # reduce(f,[x,y,z])= f(f(x,y),z)

def fn(x,y):
    return x*10 +y

list3=range(1,9,2)
print(reduce(fn,list3))

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def str2num(list0):
    return reduce(fn,map(char2num,list0))

def str2num1(list0):
    return reduce(lambda x,y:x*10+y,map(char2num,list0))
str='13579'
print(str2num(str))
print(str2num1(str))
>>>python reduce_test.py
45
1357
13579
13579
```
## filter
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','','B',None,'c',' ']))) # 删除空字符串
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x: x % n >0 

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
for n in primes():
    if n<60:
        print(n)
    else:
        break
>>>python3 filter_test.py
['A', 'B', 'c']
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
```

## sorted
```python 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(sorted([1,2,32,-3,5],key=abs))
print(sorted(['abc','AC','Tim','Lucy'],key=str.lower,reverse=True))
>>>python3 sort_test.py
[1, 2, -3, 5, 32]
['Tim', 'Lucy', 'AC', 'abc']
```
## 返回函数
## 闭包
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax = ax + n
        return ax
    return sum
#函数中定义了函数，并且内部函数可以调用外部函数的参数和局部变量，当函数返回内部函数时，相关参数和变量都保存在返回的函数中，这种成为闭包（Closure)
f=lazy_sum(1,2,3,23)

print(f)
print(f())
#每次返回的函数不一样，即使参数相同
f1=lazy_sum(1,2,3,23)
f2=lazy_sum(1,2,3,23)
print(f1==f2)
>>>python3 lazy_sum.py
<function lazy_sum.<locals>.sum at 0x7fd8a11ed510>
29
False
```
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1)
print(f2)
print(f3)
print('\n')
print(f1())
print(f2())
print(f3())
#返回闭包需要注意不要引用任何循环变量，或者后续会变化的变量
>>>python3 closure.py
<function count.<locals>.f at 0x7f3055a6d510>
<function count.<locals>.f at 0x7f3055a6d598>
<function count.<locals>.f at 0x7f3055a6d620>


9
9
9
```
## 匿名函数
```python 
def f(x):
    return x*x
#和下面的函数作用相同
f=lambda x: x*x 
#python对匿名函数的支持有限
```
- [ ] 装饰器
- [ ] 偏函数

## 模块
```python
#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# 第一行注释让该文件可以运行在Unix/Linux/Mac上
# 第二行注释表明文件本身用utf-8编码

'a test module'
# 上一行是模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__='liufaqiang'
#文档作者

import sys

#导入sys模块后，我们有变量sys指向该模块，利用sys这个变量，可以访问sys模块的所有功能。
#sys的argv变量存储了命令行的所有参数，至少有一个（第一个参数就是文  如module.py)

def test():
    args=sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello %s' % args[1])
    else:
        print('too much parameters')
if __name__=='__main__':
    test()
>>>python module.py
hello world
>>>python module.py liufaqing
hello liufaqiang
>>>python
>>>import module
>>>module.test()
hello world
```



## 进程和线程

### 多进程

```python
from multiprocessing import Process
import os 
def run_proc(name):
    print('Run child process %s,(%s)' % (name,os.getpid()))
if __name__=='__main__':
    print('Parent pricess %s.' % os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

>>>python process.py
Parent pricess 292.
Child process will start.
Run child process test,(293)
Child process end.
```
