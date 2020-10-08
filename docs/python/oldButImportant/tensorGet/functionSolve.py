import numpy as np 
import sympy as sm

x=sm.Symbol('x')
y=sm.Symbol('y')
z=sm.Symbol('z')

ans=sm.solve([x*2+y-3,x+2*y-3],[x,y]) # ans is a dict
print(ans[x])
print(ans[y])


