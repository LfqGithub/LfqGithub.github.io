---
layout: wiki
title: Pandas
---

# Syntax

## 基本元素

- Series: 一维
- DataFrame: 二维

# 合并

```python
import pandas as pd
import numpy as np

def use_concat():
    # concat: pandas.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)
    df1=pd.DataFrame(np.random.randn(6,4), columns=list('abcd'))
    df2=pd.DataFrame(np.random.randn(6,4), columns=list('abcd'))
    df3=pd.DataFrame(np.random.randn(6,4), columns=list('abcd'))
    print('df1:\n', df1,'\n')
    print('df2:\n', df2,'\n')

    concat_df=pd.concat([df1,df2,df3]) # 保留index
    print('concat df1, df2, df3:\n', concat_df, '\n')

    concat_df=pd.concat([df1,df2],ignore_index=True) # 不保留index
    print('concat df1, df2, ignore_index=True:\n', concat_df, '\n')

    concat_df=pd.concat([df1,df2],ignore_index=True) # 不保留index
    print('concat df1 df2, ignore_index=True:\n', concat_df, '\n')

    concat_df=pd.concat([df1,df2],keys=['df1','df2']) # 不保留index , 如ignore_index=True, 则keys设置不生效
    print('concat df1 df2, keep keys\n', concat_df, '\n') # multiindex? 
    print('concat_df.loc[df1]:\n', concat_df.loc['df1'], '\n')

    # 横向合并dataframe
    concat_df=pd.concat([df1,df2], axis=1) # 横向合并dataframe
    print('concat df1 df2, axis=1: \n', concat_df, '\n')
    # other parmeters: join_axes=[df1.index]
    
def use_append():
    # append: DataFrame.append(other, ignore_index=False, verify_integrity=False, sort=False)
    # 可将append看作concat的早期版本
    df1=pd.DataFrame(np.random.randn(6,4), columns=list('abcd'))
    df2=pd.DataFrame(np.random.randn(6,4), columns=list('abcd'))

    append_df=df1.append(df2)
    print('df1.append(df2):\n', append_df, '\n')
    append_df=df1.append(df2,ignore_index=True)
    print('df1.append(df2,ignore_index=True):\n', append_df, '\n')

def use_merge():
    '''
    - merge: DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
    - pd.merge只能用于两个表的拼接，从参数left和right可以看出是左右拼接，只可以左右拼接。
    - 如果两个表中有相同的列，则拼接时不用指定哪个字段作为主键
    '''
    df1=pd.DataFrame(np.random.randn(6,4), columns=list('abcd'),index=list('123456'))
    df2=pd.DataFrame(np.random.randn(6,4), columns=list('defg'),index=list('456789'))
    df1['key']=list('abcdef')
    df2['key']=list('bcdefg')
    print('df1:\n', df1,'\n')
    print('df2:\n', df2,'\n')
    merged_df=pd.merge(df1,df2,on='key') # on=key: 将两dataframe中列相同的值连接到一行上, how默认为'inner', 将key列值不相同的行删除
    print('merged df, how=inner:\n', merged_df, '\n') 
    merged_df=pd.merge(df1,df2,on='key', how='outer') #how='outer', 保留key值不相同的行
    print('merged df, how=outer:\n', merged_df, '\n') 
    left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K1', 'K0', 'K1'], 'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']})
    right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K0', 'K0'], 'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']})
    print('left dataframe:\n', left,'\n')
    print('right dataframe:\n', right,'\n')
    result=pd.merge(left, right,on='key1') # 相同的key组合在一起. 如果某一个dataframe中有两个相同的key对应元素有两个相同的，则相应的多出一行
    print('pd.merge(left, right, key=key1):\n', result,'\n')
    result=pd.merge(left, right,on=['key1','key2']) 
    print('pd.merge(left, right, key=key1, key2):\n', result,'\n')


#use_concat()
#use_append()
use_merge()


# link: https://zhuanlan.zhihu.com/p/70438557
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
# https://izziswift.com/differences-between-merge-and-concat-in-pandas/
```


## 轴(axis)的概念

