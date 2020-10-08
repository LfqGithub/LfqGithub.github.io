---
layout: quant
title: Strategy
categories: [quant, strategy]
description: frequently-used strategies
use_math: true
keywords: 
---

# Strategy
## MACD
Moving Average Convergence and Divergence，异同移动平均线，由双指数移动平均线发展而来，
## KDJ
## RSI
## 分时九转


# Strategy Evaluation

## 年化收益率

- Annualized Returns
- $p_r=(\frac{p_{\rm end}}{p_{\rm start}})^{250/n}-1$
  - $p_{\rm end}$: 策略最终总资产
  - $p_{\rm start}$: 策略初始总资产
  - $n$: 回测交易日数量

## 基准年化收益率

- Benchmark Returns
- $B_r=(\frac{B_{\rm end}}{B_{\rm start}})^{250/n}-1$
  - $B_{\rm end}$: 基准最终总资产
  - $B_{\rm start}$: 基准初始总资产
  - $n$: 回测交易日数量

## Alpha

- 投资中面临的非系统性风险
- 投资者获得的和市场波动无关的回报
- $\alpha=p_r-r_f-\beta(B_r-r_f)$
  - $p_r$: 策略年化收益率
  - $r_f$: 无风险收益率
  - $B_r$: 基准年化收益率

## Beta

- 投资中面临的系统性风险
- 反映了策略对大盘变化的敏感性
- 一个策略的$\beta$为1.3，则大盘涨1%时，策略可能张1.3%。反之亦然
- $\beta=\frac{\textrm{Cov}(p_n,B_n)}{\sigma^2_m}$
  - $p_n$: 策略每日收益率
  - $B_n$: 基准每日收益率
  - $\sigma^2_m$: 基准每日收益方差
  - $\textrm{Cov}(p_n,B_n)$: 策略每日收益率和基准每日收益率的协方差
