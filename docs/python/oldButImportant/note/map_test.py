#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def f(x):
    return x*x
list1=range(10)
r=map(f,list1) # r是一个Iterator, Iterator 为惰性求值，需要用list（）函数让其将整个序列都求出来。
print(list(r))

