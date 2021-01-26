---
layout: wiki
title: Python Syntax
keywords: [python, syntax]
categories: Python
comments: false
---

Updating...

# Index Rule of List

```python
def index_rule():
    a=list('abcdefg')
    print('Origin list a:\n', a, '\n')
    print('a[1:5] \n', a[1:5])
    print('a[1:1] \n', a[1:1]) 
    print('a[1:10] \n', a[1:10]) # 超出边界不会报错，范围到最后一个为止
    print('a[-2:] \n', a[-2:])
    print('a[::2] \n', a[::2], '\n')
    print('a[1:-2] \n', a[1:-2], '\n') # a[x:y], 为[a[x], a[y]), 即不包含最后一个索引, 如x==y, 则返回空值
    print('a[-10:2] \n', a[-10:2], '\n') # 反向超出边界则从第一个算起，不会报错
    print('a[::-1] \n', a[::-1], '\n') # 反转列表
    print('a[::-2] \n', a[::-2], '\n') 
    print('a[-2::-2] \n', a[-2::-2], '\n') 

index_rule()
```

```bash
$ python python_index_rule.py

Origin list a:
 ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 

a[1:5] 
 ['b', 'c', 'd', 'e']
a[1:1] 
 []
a[1:10] 
 ['b', 'c', 'd', 'e', 'f', 'g']
a[-2:] 
 ['f', 'g']
a[::2] 
 ['a', 'c', 'e', 'g'] 

a[1:-2] 
 ['b', 'c', 'd', 'e'] 

a[-10:2] 
 ['a', 'b'] 

a[::-1] 
 ['g', 'f', 'e', 'd', 'c', 'b', 'a'] 

a[::-2] 
 ['g', 'e', 'c', 'a'] 

a[-2::-2] 
 ['f', 'd', 'b'] 
```


