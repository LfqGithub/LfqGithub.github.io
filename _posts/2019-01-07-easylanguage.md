---
layout: post
title:  EasyLanguage
categories: [EasyLanguage]
description: 
keywords: easylanguage
---

updating...

# 基础知识

## 数值类型
- 数值型
  - 整型(Int32)
  - 长整型(Int64)
  - 单精度浮点型(Float)
  - 双精度浮点型(Double)
- 逻辑/布尔型
  - True
  - False
- 字符型
  - `Var: String("hello")`

## 参数(Input)
用户向程序输入的变量值，通过改变参数实现对整个程序的调整，参数值一般不能在运算中被更改，用户只能在程序运行之前进行参数设定。
```easylanguage
Input: Length(10), Con(False);
```


## 变量

## 数组
```eashlanguage
Array int nums[12](0)  // 大小为13， 初始值为0的一维数组 
```



## 运算

- 基本运算符:`+ - * /`
- 关系运算符
  - `> = < >= <= <>` (大于、等于 小于 大于等于 小于等于 不等于)
  - `Cross Over/Above`: 向上穿越
  - `Cross Below/Under`: 向下穿越
- 赋值运算符
  - `Condition=close=open`: 第一个`=`为赋值运算符，第二个`=`为等于号，该语句的含义是: 判断开盘价和收盘价是否相等，并将该结果的布尔值赋给变量`Condition`
  - `Condition=close>open And High>Close + Open`
- 运算符优先级: 小括号>乘除法>加减法>关系运算符>逻辑运算符

## Bar时间序列编程思想
## Bar属性保留字
每根K线都包含这些属性值，在编程过程中，可用回溯的方式调用任一根K线的属性值, 如`Value=Open[1]`或`Value=O[1]`，或`Value=Open of 1 Bar Ago`
- Data/D: 当前Bar最后Tick的日期
- Time/T: 当前Bar最后Tick的时间
- Open/O: 开盘价
- High/H: 最高价
- Low/L：最低价
- Close/C: 收盘价
- Volume/V: 当前Bar时间内成交量
- OpenInt/I: 当前Bar时间内持仓量

## 条件判断
```easylanguage
IF Condition Then
	xxx

IF Condition Then
	xxx
Else
	xxx

IF Condition Then
	xxx
End;

IF Condition Then Begin
	xxx
	xxx
End;

IF Condition Then Begin
	xxx
	xxx
End
Else Begin
	xxx
	xxx
End;
```


## 函数
- AverageFC: 移动平均值 (FC: Fast Calculation)
- Xaverage: 指数移动平均值，exponentially weighted average
- 

# 参考内容
- [EL 数学函数](http://blog.sina.com.cn/s/blog_6de2d5770100sd6z.html)
- [EL简写](https://wenku.baidu.com/view/a177c27ef8c75fbfc77db2f9.html)
