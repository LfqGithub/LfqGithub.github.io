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

