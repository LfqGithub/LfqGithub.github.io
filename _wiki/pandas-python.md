---
layout: wiki
title: Pandas
---

# Syntax

## 基本元素

- Series: 一维
- DataFrame: 二维

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

- axis的概念：
  - 使用0值表示沿着每一列或行标签\索引值向下执行方法
  - 使用1值表示沿着每一行或者列标签模向执行对应的方法
- ```bash
  # 按轴排序
  $ df.sort_index(axis=0, ascending=False) # axis=1: 列, 0: 行， 默认为0, ascending默认为True
  A         B         C         D
  2013-01-07  1.352924  0.242703 -0.194658  0.569674
  2013-01-06  0.987230 -1.559071  0.949769  0.116051
  2013-01-05  0.080791 -1.152969  0.167891 -0.536811
  2013-01-04  0.155445 -0.481355 -0.417834  0.594135
  2013-01-03  0.283135 -0.726245 -0.159991  0.894098
  2013-01-02  1.178772 -0.558339 -1.488682 -2.019443
  $ df.sort_index(axis=1, ascending=False) # axis=1: 列, 0: 行， 默认为0
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
- [pandas guide](https://media.readthedocs.org/pdf/pandasguide/latest/pandasguide.pdf)
- [python pandas tutorial](https://www.tutorialspoint.com/python_pandas/python_pandas_tutorial.pdf)
- [Pandas使用](http://wiki.jikexueyuan.com/project/start-learning-python/311.html)

