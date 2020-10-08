---
layout: math
use_math: true
title: Mathematical Statistics
---

Updating......

# 概念
- IDD 样本: 总体分布为 $F$, $X_1,X_2,..., X_n$为独立同分布的样本时,我们常称$X_1,X_2,..., X_n$为总体$F$中抽出的简单随机样本或独立同分布 (**IDD**, independent identically distributed) 的样本, 记为

$$X_1,X_2,...,X_n\stackrel{IDD}{\sim}F(x)$$

也可以记为

$$X_1,X_2,...,X_n\stackrel{IDD}{\sim}f(x)$$

其中$f(x)$ 为分布 $F(x)$ 的概率密度函数.

- 样本分布族
- 参数空间
- 统计量
- 样本均值
- 样本方差
- 样本相关系数 sample correlation coefficient
- 离均差平方和ss: Sum of square of deviation from mean, $SS=\sum(x_i-\overline{x})^2$

$$r(X,Y)=\frac{\sum\limits_{i=1}^n(X_i-\overline{X})(Y_i-\overline{Y})}{\sqrt{\sum\limits_{i=1}^n(X_i-\overline{X})^2\sum\limits_{i=1}^n(Y_i-\overline{Y})^2}}$$

称为$X,Y$的样本相关系数
- 次序统计量 order statistic: 对于样本$X_1,X_2,...,X_n$, 将其由小到大排列为$x_{(1)},x_{(2)},...,x_{(n)}$, 新的排布称为次序统计量, $X_{(i)}$称为第 $i$ 个次序统计量.
- 样本p分位数 quantile: 对于给定的 $p\in (0,1)$, 我们称



$$m_{n,p}=X_{([np])}+(n+1)(p-\frac{[np]}{n+1})(X_{([np]+1)}-X_{([np])})$$


为样本的 $p$ 分位数. 其中 $\left[x\right]$表示不超过 $x$的最大整数. 特别地,样本中位数 (median) 定义为

$$X_{med}=
\begin{cases}
X_{((n+1)/2)} & \textrm{n is odd} \\
\frac{X_{(n/2)}+X_{(n/2+1)}}{2} & \textrm{n is even}
\end{cases}
$$

- 极值统计量: $X_{(l)}$,$X_{(m)}$ 为极小值与极大值统计量
- 极差: $X_{(m)}-X_{(l)}$
- 变异系数 coefficient of variation: $S_n/\overline{X}$
- 样本偏度和峰度
- 经验分布函数
- [ ] 中心极限定理--样本期望分布为正态分布--证明
- 累积分布函数 CDF: cumulative distribution function
- 概率密度函数 PDF: probability distribution function
- 极大似然概率 MLE(Maximum Likeihood Estimate) 
- 无偏估计 UE(unbiased estimate)
- 一致最小方差无偏估计 UMVUE(uniformly minimum variance unbiased estimate)
- 点估计 point estimation
- 区间估计 interval estimation
- 下确界 Infimum: $\leq$ 集合中所有元素的值
- 上确界 supremum: $\geq$ 集合中所有元素的值
- [ ] 联合概率分布






# 参数估计

- 总体： 总体是一个概率分布，当总体分布为指数分布时，称为指数分布总体。
- 样本: 按照一定的规定从总体中抽出的一部分个体。
- 统计量: 完全由样本决定的量，称为统计量
- 变异系数：有些问题中，虽然$\mu$未知，但可以知道$\mu >0$, 则$\sigma /\mu $成为总体的变异系数. 变异系数以均值为单位去估计总体的标准差, 该系数为一定意义上的“相对误差”。
- 样本方差: 使用时要注意其和二阶中心矩, 及整体方差的区别
- 整体方差

> 总体样本量和抽样方式：设想样本是一个一个抽出来的，第一次 ($X_1$) 抽是从整体中抽一个，$X_1$ 和整体分布相同。如果抽第一次后不放回，则第二次抽时已经少了一个个体，整体分布产生了变化。
因此 $X_2$ 的分布相对 $X_1$ 已经发生了变化。但当总体中包含的个数极多时，抽样导致的变化极小，可以忽略不计。

