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
