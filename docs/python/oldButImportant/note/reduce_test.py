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