当总体中所含样本不大时，情况就不同。
举例来说，当 N 件产品中有 n 个次品，抽取 K 次， 抽中 k 个次品的概率，放回抽样的概率为二项分布

$${K \choose k}p^k(1-p)^{K-k}$$

其中$p=n/N$。

如果用不放回抽样 (without replacement), 则概率为超几何分布

$${K \choose k}{N-K \choose n-k}/{N \choose K}$$

## 点估计
- [ ] 概念

### 矩估计

设总体分布为$f(x; \theta_1,\theta_2,..., \theta_k)$， 则其(原点)矩为

$$\alpha_m=\int_{-\infty}^{\infty}x^mf(x,\theta_1,\theta_2,..., \theta_k) dx$$

或

$$\alpha_m=\sum\limits_{i}x_i^mf(x_i,\theta_1,\theta_2,..., \theta_k)$$

该矩依赖于$\theta_1, \theta_2, ..., \theta_k$。当样本量较大时，$\alpha_m$应接近于样本原点矩$\alpha_m$, 因此

$$\alpha_m=\alpha_m(\theta_1, \theta_2,..., \theta_k)\approx a_m=\sum_limits_{i=1}^{n}X_i^m/n$$

取 $m=1,2,...,k$, 将近似符号改为等号，可得方程组

$$\alpha_m(\theta_1, \theta_2,...,\theta_k)=a_m (m=1,2,...,k)$$

解此方程组，可得其根

$$\overline{\theta_i}=\hat{\theta_i}(X_1,X_2,...,X_k)$$

其中$i=1,2,...,k$。将$\overline{\theta_i}$作为$\theta_i$的估计。 如果需要估计的为$\theta_1,\theta_2,...,\theta_k$的函数，则用

$$\overline{g}(X_1,X_2,...,X_k)=g(\hat{\theta_1},\hat{\theta_2},...,\hat{\theta_k})$$估计。


>一般原则为能用低阶矩估计的就不用高阶矩: 以泊松分布$P(\lambda)$为例，$\lambda$为均值，同时也为方差，用矩估计法，可用一阶矩，也可用二阶矩估计。但是通常使用低阶矩来估计。

### 极大似然估计


**似然函数** (Likelihood Function)：对于分布族$$\left\{f(x,\theta), \theta\in\Theta\right\}$$, 以$f(\textrm{x},\theta)$记作其$n$个样本的联合概率分布，对于给定的样本观测值$\textrm{x}=(x_1,x_2,...,x_n)$， 我们称$f(\textrm{x}),\theta)$
为参数$\theta$的似然函数。简称似然函数。记为

$$L(\theta, \textrm{x})=f(\textrm{x}, \theta), \forall\theta\in\Theta$$

称$\ln L(\theta, \textrm{x})$为对数似然函数，记为$l(\theta, \textrm{x})$或$l(\theta)$。(b2, p49)

>>从上式可看出，似然函数和样本联合概率分布相同，二者含义确不同：样本联合概率分布函数为参数值$\theta$下样本$\textrm{x}$的函数，取值空间为样本空间$\mathcal{X}$， 而似然函数则是固定样本观测值$\textrm{x}$下关于参数$\theta$的函数，其在参数空间$\Theta$上取值。如果把参数$\theta$视为**原因**，把样本看作**结果**, 给定参数后，样本联合分布告诉我们的是样本会以多大概率被观测到；似然函数告诉我们，观察到样本后，如何最可能的取参数$\theta$的估计。

**极大似然概率MLE**: 设$X_1,X_2,...,X_n$是来自概率分布

$$f(x,\theta)\in \mathcal{F}=\left\{f(x,\theta): \theta\in\Theta\subseteq\mathbb{R}^k\right\}$$

的一组样本，如果统计量$\overline{\theta}(\textrm{X})$ 满足