```python

import numpy as np
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180)

dates=pd.date_range('20200121', periods=6)
df=pd.DataFrame(np.random.randn(6,4), index=dates,columns=list('abcd'))

print('df:\n', df, '\n')
print('df.mean(0):\n', df.mean(0), '\n')
print('df.mean(1):\n', df.mean(1), '\n')
print('df.apply(lambda x:x.max()-x.min(), axis=0):\n', df.apply(lambda x:x.max()-x.min(), axis=0))
print('df.apply(lambda x:x.max()-x.min(), axis=1):\n', df.apply(lambda x:x.max()-x.min(), axis=1))

'''
轴的概念
默认的轴为axis=0, 即垂直向下的方向。
axis的重点在于方向，而不是行和列。
- axis=0
  - 沿着行的垂直向下 
- axis=1: 
  - 沿着列的方向水平延申, 表示横轴，方向从左到右
  - 当axis=1时，数组的变化是横向的，体现出来的是列的增加和减少。
  - 如果是求平均，意味着从左到右横向求平均，如果是拼接，意味着左右横向拼接，如果是drop, 横向变化，体现为列的减少
>> links: [python数据分析里axis=0/1 行列定义为什么每次都不同？ - Isco的回答 - 知乎](https://www.zhihu.com/question/58993137/answer/375111564)
'''
```
```bash
$ python axis-pd.py

df:
                    a         b         c         d
2020-01-21 -0.065037 -0.753123 -1.462927 -0.995091
2020-01-22 -1.608109 -0.927458  1.084200 -1.180333
2020-01-23 -0.262473 -0.847355  1.165586  0.402265
2020-01-24 -0.664000  0.820257  1.442003  0.389481
2020-01-25 -0.762001  1.888360 -0.666509  1.081992
2020-01-26 -0.805037  0.810417 -0.638767 -0.610019 

df.mean(0):
 a   -0.694443
b    0.165183
c    0.153931
d   -0.151951
dtype: float64 

df.mean(1):
 2020-01-21   -0.819045
2020-01-22   -0.657925
2020-01-23    0.114506
2020-01-24    0.496935
2020-01-25    0.385460
2020-01-26   -0.310852
Freq: D, dtype: float64 

df.apply(lambda x:x.max()-x.min(), axis=0):
 a    1.543072
b    2.815817
c    2.904930
d    2.262326
dtype: float64
df.apply(lambda x:x.max()-x.min(), axis=1):
 2020-01-21    1.397890
2020-01-22    2.692309
2020-01-23    2.012941
2020-01-24    2.106003
2020-01-25    2.650361
2020-01-26    1.615454
Freq: D, dtype: float64
```

## 初始化

```bash
$ import pandas as pd 
$ obj0=pd.Series([1,2,3,4]) # 从list创建Series
$ obj1=pd.Series(np.array([10,20,30,40])) # 从numpy array创建Series
$ obj2=pd.Series([10,20,30,40], index=['a','b','c','d']) # 添加index
$ obj0.index
RangeIndex(start=0, stop=4, step=1)
$ obj0.values # 返回 np.array
array([1,2,3,4])
$ dates=pd.date_range('20130102', periods=6)
$ df=pd.DateFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
$ df 
 A         B         C         D
 2013-01-02  1.178772 -0.558339 -1.488682 -2.019443
 2013-01-03  0.283135 -0.726245 -0.159991  0.894098
 2013-01-04  0.155445 -0.481355 -0.417834  0.594135
 2013-01-05  0.080791 -1.152969  0.167891 -0.536811
 2013-01-06  0.987230 -1.559071  0.949769  0.116051
 2013-01-07  1.352924  0.242703 -0.194658  0.569674
$ s1=pd.Series([1,2,3,4,5,6]), index=pd.date_range('20130102',period=6))
$ s1 
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
$ df1=df.copy()
$ df1['F']=s1
$ df1
                   A         B         C         D  F
2013-01-02  1.178772 -0.558339 -1.488682 -2.019443  1
2013-01-03  0.283135 -0.726245 -0.159991  0.894098  2
2013-01-04  0.155445 -0.481355 -0.417834  0.594135  3
2013-01-05  0.080791 -1.152969  0.167891 -0.536811  4
2013-01-06  0.987230 -1.559071  0.949769  0.116051  5
2013-01-07  1.352924  0.242703 -0.194658  0.569674  6

```

## 查看

