
updating...

## 特点
- 优雅的语法糖，让工程中的代码复用变得更加艺术
- 给已经定义好的函数装饰一些功能
- 将函数或者对象作为参数传给另一个函数或者对象，并且返回新的函数对象，装饰器是这种概念的一种语法
  - ```python
    @decorator 
	def foo():
		pass
	# 相当于
	def foo():
		pass
	foo=decorator(foo)
	```

## 语法

### 典型装饰器
```python
from functools import wraps # 消除装饰器副作用，保持被装饰器修饰过的函数的元属性，如func.__name__等

# python decorator 装饰器学习
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

class Foo(object): # 类装饰器
    def __init__(self,func):
        self._func=func
    def __call__(self):
        print('class decorator running...')
        self._func()
        print('class decorator running...')
@Foo
def bar():
    print('bar')
bar()
```

```bash
$ python decorator.py
start callling function...
args:  (1, 2) {}
3
hello, world!
hello, world!
hello, world!
hello, world!
hello, world!
hello, world!
hello, world!
hello, world!
hello, world!
print_n_hello_world

class decorator running...
bar
class decorator running...
```

## Links
- [python decorator-zhihu](https://zhuanlan.zhihu.com/p/27382232)
- [python decorator-zhihu-too](https://www.zhihu.com/question/26930016/answer/99243411)