$$L\left(\overline{\theta}(x),x\right)=\mathop{\text{sup}}\limits_{\theta\in\Theta}L(\theta,x)$$

或等价地满足

$$l\left(\overline{\theta}(x),x\right)=\mathop{\text{sup}}\limits_{\theta\in\Theta}l(\theta,x)$$

则称$\overline{\theta}$为$\theta$的极大似然概率MLE。

>> 从上述定义可以看出，求某参数的极大似然概率, 就是求上述两式之一的极值。如果似然函数$L(\theta, \textrm{x})$关于$\theta$可微， 则$\theta$的极大似然概率可通过解下面方程求得
$\frac{\partial L(\theta,\textrm{x})}{\partial{\theta}_j}=0, j=1,2,...,k$, 或等价地有 $\frac{\partial l(\theta,\textrm{x})}{\partial{\theta}_j}=0, j=1,2,...,k$。 在统计上，我们称上述两方程为似然方程。

- [ ] 极大似然估计一般来说更为优良，但是在个别情况下也有可能给出不理想的结果。
- [ ] SCFT 解法，是否为最大似然估计？

### 贝叶斯估计

### 优良性准则

考虑估计量的优劣时，必须从整体性能去衡量，而不能看他在个别样本下表现如何。整体性能包含两种意义：估计量的某种特性，具有这种特性就是好的，否则就不好。如**无偏性**; 二是指某种具体的数量性指标，两个指标量，指标小者为优，如**均方误差**。

- [ ] 无偏估计
- [ ] 最小方差无偏估计
- [ ] 相合性
- [ ] 渐近正态性

## 区间估计

点估计是用一个点估计未知参数，**区间估计 (Interval Estimate)**是用一个区间去估计未知参数，即把未知参数值估计在一个区间之内。如一个人年龄在30$\sim$35岁之间。\\
区间估计是一种常用的估计形式，其优势在于把可能的误差直接标注出来。估计费用在800$\sim$1200之间，人们会相信在做估计时，将可能的误差考虑进去了，会给人更大的信任感。

区间估计定义1(b1): 设 $X_1,X_2,...,X_n$ 是从总体中抽出的样本，$\theta$ 的区间估计，是指满足条件 

$$\overline{\theta_1}(X_1,X_2,...,X_n) \leq \hat{\theta_2}(X_1,X_2,...,X_n)$$

的两个统计量$\overline{\theta_1}, \hat{\theta_2}$ 为端点的区间
$\left[\overline{\theta_1},\hat{\theta_2}\right]$。对于样本 $X_1,X_2,...,X_n$，将$\theta$估计在区间$\left[\hat{\theta_1}(X_1,X_2,...,X_n),\hat{\theta_2}(X_1,X_2,...,X_n)\right]$之内。这里有两个要求

- $\theta$ 落在区间内概率要较大(可靠度高)
- 区间要尽可能小(精准度高)

这是两个相对矛盾的要求。在决策时，一般先保证可靠度，在此前提下提高精准度。

区间估计定义2(b2,p112): 设$X_1,X_2,...,X_n$为来自参数分布族$$\mathcal{F}=\left\{f(x,\theta):\theta\in\Theta\right\}$$的样本，$\theta$为一维未知参数，如果$\overline{\theta}_L(\textrm{X})$,$\hat{\theta}_U(\textrm{X})$为两个统计量，且$$\hat{\theta}_U(\textrm{X})<\hat{\theta}_U(\textrm{X})$$, 则称随机区间$\left[\hat{\theta}_L(\textrm{X}),\hat{\theta}_U(\textrm{X})\right]$为$\theta$的一个区间估计。

>>从上述定义可以看出，给出一个区间估计很容易，但是如何衡量估计的好坏？当参数真值为$\theta$时，我们希望随机区间$\left[\overline{\theta}_L(\bf{X}), \hat{\theta}_U(\bf{X})\right]$包含$\theta$的概率$P_{\theta}\left\{\hat{\theta}_L(\bf{X})\leq\theta\leq\hat{\theta}_U(\bf{X})\right\}$越大越好。这个概率称为**置信水平 (Confidence Level)**, 或**置信度**。由于置信水平依赖于参数真值，我们希望对于参数空间$\Theta$中每一个$\theta$， 其置信水平都很大。