```bash
$ df.head(n) # 查看前n行，默认n=5
$ df.tail(n)
$ df.index
DatetimeIndex(['2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05',
               '2013-01-06', '2013-01-07'],
			                 dtype='datetime64[ns]', freq='D')
$ df.columns
Index(['A', 'B', 'C', 'D'], dtype='object')
$ (df.T).index  # df.T 交换index和columns
Index(['A', 'B', 'C', 'D'], dtype='object')
$ (df.T).columns
DatetimeIndex(['2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05',
               '2013-01-06', '2013-01-07'],
			                 dtype='datetime64[ns]', freq='D')
```

## 排序

- ```bash
  # 按轴排序
  $ df.sort_index(axis=0, ascending=False) # ascending默认为True
  A         B         C         D
  2013-01-07  1.352924  0.242703 -0.194658  0.569674
  2013-01-06  0.987230 -1.559071  0.949769  0.116051
  2013-01-05  0.080791 -1.152969  0.167891 -0.536811
  2013-01-04  0.155445 -0.481355 -0.417834  0.594135
  2013-01-03  0.283135 -0.726245 -0.159991  0.894098
  2013-01-02  1.178772 -0.558339 -1.488682 -2.019443
  $ df.sort_index(axis=1, ascending=False) 
  2013-01-02 -2.019443 -1.488682 -0.558339  1.178772
  2013-01-03  0.894098 -0.159991 -0.726245  0.283135
  2013-01-04  0.594135 -0.417834 -0.481355  0.155445
  2013-01-05 -0.536811  0.167891 -1.152969  0.080791
  2013-01-06  0.116051  0.949769 -1.559071  0.987230
  2013-01-07  0.569674 -0.194658  0.242703  1.352924
  # 按值排序
  $ df.sort_values(by='B')
  A         B         C         D
  2013-01-06  0.987230 -1.559071  0.949769  0.116051
  2013-01-05  0.080791 -1.152969  0.167891 -0.536811
  2013-01-03  0.283135 -0.726245 -0.159991  0.894098
  2013-01-02  1.178772 -0.558339 -1.488682 -2.019443
  2013-01-04  0.155445 -0.481355 -0.417834  0.594135
  2013-01-07  1.352924  0.242703 -0.194658  0.569674
  ```

## 计算

```bash
$ df.mean() # 对行进行平均
A    0.673049
B   -0.705879
C   -0.190584
D   -0.063716
dtype: float64
$ df.mean(axis=1) # 对列进行平均
2013-01-02   -0.721923
2013-01-03    0.072749
2013-01-04   -0.037402
2013-01-05   -0.360275
2013-01-06    0.123495
2013-01-07    0.492661
Freq: D, dtype: float64
```

## 从文件读取数据

```bash
# pd.read_ + Tab # check the supported file formats
# read_csv parse 'a\tb' while read_table parse 'a,b'
df0=pd.read_csv('closeprice.csv',edcoding='gbk') 
df1=pd.read_table('closeprice.csv')
df2=pd.read_csv('testgz.gz',compression='gzip',header=0, sep=',',quotechar='"')
df3=pd.read_table(gzip.open('testgz.gz'),sep=',') # read .gz file
df4=pd.ExcelFile('./a.xlsx') # pip install openpyxl
```

## 修改/删除

```bash
$ df.drop(['A'], axis=1)  # axis=1等价于axis='columns'默认为columns
B         C         D
2013-01-02 -0.558339 -1.488682 -2.019443
2013-01-03 -0.726245 -0.159991  0.894098
2013-01-04 -0.481355 -0.417834  0.594135
2013-01-05 -1.152969  0.167891 -0.536811
2013-01-06 -1.559071  0.949769  0.116051
2013-01-07  0.242703 -0.194658  0.569674
$ df.drop(df.index[2])
A         B         C         D
2013-01-02  1.178772 -0.558339 -1.488682 -2.019443
2013-01-03  0.283135 -0.726245 -0.159991  0.894098
2013-01-05  0.080791 -1.152969  0.167891 -0.536811
2013-01-06  0.987230 -1.559071  0.949769  0.116051
2013-01-07  1.352924  0.242703 -0.194658  0.569674
$ df.iat[0,1]=0
$ df.at[dates[0],'A']=0
$ df.loc[:, 'D']=np.array([5]*len(df))
$ df[df>0]=-df
```

## 替代/重命名

```bash
a.replace(1,np.nan)
a.rename(columns={columns={'Unnamed: 0':'id'})
```

## 索引

