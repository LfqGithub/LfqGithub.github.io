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
 
## 随机数
```python
$ vi random_function_comparison-numpy.py
import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(20000,4), columns=list('abcd')) # random.randn中的n: normal distribution
print('pd.DataFrame(np.random.randn(20000,4)).describe():\n',df.describe(),'\n') 
df=pd.DataFrame(np.random.rand(20000,4), columns=list('abcd')) # 0~1
print('pd.DataFrame(np.random.rand(20000,4)).describe():\n',df.describe(),'\n')
randint=np.random.randint(4,20000) # numpy.random.randint(low, high=None, size=None, dtype='l'), Return random integers from low (inclusive) to high (exclusive).
print('np.random.randint(4,20000): \n',randint,'\n')

```
```bash
$ python random_function_comparison-numpy.py

pd.DataFrame(np.random.randn(20000,4)).describe():
                   a             b             c             d
count  20000.000000  20000.000000  20000.000000  20000.000000
mean      -0.005510     -0.000253     -0.001603     -0.006190
std        1.008032      0.997202      1.005806      0.999230
min       -3.990401     -3.839888     -3.687128     -3.899739
25%       -0.687308     -0.674624     -0.679843     -0.677792
50%       -0.007345     -0.001680     -0.002064     -0.012789
75%        0.668355      0.670388      0.675867      0.662523
max        3.849040      3.696426      3.671636      4.367503 

pd.DataFrame(np.random.rand(20000,4)).describe():
                   a             b             c             d
count  20000.000000  20000.000000  20000.000000  20000.000000
mean       0.502510      0.499126      0.499444      0.498538
std        0.288140      0.289055      0.288057      0.289362
min        0.000008      0.000016      0.000047      0.000029
25%        0.257415      0.247476      0.249294      0.249817
50%        0.503497      0.498214      0.501608      0.496005
75%        0.750540      0.748842      0.748458      0.748513
max        0.999995      0.999970      0.999985      0.999954 

np.random.randint(4,20000): 
 3471 
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

