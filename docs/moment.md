---
layout: math
use_math: true
title: Moment
---

## 矩

- In physics, a moment is an expression involving the product of a distance and a physical quantity, and in this way it accounts for how the physical quantity is located or arranged.
  --[Moment(Physics)-wiki](https://en.wikipedia.org/wiki/Moment_(physics))
- In mathematics, a moment is a specific quantitative measure, used in both mechanics and statistics, of the shape of a set of points.
If the points represent mass, then the zeroth moment is the total mass, the first moment divided by the total mass is the center of mass, and the second moment is the rotational inertia.
If the points represent probability density, then the zeroth moment is the total probability (i.e. one), the first moment is the mean, the second central moment is the variance, 
the third moment is the skewness, and the fourth moment (with normalization and shift) is the kurtosis.
The mathematical concept is closely related to the concept of moment in physics.--[Moment(Mathematics)-wiki](https://en.wikipedia.org/wiki/Moment_(mathematics))

## Elaboration

- $\mu^n={\bf r}^n Q$, $Q$ is the physical quantity such as a force applied at a point, or a point charge, or a point mass, etc.
- If the quantity is not concentrated solely at a single point, the moment is the integral of that quantity's density over space
  - $\mu^n=\int {\bf r}^n \rho({\bf r}) d{\bf r}$
- $n$, 矩的阶数，当$n=0$时，矩和位置无关。此时
  - $Q$为质量时
    - 0阶矩为总质量
    - 1阶矩为质心
    - 2阶矩为转动惯量
  - $Q$为概率分布时
    - 0阶矩为总概率(即1)
	- 1阶矩为平均值
	- 2阶矩为方差
	- 3阶矩为歪斜
	- 4阶矩为尾巴胖瘦。

## 矩在数学/金融中的应用

- 随机变量的期望是其一阶原点矩
  - $E(x)=\int_{-\infty}^{\infty}$
- mean(期望)是随机变量的中心，那么，任何随机变量的一阶中心距都为0, 在求更高阶的矩时，利用更多的是中心距而不是原点矩。
- variance(方差)是随机变量的二阶中心距
  - $\mathrm{var}(x)=\int_{-\infty}^{\infty}[x-E(x)]^2f(x)dx$
- skewness(偏态)是随机变量的三阶中心距
  - $\mathrm{S}(x)=\int_{-\infty}^{\infty}[x-E(x)]^3f(x)dx$
  - 任何对称分布偏态为0
- kurtosis(峰度)定义为随机变量的四阶中心距与方差平方的比值
  - $\mathrm{K}(x)=\frac{\int_{-\infty}^{\infty}[x-E(x)]^3f(x)dx}{\sigma^2}$
  - 3是正态分布的峰度。
  - $K(x)$减去正态分布的峰度3，得到超值峰度。
  - 峰度表示波峰和尾部与正态分布的区别(金融中的肥尾效应)

## 混合矩

- 混合矩是多个变量的矩
- 协方差只有一个
- 协偏度和协峰度不止一个

## 样本矩

- 不需要先估计其概率分布
- $\hat{\mu}_n\sim\frac{1}{n}\sum\limits_{i=1}^{N}x_i^n$

## References
- [Moment(Mathematics)-wiki](https://en.wikipedia.org/wiki/Moment_(mathematics))
- [Moment(Physics)-wiki](https://en.wikipedia.org/wiki/Moment_(physics))
