#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(abs)
f=abs
print(f)

print('\n')
def add(x,y,f): # 将函数作为参数输入函数，该函数成为高阶函数
    return f(x)+f(y)
print(add(-5,6,abs))

