---
layout: wiki
title: Numpy
---

## Elaboration

- 高性能科学计算和数据分析基础包
- Pandas, Scikit-Learn, StatMOdels库的构建基础

## Syntax 

- 固定缩写
  ```bash
  import numpy as np # 约定俗成的缩写
  ```
- ndarray中，所有元素类型必须相同
- 创建数组
  ```bash
  $ import numpy as np
  $ data=[1,2,3,4]
  $ arr=np.array(data)
  $ arr
  array([1,2,3,4])
  $ data1=[data,data]
  $ arr1=np.array(data1)
  $ arr1
  array([1,2,3,4],
        [1,2,3,4])
  $ np.zeros([3,3])
  $ np.ones([3,3])
  $ np.arange(1,10,2)   # 步长为 2
  $ np.linspace(1,10,4) # 长度为 4
  ```

### 数据类型

- bool
- int
- float
- string_
- unicode_

### 代码向量化
- ```bash
  arr1*arr2
  arr1+arr2
  arr1-arr2
  arr1**2
  ```
### 数组统计方法
- sum
- mean
- std: 标准差
- var: 方差
- min/max
- argmin/argmax: 最大值索引
- cumsum/cumprod: 所有元素的累计和/累计积