- loc: location, iloc: index location
- selecting via `[]`, which slices the rows
- label slicing, both endpoints are included: `df.loc['20200702',['A','B]]`

```bash
$ df.loc[;,'A'] 
2013-01-02    1.178772
2013-01-03    0.283135
2013-01-04    0.155445
2013-01-05    0.080791
2013-01-06    0.987230
2013-01-07    1.352924
$ df.iloc[:,[1,4]] # 索引
                B         C
2013-01-02 -0.558339 -1.488682
2013-01-03 -0.726245 -0.159991
2013-01-04 -0.481355 -0.417834
2013-01-05 -1.152969  0.167891
2013-01-06 -1.559071  0.949769
2013-01-07  0.242703 -0.194658
a.ix[:4,['ticker','closePrice']] 
$ df.ix[:4, ['A','C']] # 自动判断索引类型并且决定使用位置还是标签进行切片
                A         C
2013-01-02  1.178772 -1.488682
2013-01-03  0.283135 -0.159991
2013-01-04  0.155445 -0.417834
2013-01-05  0.080791  0.167891
$ df[df.A>0.5]
                A         C
2013-01-02  1.178772 -1.488682
2013-01-03  0.283135 -0.159991
2013-01-04  0.155445 -0.417834
2013-01-05  0.080791  0.167891
$ df2=df.copy()
$ df2['E']=['one','two','three','four','five','six']
$ df2
                A         B         C         D      E
2013-01-02  1.178772 -0.558339 -1.488682 -2.019443    one
2013-01-03  0.283135 -0.726245 -0.159991  0.894098    two
2013-01-04  0.155445 -0.481355 -0.417834  0.594135  three
2013-01-05  0.080791 -1.152969  0.167891 -0.536811   four
2013-01-06  0.987230 -1.559071  0.949769  0.116051   five
2013-01-07  1.352924  0.242703 -0.194658  0.569674    six
$ df2[df2['E'].isin(['two','four'])]
                 A         B         C         D     E
2013-01-03  0.283135 -0.726245 -0.159991  0.894098   two
2013-01-05  0.080791 -1.152969  0.167891 -0.536811  four
# df.at(), df.iat() 访问单个标量元素
```

## 筛选

```bash
a[a.closePrice>10]
a[(a.closePrice>10) & (a.ticker>3)]
a[(a.closePrice>10)*1+(a.ticker>3)*1==2] # 用于条件筛选，至少或者至多满足几个条件时进行筛选
```

## 分组
```bash
bins=[4,9,10,20,30]
cat=pd.cut(a.closePrice,bins)
pd.value_counts(cat)
group_names=['low','middle_1','middle_2','high']
pd.cut(a.closePrice,bins,labels=group_names]
```

## 输出

```bash
import pandas as pd 
pd.set_optiom("display.max_rows",1000)
pd.set_optiom("display.max_columns",20)
pd.set_optiom('precision',7)
pd.set_optiom('large_repr','truncate')
```

## Transform

```bash
obj.to_dict()
```
- Sort
```bash
import pandas as pd 
data=pd.DataFrame({'group':['a']*3+['b']*3+['c']*3, 'ounces': [4,3,12,6,7.5,8,3,5,6]})
data.sort_values(by=['group','ounces'],ascending=[False,True], inplace=True)
data.drop_duplicates()
data.drop_duplicates(subset=['k1'],keep='last')
data[data.duplicated()]
```

## operation
```bash
import pandas as pd 
a=pd.read_csv('closeprice.csv',edcoding='gbk')
b={1:'银行',2:'房地产',4:'医药',5:'房产',6:'采掘',7:'休闲',8:'机械设备'}
a['ind']=a.ticker.map(b)
a.describe().T
```

- help
```bash
$ pd-Series. + Tab # 查找Series中的函数/方法
```

## 常用函数

- describe()函数
  - 四分位差

