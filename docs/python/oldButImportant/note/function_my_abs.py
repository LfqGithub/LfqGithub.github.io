def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad openrand type')
    if  x>=0:
        print(x)
    else:
        print(-x)