**置信系数**: 设随机区间$\left[\overline{\theta}_L(\bf{X}), \hat{\theta}_U(\bf{X})\right]$ 为$\theta$的一个区间估计，则

$$\mathop{\text{inf}}\limits_{\theta\in\Theta}P_{\theta}\left\{\overline{\theta}_L(\bf{X})\leq\theta\leq\hat{\theta}_U(\bf{X})\right\}$$

为该区间估计的置信系数。



## 枢轴变量法 

区间估计理论和方法的基本问题：在已有样本资源限制下，如何找到更好的估计方法，尽量提高可靠度和精度。
如二者无法兼得，则一般原则为先保证可靠度，再次前提下尽量使精度提高。为此引进置信系数的概念。

**置信系数**：给定一个很小的数 $\alpha > 0$, 如果对参数 $\theta$ 的任何值，概率

$$P_\theta(\overline{\theta}(X_1,X_2,...,X_n)\leq\theta\leq\hat{\theta}(X_i,X_{i+1}...,X_n))$$

上式概率都等于$1-\alpha$, 则乘区间估计$\[\overline{\theta_1}, \hat{\theta_2}\]$的置信系数为$1-\alpha$。

有时无法确定对一切$\theta$都恰好等于$1-\alpha$, 但是知道其不会小于$1-\alpha$, 则我们称之为**置信水平**。

**上分位点**: 
**下分位点**: 











# 假设检验

## 概念

- 假设：统计中，我们将需要根据样本去推断其正确与否的命题，成为一个假设或者统计假设。
- 检验：通过样本对一个假设做出对与不对的具体判断规则，成为该假设的一个检验。
- 简单假设/复合假设：不管是原假设还是对立假设，若其中只含有一个参数值，则成为简单建假设，否则成为复合假设, 又称复杂假设。
- 拒绝域/接受域：当有了具体的样本后，由假设检验法则或策略就可以决定是接受$H_0$或者拒绝$H_0$, 即检验就相当于将样本空间$\chi$划分成两个互不相交的部分$W$和$\overline{W}$，当样本属于$\hat{W}$时，接受$H_0$, 否则拒绝。我们称$W$为该检验的拒绝域，$\overline{W}$为接受域。
- 一类/二类错误：拒真/纳伪的错误，分别成为一/二类错误。
  - 犯第一类错误的概率：$\alpha=P_\theta\{X\in W\}, \theta\in\Theta_0$, 也记为$P\{X\in W\vert H_0\}$
  - 犯第二类错误的概率：$\alpha=P_\theta\{X\in \overline{W}\}, \theta\in\Theta_1$, 也记为$P\{X\in \hat{W}\vert H_1\}$
- 势函数: 对于假设的一个假设方法$\psi$, 其拒绝域记为$W$, 则称 

$$\beta_{\psi}(\theta)=P_{\theta} \{X\in W\}, \forall \theta \in \Theta$$

为该函数的势函数。





参数假设检验基本包括显著性检验(significance test)和最大功效检验(most powerful test)两部分.

## 假设检验--显著性检验

显著性水平(significance level)$\alpha$: 越小，获得显著性结果越难，越难拒绝零假设H.


# 方差分析
- [ ] 介绍，基本公式
- [ ] F分布


# Todo

- [ ] [为什么样本方差的分母为n-1](https://www.zhihu.com/question/20099757)--自己推导
  - 即二阶中心距和样本方差 $S^2$ 只差一个常数因子
  - $$m_2=\frac{n-1}{n}S^2$$


# Ref
- [标准正态分布表](https://www.shuxuele.com/data/standard-normal-distribution-table.html)
- b1: 陈希孺，数理统计与概率论, 中国科学技术大学出版社
- b2: 王兆军, 邹长亮, 数理统计教程,高等教育出版社
