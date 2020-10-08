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
