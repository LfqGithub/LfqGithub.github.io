---
layout: quant
title: Quant Basic
categories: [math, finance]
description: equation/math in finace
use_math: true
keywords: math, finace, equation
---

Updating...

# Technical Terms 


## ETF

Exchange Traded Funds, 交易所交易基金，交易所买卖基金

## PB

- Price/Book Value, 市净率, 又称P/B
- 股票市价/每股净资产 
- 越低，投资价值越高

## EPS

- Earnings Per Share, 每股收益
- 利润/总股数
- 本年净收入与普通股份总数的比值

## ROE

- Return on Equity
- 股本回报率
- 净资产收益率
- 报告期净利润/报告期净资产
- 指标越高，投资带来的收益率越高

## 滑点

- 下单的点位和最后成交的点位有差距

## hurst

## alpha

## beta

## PE

- Price-to-Earning Ratio, 又称PER, P/E, 默认情况下指静态市盈率, 股价/每股收益
- PE(LYR)
  - 静态市盈率，Last Year Ratio, 当前总市值/上一年总净利润
- PE(TTM)
  - Trailing Twelve Months
  - 市盈率TTM，又称动态市盈率/滚动市盈率 
  - 市盈率在一定考察期内（一般为12月），普通股每股市场价格/普通股每股盈利, 同花顺软件中，动态市盈率=股价/（最新报表EPS\*（1/报表截止日占全面比例））
- 预测市盈率
  - 根据季报数据折算的年每股收益

## EBIT

- Earnings Before Interest and Tax, 息税前利润
- 不扣除利息、所得税之前的利润

## 收益率

投资人投入本金$C$到市场，经过时间$T$后其市值变成$V$，则该次投资中
- 收益： $P=V-C$
- 收益率： $K=P/C=V/C-1$
- 年化收益率为：
  - $Y=(1+K)^N-1=(1+K)^{D/T}-1$
  - $Y=(V/C)^N-1=(V/C)^{D/T}-1$
  - 其中$N=D/T$表示投资人一年内重复投资的次数， $D$表示一年的有效投资时间
    - 银行存款、票据、债卷等，$D=360$
	- 股票、期货等，$D=250$
	- 房地产，实业等， $D=365$

### 年化收益率

投资期限为一年所获取的收益率, 货币基金常用参数
- 万份收益
- 7日年化收益率
  - 指年化收益率货币基金过去七天每万份基金份额净收益折合成的年收益率
    - 日日分红，按月结转, 相当于日日单利，月月复利
	  - 计算公式：$\sum (R_i/7)*365/10000{\rm x}100\%$
	- 日日分红, 按日结转，相当于日日复利
	  - 计算公式：$\prod (1+R_i/10000)^{365/7}{\rm x}100\%$
	- 其中$R_i(i=1,2...7)$为最近第$i$公历日的每万分收益

## 年化风险

## 无风险短期利率

## 夏普率

- Sharpe ratio
- （预期收益率-无风险利率）/投资组合标准差
- 报酬与波动性比率
- 最常用的投资组合管理度量标准
- 本身没有意义，只有与其他组合比较才有价值

## K线图
  - 包含信息
	- 开盘价
    - 收盘价
	- 最高价
	- 最低价

# Index

- U.S. Dollar Index : USDX，衡量美元在国际外汇市场变化的一项综合指标，由美元对六个主要国际货币（欧元Euro/EUR、日元Yen/JPY、英镑Pound/GBR、加拿大元Canadian Dollar/CAD、瑞典克朗Krona/SEK和瑞士法郎Franc/CHF）的汇率经过加权平均计算获得。
  - 

## 金叉/死叉

- 股票行情指标的短期线向上/下穿越长期线的交叉成为金/死叉

# Data Processing

## Data Standardization

- Min-max
  - $V=\frac{v-min}{max-min}$
  - 将数据值统一到0~1
- z-score
  - $Z=\frac{v-\mu}{\sigma}$
  - 将数据的数值分布均值变成0， 方差变为1

## 回归分析

确定两种或者两种以上变量之间相互依赖的定量关系的一种统计分析方法。

### 分类

- 涉及变量数量
  - 一元回归分析
  - 多元回归分析
- 因变量数目
  - 简单回归分析
  - 多重回归分析
- 自变量和因变量的关系类型
  - 线性回归分析
  - 非线性回归分析

### 方法

- OLS
  - ordinary least square， 普通最小二乘法
  - 应用最多的参数估计方法

# 图表

## 箱型图
- boxplot, 又称盒须图、盒式图、盒状图或者箱线图
- 显示一组数据分散情资料的统计图
- 显示一组数据的最大值、最小值、中位数、上下四分位数

# Trading 

- 浮动盈亏: 又称持仓盈亏，持仓合约的初始成交价与当日结算价计算的潜在盈亏
  - 浮动盈亏=(当天结算价-开仓价格)\*持仓量\*合约单位
- 持仓成本：同一时期内连续分批（买入，卖出）交易某金融产品或衍生品后的交易总成本减去浮动盈亏的数额除以现有持有数量

# Others

## 国内四大期货交易所
- 中国金融期货交易所(CFFEX)
- 大连商品交易所(DCE)
- 郑州商品交易所(ZCE)
- 上海期货交易所(SHFE)

## 证券交易所代码

- SHA: 上海证券交易所
- SHE: 深圳证券交易所
- HKG: 香港交易所
- NYSE：纽约交易所
- NASDAQ: 纳斯达克交易所

- [ ] 哑变量


## Refs
- [What is US Dollar Index?](https://www.babypips.com/learn/forex/what-is-the-dollar-index)
- [boxplot](http://wiki.mbalib.com/wiki/%E7%AE%B1%E7%BA%BF%E5%9B%BE)
- [期货交易名词与术语](http://www.guodu.cc/05/03/370.html)
- [期货交易术语](http://wiki.mbalib.com/wiki/%E6%9C%9F%E8%B4%A7%E4%BA%A4%E6%98%93%E6%9C%AF%E8%AF%AD)
- [国内期货品种及其代码](https://quizlet.com/13706624/flash-cards/)
- [K线图-百度文库](https://jingyan.baidu.com/article/15622f2476271efdfcbea583.html)
- [上海期货交易所交易规则](http://www.shfe.com.cn/regulation/regulation/regulation/)
