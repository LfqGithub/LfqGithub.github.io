def fib(x):
    n,a,b=0,0,1
    while n<x:
        yield b
        a,b=b,a+b
        n=n+1
    return
print(fib(3))
