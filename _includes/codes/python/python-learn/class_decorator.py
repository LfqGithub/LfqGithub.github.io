class Foo(object):
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
