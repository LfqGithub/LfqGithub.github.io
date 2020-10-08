---
layout: quant
title: Indicators
categories: [quant, stock]
use_math: true
description: Indicators
keywords: indicator, quant, finance
---

Indicators in trading, updating......

# Indicators
### MA
Moving Average, 移动平均线，MAn 表示包括今天在内的前 n 天的收盘价的平均值
根据时间长短，可以定义短期(一般5日或10日)移动平均线、中期(一般30日或60日)移动平均线和长期(一般100天或200天)移动平均线。
### SMA
Simple Moving Average, 即上述的MA， 每一时限的值权重相同，即简单的算术平均
### WMA
Weighted Moving Average, 加权移动平均线，比重以平均线的长度设定，越近期的收盘价，对未来的市场影响越大。计算时每个时期的价格乘以不同的比重，越近期的值比重越大，之前的值所占比重随相隔时间递增。
#### 线性加权移动平均线
MA n=$$\sum_0^nC_n*n/\sum n$$
#### 梯形移动加权平均线
MA n=$$\sum_0^nC_n*n/\sum n$$

### MACD
Moving Average Convergence/Divergence, 异同移动平均线

### EMA

Exponential Moving Average，指数移动平均值，又称 EXPMA 指标，趋向类指标，指数式递减加权的移动平均
$$\textrm{EMA}_n=\alpha\cdot price_n+(1-\alpha)\cdot\textrm{EMA}_{n+1}$$，其中
- $\alpha$: 平滑指数，N天指数移动平均线的平滑指数一般取$2/(N+1)$
- $\textrm{EMA}_1$ 没有定义，有多种定义方法，一般取 EMA1为 $\textrm{price}_1$,也可以取前 4~5 个 price 的平均值
