---
layout: wiki
title: Python
categories: Python
description: python 学习
keywords: python, basic
---

Python 记录、理解, updating...

## Syntax

- `and/or`
  - `(a and b)`: 当a,b都为真，返回第二个值
  - `(a or b)`: 当a,b都为真，返回第一个值
> The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned. The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.

### Note

- 修改元素禁止使用下列方法
```python
a=[1,2,3,4]
for i in a:
	i=i*2
print(a)
 [1,2,3,4]
```
> 原因：`i`的id已经不是原来的id

```python
a=[1,2,3,4,5]
for i,el in enumerate(a):
	if el==3:
		del a[i]
print(a)
[1,2,4,5]
```
> 原因：for 遍历过程中，如果删除了其中的一个元素，会导致后面元素前移，出现漏网之鱼. 涉及到列表的插入与删除，不要用`for`
```python
a=[1,2,3,4,5]
for i in range(len(a)):
    a[i]*=2
print(a)
[2,4,6,8,10]
```

## pip

- update all pip-installed packages
```python
import pip
from subprocess import call
for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
```
- `pip show package-name`: Show information about installed packages.

