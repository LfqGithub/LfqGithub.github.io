

# 正则表达式

`\d` 数字 

`00\d` 匹配00加上一个数字,如`007`

`\d\d\d` 匹配三个数字，如`007`

`\w\w\d` 两个字符加一个数字，如`py3`


`.`匹配任意字符

`py.` 可以匹配`pyi`,`py!`等 

`\d{3}` 可以匹配三个数字，如`010`

`\d{3-8}` 匹配3-8个数字

`*` 任意个字符，包括0个

`\s` 匹配一个空格

`+` 至少一个字符

`?` 表示1个或者0个字符

`{n}` n个字符

`{n,m}` n-m个字符

`\d{3}\s+\d{3,8}` 3个数字加一个空格加3-8个字符，可以匹配以任意个空格匹配以任意个空格隔开的带区号的电话号码

`\d{3}\-\d{3,8}` 类似于`010-12345`这样的电话号码

`[0-9a-zA-Z\_]` 一个数字、字母或者下划线

`[0-9a-zA-Z\_]+` 至少有一个数字、字母或者下划线组成的字符串，如`a100`,`0_z`等

`[a-zA-Z\_][0-9a-zA-Z\_]*` 一个由字母或者下划线开头，后面接一个由数字、字母或者下划线组成的字符串，也就是python的合法变量

`[a-zA-Z\_][0-9a-zA-Z\_]{0-19}` 更精确的限制了变量的长度是1-20个字符

`^` 表示行的开头

`^\d` 必须以数字开头

`$` 行的结束

`\d$` 以数字结束

`^py$` 一行只有`py`


## re模块

由于python的字符串本身也需要转义，所以，建议使用python的r前缀，这样，就不用考虑转义的问题了。

```python
s=r'abc\-001 
#相当于下面的表达式
s=abc\\-001
```

```python
#match()方法判断是否匹配，如果成功，返回一个mathch对象，如果不匹配，返回None
>>>re.match(r'\d{3}\-\d{3,8}$','010-12345')
<sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>>re.match(r'\d{3}\-\d{3,8}$','010 12345')

```
### 切分字符串
```python
>>>'a b  c'.split(' ')
['a','b',' ','c']
#无法识别连续的空格
>>>re.split(r'\s+','a b  c')
['a','b','c']
#无论多少空格都可以
>>>re.split(r'[\s\,\;]+','a,b;; c   d')
['a','b','c','d']
```
### 分组
```python
>>>m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
>>>m
m=re.match(r'^(\d{3})-(\d{3-8})$','010-12345')
>>>m.group(0)
'010-12345'
>>>m.group(1)
'010'
>>>m.group(2)
'12345'
#m.group的第一个元素永远是元素本身
>>> t = '19:05:30'
>>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
>>> m.groups(1)
19
>>> m.groups(2)
05
>>> m.groups(3)
30
#对于2-30这样的非法日期，正则无法识别，需要程序配合
```

```python
>>> re.match(r'^(\d+)(0*)$', '102300').groups()
('102300', '')
>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')
#注意贪婪匹配
```
### 编译
```python
>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
```
### 作业
请尝试写一个验证Email地址的正则表达式。

`someone@gmail.com`
`bill.gates@microsoft.com`

提取出邮件中的姓名

`<Tom Paris> tom@voyager.org`

答题:

```python
import re
>>>re.match(r'[a-z]+\@gmail.com','some@gmail.com')
<_sre.SRE_Match object; span=(0, 14), match='some@gmail.com'>
>>>re.match(r'[a-z]+\.[a-z]+\@microsoft.com','bill.gates@microsoft.com')
<_sre.SRE_Match object; span=(0, 24), match='bill.gates@microsoft.com'>
>>>a=re.match(r'<([a-zA-Z]+\s[a-zA-Z]+)>\s[a-z]+\@voyager.org','<Tom Paris> tom@voyager.org')
>>>a.group(1)
'Tom Paris'
```
