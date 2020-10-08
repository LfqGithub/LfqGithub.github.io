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
