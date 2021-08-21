---
layout: wiki
title: 位运算
keywords: [bit, operation]
categories: [math, code]
use_math: true
description: 
---

# 位运算
## 位运算规律
### 异或
- `a^b=b^a`
- `a^b^c=a^(b^c)=(a^b)^c`
- `a^b^a=b,a^a^b=b, b^a^a=b`
- 若`d=a^b^c`, 则`a=d^b^c`
[常见用途](https://blog.csdn.net/feliciafay/article/details/6842604)

1. 不适用临时变量交换两个值

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

## 二进制的表示方法
小数如何[转变为二进制数](https://spaces.ac.cn/archives/1907)? 
以0.1 为例， 
- 0.1 x 2 =0.2, 取整数部分0，得到了0.0
- 0.2 x 2 =0.4, 取整数部分0，得到了0.00
- 0.4 x 2 =0.8, 取整数部分0，得到了0.000
- 0.8 x 2 =1.6, 取整数部分1，得到了0.0001
- 0.6 x 2 =1.2, 取整数部分1，得到了0.00011
- 0.2 x 2 =0.4, 取整数部分0，得到了0.00011
$\vdots$

这样无限循环下去，可以推测出循环节为0011, 而0.1的二进制表示为$0.0001100110011\cdots$.
其实大多数有限小数的二进制都是无限循环的，除非该小数小数点后为$1/2^n$。



## Ref

- [位运算](https://www.cnblogs.com/Neeo/articles/10536202.html#%E6%8C%89%E4%BD%8D%E4%B8%8E-)
- [位运算--奇偶位交换](https://blog.csdn.net/weixin_46422390/article/details/106266981)
- [计算二进制数中1的个数](https://www.cnblogs.com/graphics/archive/2010/06/21/1752421.html)

