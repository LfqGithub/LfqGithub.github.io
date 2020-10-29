import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from timeit import timeit
from functools import reduce


def normal_for(x):
    s=0
    for i in range(x):
        s+=i
    print('normal for, result:',s)

def _add(x,y):
    return x+y

def _reduce(x):
    result=reduce(_add, range(x))
    print('reduce, result:',result)

@jit(nopython=True)
def jit_for(x):
    s=0
    for i in range(x):
        s+=i
    print('jit for, result:',s)




normal_for_t=timeit('normal_for(1000000)','from __main__ import normal_for',number=10)
jit_for_t=timeit('jit_for(1000000)','from __main__ import jit_for',number=10)
reduce_t=timeit('_reduce(1000000)','from __main__ import _reduce',number=10)
print('runtime of normal for:', normal_for_t)
print('runtime of jit for:', jit_for_t)
print('runtime of reduce:', reduce_t)


