---
layout: wiki
title: 位运算
keywords: [bit, operation]
categories: [math, code]
description: 
---

# 位运算

## 常用操作

- 如果想获得常见的二进制组合的数字？ 如0b10101010，其实是十六进制的0xaa

- 遍历一个二进制数：

```python
for i in range(32):
    if a & (1 << i):
        do something
```


### 数1

```python
# 计算一个二进制数中1的数量
num_1=0
while n:
    num_+=n & 1
    n=n>>1
```



## Ref

- [位运算](https://www.cnblogs.com/Neeo/articles/10536202.html#%E6%8C%89%E4%BD%8D%E4%B8%8E-)
- [位运算--奇偶位交换](https://blog.csdn.net/weixin_46422390/article/details/106266981)
- [计算二进制数中1的个数](https://www.cnblogs.com/graphics/archive/2010/06/21/1752421.html)

