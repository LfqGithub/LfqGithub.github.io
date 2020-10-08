# python decorator 装饰器学习

from functools import wraps # 消除装饰器副作用，保持被装饰器修饰过的函数的元属性，如func.__name__等

def foo_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('start callling function...')
        print('args: ',args,kwargs)
        res=func(*args,**kwargs)
        return res
    return wrapper

def repeat_twice(func):
    @wraps(func)
    def _repeat_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return _repeat_twice

def repeat(n): # 执行func函数n次
    def repeat_n(func):
        @wraps(func)
        def _repeat_n(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return _repeat_n
    return repeat_n

@foo_wrapper
def foo(a,b):
	print(a+b)
foo(1,2)

@repeat_twice
@repeat_twice
def print_hello_world():
    print('hello, world!')

@repeat(5)
def print_n_hello_world():
    print('hello, world!')

print_hello_world()

print_n_hello_world()
print(print_n_hello_world.__name__)