- Pivot Table
  - A pivot table is a table that summarizes data from another table, and is made by applying an operation such as sorting, averaging, or summing to data in the first table, 
    typically including grouping of the data.--[pivot table-wiki](https://en.wikipedia.org/wiki/Pivot_table)

## 绘图

- boxplot

## 举例

- ### Series

```python
import pandas as pd

print('Series in Pandas...\n')
s0=pd.Series(['Python','C++','c','Matlab'])
print('s0: \n',s0,'\n')
s1=pd.Series(['Python','C++','c','Matlab'],index=['a','b','c','d'])
print('s1: \n',s1,'\n')
print("s1['a']: ",s1['a'],'\n')
sd={'a':'Python','b':'C++','c':'c','d':'Matlab'}
s2=pd.Series(sd)
print('s2: \n',s2,'\n')
s3=pd.Series(s2,index=['a','b','d','e'])
print('s3: \n',s3,'\n')
print('s3 if null: \n',pd.isnull(s3),'\n')
print('s3 if not null: \n',pd.notnull(s3),'\n')
s2.index=['a1','a2','a3','a4']
print('s2: \n',s2,'\n')
print('s2*2: \n',s2*2,'\n')
print('s1+s2: \n',s1+s2,'\n')

# Output

Series in Pandas...

s0: 
 0    Python
1       C++
2         c
3    Matlab
dtype: object 

s1: 
 a    Python
b       C++
c         c
d    Matlab
dtype: object 

s1['a']:  Python 

s2: 
 a    Python
b       C++
c         c
d    Matlab
dtype: object 

s3: 
 a    Python
b       C++
d    Matlab
e       NaN
dtype: object 

s3 if null: 
 a    False
b    False
d    False
e     True
dtype: bool 

s3 if not null: 
 a     True
b     True
d     True
e    False
dtype: bool 

s2: 
 a1    Python
a2       C++
a3         c
a4    Matlab
dtype: object 

s2*2: 
 a1    PythonPython
a2          C++C++
a3              cc
a4    MatlabMatlab
dtype: object 

s1+s2: 
 a     NaN
a1    NaN
a2    NaN
a3    NaN
a4    NaN
b     NaN
c     NaN
d     NaN
dtype: object 
```

### DataFrame

```python

import pandas as pd

data = {"name":["yahoo","google","facebook"], "marks":[200,400,800], "price":[9, 3, 7]}
df0=pd.DataFrame(data)
print('df0: \n', df0,'\n')
# 和dict不同地是，DataFrame可以规定顺序
df1=pd.DataFrame(data,columns=['name','price','marks'])
print('df1: \n', df1,'\n')
df2=pd.DataFrame(data, columns=['name', 'price', 'marks', 'debt'], index=['a','b','c'])
print('df2: \n', df2,'\n')
# 字典套字典
newdata = {"lang":{"firstline":"python","secondline":"java"}, "price":{"firstline":8000}}
df3=pd.DataFrame(newdata)
print('df3: \n', df3,'\n')
print('df2.index: \n', df2.index,'\n')
print('df2.columns: \n', df2.columns,'\n')
print('df2.columns_price: \n', df2['price'][:],'\n')
print('df2.columns_price_1st: \n', df2['price']['a'],'\n')

# Output

df0: 
        name  marks  price
0     yahoo    200      9
1    google    400      3
2  facebook    800      7 

df1: 
        name  price  marks
0     yahoo      9    200
1    google      3    400
2  facebook      7    800 

df2: 
        name  price  marks debt
a     yahoo      9    200  NaN
b    google      3    400  NaN
c  facebook      7    800  NaN 

df3: 
               lang   price
firstline   python  8000.0
secondline    java     NaN 

df2.index: 
 Index(['a', 'b', 'c'], dtype='object') 

df2.columns: 
 Index(['name', 'price', 'marks', 'debt'], dtype='object') 

df2.columns_price: 
 a    9
b    3
c    7
Name: price, dtype: int64 

df2.columns_price_1st: 
 9 

```


## References

- [箱型图-boxplot](https://blog.csdn.net/You_are_my_dream/article/details/53435733)
- [read_csv函数参数](https://www.cnblogs.com/datablog/p/6127000.html)
- [pandas中axis的理解](https://www.jianshu.com/p/9aa448ea397c)

## 教程
- [Pandas 中文教程--w3cschool--Recommend](https://www.w3cschool.cn/hyspo/hyspo-sufo3721.html)
- [pandas guide](https://media.readthedocs.org/pdf/pandasguide/latest/pandasguide.pdf)
- [python pandas tutorial](https://www.tutorialspoint.com/python_pandas/python_pandas_tutorial.pdf)
- [Pandas使用](http://wiki.jikexueyuan.com/project/start-learning-python/311.html)

