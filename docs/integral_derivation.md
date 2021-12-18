---
layout: math
use_math: true
title: Integral/Derivation
keywords: math, integral, 积分
---

Updating...

# Integral

## 常用积分公式

- $I=\int_0^{\infty} x e^x dx$ 

## 积分运算
积分运算可分为三类
- 加
- 乘法法则 (Product Rule)

<div align="center"><img width="600" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/product-rule.png"/></div>

- 链式法则 (Chain Rule)

<div align="center"><img width="600" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/chain-rule.png"/></div>


# Derivation

## Implicit Function

- $$x^2+y^2=\mathrm{C}$$： $$d(x^2)+d(y^2)=0$$

隐函数求导的思路：

<div align="center"><img width="600" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/implicit_function_derivate.png"/></div>

以$y=\ln(x)$为例，我们知道$de^x=e^xdx$, 因此我们将$y=\ln (x)$变换为$e^y=x$, 对左右两边求导，得出

$$\begin{aligned}
& de^y=dx \\
\leftrightarrow & e^ydy=dx \\
\leftrightarrow & \frac{dy}{dx}=\frac{1}{e^y} \\
\leftrightarrow & \frac{dy}{dx}=\frac{1}{x} 
\end{aligned}$$

从而证明$y=\ln(x)$的导数为$\frac{1}{x}$。

# Other

## 洛必达法则

<div align="center"><img width="600" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/洛必达法则.png"/></div>

## 变上限积分函数

- [ ] [变上限积分函数的求导](http://www.saikr.com/a/2774)

# Refs

- [3B1B--微积分的本质](https://www.bilibili.com/video/av10308208)
