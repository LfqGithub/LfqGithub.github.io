---
layout: math
use_math: true
title: Probability Theory
---

Updating......

# 概念

## 概率分布函数

设$X$为一随机变量，则函数

$$P(X\leq x)=F(x) (-\infty \leq x \leq \infty)$$

为$X$的概率分布函数(b1, p42)。

## 概率密度函数

设连续型随机变量$X$有概率分布函数$F(x)$, 则$F(x)$的导数

$$f(x)=F^{'}(x)$$

为$X$的概率密度函数(b1,p48)。

## 矩

统计学上的矩和物理学上的矩, 都是数学上矩的特例。英文都是 Moment.
The n-th moment of a real-valued continuous function $f(x)$ of a real variable about a value $c$ is [source](https://en.wikipedia.org/wiki/Moment_(mathematics))

$$\mu_n=\int_{-\infty}^{\infty}(x-c)^nf(x)$$

如果$f(x)$是分布函数，上式就是统计矩。
如果$f(x)$是力的分布，n=1, 上式就是力矩。
如果$f(x)$是质量分布，n=2, 上式就是转动惯量。
其他物理上的 moment 还有磁矩(电流的矩), 角动量(动量的矩), 电偶极矩(电荷的矩)。

## MGF

[Moment Generating Function](https://zh.wikipedia.org/wiki/%E7%9F%A9%E7%94%9F%E6%88%90%E5%87%BD%E6%95%B8), 矩生成函数

## 伯努利实验

只有两种可能结果(成功或者失败)的单次随机实验。即对于一个变量$X$而言 

$$ P =
\begin{cases}
p & (X=1) \\
1-p & (X=0)
\end{cases}$$ 


# 概率运算

## 事件关系

- 独立事件: 两事件 A, B 如果满足$P(AB)=P(A)P(B)$, 则称A,B事件相互独立: $A(B)$发生与否对$B(A)$无影响。

- 互斥事件: 两事件 A, B 不能在一次事件中同时发生(可以同时不发生), 则称他们是互斥的。

- 对立事件: 事件 A 的对立事件 B={A不发生}, 记为 $\overline{A}$,读作 A bar。也记作$A^c$。

- 和: $C=A+B$, 含义为只要A发生，或B发生，以及AB同时发生，都算C发生。

- 积: $C=AB$, 含义为AB同时发生,则算作C发生。

- 差: $C=A-B=A+\overline{B}$

## 乘法定理

- 若$P(A)>0$,则$P(AB)=P(B\|A)P(A)$
- 可推广到$P(AB)>0$,则$P(ABC)=P(C\|AB)P(B\|A)P(A)$

## 加法定理
互斥时间之和的概率(互斥事件同时发生)等于互斥事件概率之和

## 条件概率
两事件A,B, 其中$P(B)\neq 0$， 则$P(A|B)=P(AB)/P(B)$, 其中$P(A|B)$为B已经发生的前提下，A事件发生的概率。

## 全概率公式

设$B_1$, $B_2$, ...... $B_n$为有限或者无限个事件，两两互斥且在每次实验中至少发生一次。即

$$B_iB_j=\emptyset$$

$$B_1+B_2+...=\Omega$$

其中$\Omega$符号代表必然事件。
具备这两个性质的一组事件称为**完备事件群**。从这个概念我们可以得到：任何一个时间和其对立事件可以组成一个完备事件群。

针对任一事件A和一个完备事件群$\Omega$, 我们可以得出$A=A\Omega=AB_1+AB_2+...+AB_n$, 因为$B_1,B_2,...,B_n$两两互斥，我们可以得出$AB_1,AB_2,...,AB_n$两两也互斥, 根据加法定理, 有

$$P(A)=P(AB_1)+P(AB_2)+...P(AB_n)$$。

由条件概率的定义可得

$$P(AB_n)=P(B_n)P({A}\vert{B_n})$$

因此A的概率可以写成

$$P(A)=P(B_1)P({A}\vert{B_1})+P(B_2)P({A}\vert{B_2})+...P(B_n)P({A}\vert{B_n})$$

此公式被称为**全概率公式**。

- 全概率公式名称由来: 一个时间A的全部概率被分解成了多个部分之和
- 全概率公式的理论和实用意义：较复杂情况下直接算$P(A)$不易，单A总是随着某个$B_i$一起发生。适当去构造这一组$B_i$, 可简化计算
- 全概率公式的另一个理解角度：将$B_i$看作导致事件A发生的一种可能路径，对不同路径，A发生的概率即条件概率$P({A}\vert{B_i})$, 而采取哪个路径确是随机的

## 贝叶斯公式

在全概率公式的假定之下，有

$$P({B_i}\vert{A})=P(B_iA)/(P(A))=P(B_i)P({A}\vert{B_i})/\sum\limits_jP(B_j)P({A}\vert{B_j})$$

此公式为贝叶斯公式。

>>此公式之所以著名，在于其现实乃至哲理意义的解释上。$P(B_1),P(B_2),...,P(B_n)$是在没有进一步信息(不知道事件A是否发生)的前提下，人们对事件$B_1,B_2,...,B_n$发生可能性大小的认识。现在有了新的信息(A的发生),
人们对$B_1,B_2,...,B_n$发生的可能性大小有了新的认识。这种思维路径，在生活中经常见到：原以为不甚可能的一种情况，可能因为某种事件的发生而变得甚为可能(如刑事案件中推断嫌疑人)。

- [ ] We are restricting our view only to the possibilities where the evidence holds.


# 概率分布

## 均匀分布

[Uniform Distribution](https://zh.wikipedia.org/wiki/%E9%80%A3%E7%BA%8C%E5%9E%8B%E5%9D%87%E5%8B%BB%E5%88%86%E5%B8%83), 其概率密度函数为

$$f(x)=
\begin{cases}
\frac{1}{b-a} & (a\leq x \leq b) \\
0 & elsewhere
\end{cases}$$

<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/uniform_distribution.png"/></div>


## 二项分布
Bionomial Distribution, 
计作$b(x,n,p)$, 或$X\sim B(n,p)$
二项分布的概率函数为

$$b(x,n,p)={n \choose x}p^xq^{n-x}$$， 其中$x=0,1,2,......,n$为正整数。

<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/binormal_distribution.png"/></div>

## 几何分布

[Geometric Distribution](https://zh.wikipedia.org/wiki/%E5%B9%BE%E4%BD%95%E5%88%86%E4%BD%88)

$$P(X)=p(1-p)^x$$

因概率 $p, p(1-p), p(1-p)^2, ...$呈公比为$(1-p)$的几何级数，因此这种分布为几何分布。

<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/geometric_distribution.png"/></div>


## 泊松分布

[Possion Distribution](https://zh.wikipedia.org/wiki/%E6%B3%8A%E6%9D%BE%E5%88%86%E4%BD%88)

随机变量X的可能取值为0,1,2,..., 且概率分布为$$P(X=i)=e^{-\lambda}\lambda^i/i!$$, 称为泊松分布, 计作$X\sim P(\lambda)$。
对上式中公式右边进行求和，结果为1. 可以通过一个常用的公式
$$e^{\lambda}=\sum\limits_{i=0}^{\infty}\lambda^i/i!$$求出。

>>证明方法见证明1


- [ ] $$e^{\lambda}=\sum\limits_{i=0}^{\infty}\lambda^i/i!$$
- [ ] $$\lim_{n\to\infty} {n \choose i}/n^i=1/i!$$
- [ ] $$\lim_{n\to\infty}(1-\lambda/n)^n=e^{-\lambda}$$

<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/possion_distribution.png"/></div>

## 超几何分布

- [ ] 超几何分布

## 正态分布

随机变量 $X$ 具有概率密度函数

$$f(x)=(\sqrt{2\pi}\sigma)^{-1}e^{-\frac{(x-\mu)^2}{2{\sigma}^2}}$$

其中$(-\infty < x < \infty)$, 则称$X$为正态随机变量。记为$X\sim N(\mu, \sigma^2)$， 这里 $N$ 为Normal一词的首字母。

- [ ] 证明过程
- [ ] 细节理解过程

<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/normal_distribution.png"/></div>

## 指数分布

$$f(x)=\begin{cases}\lambda e^{-\lambda x} & (x>0) \\
0 & (x\leq 0)
\end{cases}
$$

其中$\lambda>0$为指数分布的一个参数，常被成为**率参数**，即每单位事件内发生的次数。
指数分布还可以写成

$$X\sim\mathrm{Exponential(\lambda)}$$

**指数分布的累积分布函数**为

$$F(x)=\begin{cases}1-  e^{-\lambda x} & (x>0) \\
0 & (x\leq 0)
\end{cases}
$$


**指数分布的期望**可通过分部积分求得

$$
\begin{aligned}
E&=\int_{0}^{x\rightarrow\infty} x f(x)dx=\int_{0}^{\infty} x\lambda e^{-\lambda x}dx \\
&=1/\lambda
\end{aligned}
$$


- [ ] 证明过程
- [ ] 细节理解过程

常用场合：寿命分布

## 威布尔分布
老化应该随时间而上升，因此应去一个时间 t 的增函数，如$\lambda x^m (\lambda >0, m>0)$,这个条件下，寿命分布满足微分方程

$$F'(x)/[1-F(x)]=\lambda x^m$$

与初始条件 $F(0)=0$ 结合，得出

$$F(x)=1-e^{-\lambda}$$

-  [ ] 完善


## 多项分布

与一维随机变量对应的为**多维随机变量**, 又称**多维随机向量**。和一维随机变量相同，多维随机变量也有离散型和连续型区别。

设$A_1, A_2,..., A_n$是某一实验下的完备事件群，即事件$A_1, A_2,..., A_n$两两互斥，其和为必然事件，分别以$p_1,p_2,...,p_n$记事件$A_1, A_2,...,A_n$的概率，则$P_i\geq 0, \sum p_i=1$。
将实验重复$N$次，以$X_i$记$N$次事件中$A_i$发生的次数($i=1,2,3,...,n$)。则$X=(X_1,X_2,...,X_n)$为一个n维随机向量，取值范围为非负整数。其和为N。
$X$的分布即为多项分布。记为$M(N,p_1,p_2,...,p_n)$。多项分布 ([Multinominal distribution](https://en.wikipedia.org/wiki/Multinomial_distributioni)) 为最重要的离散型多维分布。

计算事件

$$B=\{X_1=k_1, X_2=k_2, ..., X_n=k_n\}$$

的概率， 这里包含前提条件$k_i\geq 0$ 且$\sum k_i=N$, 否则$P(B)=0$。

要使得事件$B$发生，需要$A_1$发生$k_1$次, $A_2$发生$k_2$次, $A_n$发生$k_n$次。
此过程相当于在$N$个不相同的物体分成$n$堆，各堆分别有$k_1,k_2,...,k_n$的分法种类数。我们可以推断出分法有$N!/(k_1!k_2!...k_n!)$种。
由于每次试验都是相互独立的，根据概率乘法定理，上述每单个分法的概率都为$$p_1^{k_1}p_2^{k_2}...p_n^{k_n}$。
因此，我们得到

$$P(B)=N!/(k_1!k_2!...k_n!)p_1^{k_1}p_2^{k_2}...p_n^{k_n}$$

上式即为**多项分布**, 其名称来源于该式和多项展开式

$$(x_1+x_2+...+x_n)^N=\sum^{*}\frac{N!}{k_1!k_2!...k_n!}x_1^{k_1}x_2^{k_2}...x_n^{k_n}$$

其中$$\sum^{*}$$代表求和范围中蕴含条件$\sum k_n=N$。

多项式分布在实际应用中经常见到。当一个总体按照某种属性分为几类时，就是多项分布。
如产品的分类概率已知条件下，中一等、二等、三等和不合格数量的分布。

当$n=2$时，多项分布回到了二项分布。同样地，此分布中$P(X_1)$的分布，属于$M(N,p_1,p_2,...,p_n)$的边缘分布，也属于二项分布。


## 边缘分布

## 卡方分布

$\Gamma$函数和$B$函数

$$\Gamma(x)=\int_0^{\infty}e^{-t}t^{x-1}dt (x>0)$$

$$B(x,y)=\int_0^1 t^{x-1}(1-t)^{y-1}dt (x>0, y>0)$$

B函数和$\Gamma$函数满足

$$B(x,y)=\Gamma(x)\Gamma(y)/\Gamma(x+y)$$

由$\Gamma$函数的定义，可得

$$k_n(x)=
\begin{cases}
\frac{1}{\Gamma(n/2)2^{n/2}}e^{-x/2}x^{(n-2)/2} & n>0 \\
0 & x\leq 0
\end{cases}
$$

- [ ] 是概率分布函数。

此函数为**自由度为$n$的皮尔逊卡方分布**, 简称**卡方分布**, 记为$\chi_n^2$。


- [ ] 雅克比行列式

分布绘图代码:

<script src="https://gist.github.com/LfqGithub/d1ec37ce65755a5c8cf5a7c7d4b7a0cc.js"></script>




# 随机变量数字特征

## 期望

设随机变量$X$只取有限个可能只$a_1,a_2,...,a_n$, 其概率分布为$P(X=a_i)=p_i(i=1,2,...,n)$, 则$X$的数学期望，记为$E(X)$或$EX$为

$$E(X)=a_1p_1+a_2p_2+...+a_np_n$$


## 中位数
连续型随机变量 $X$ 的分布函数为$F(x)$, 满足条件

$$P(X\leq m)=F(m)=1/2$$

的数 $m$ 称为 $X$ 或分布 $F$ 的中位数。

## 期望 vs 中位数

中位数存在一些优势：
- 中位数一直存在，均值不是对任何随机变量都存在
- 中位数在描述某些量的代表性数值时，比期望更能说明问题，如某社区内人的收入的中位数，相比数学期望，更具有代表性，因为其受少数特别大或者特别小的样本影响较小。
但是, 无论是在理论和实际应用中国，期望都更重要。 这是因为：
- 数学上处理均值很方便。如加法的均值等于均值的加法。而中位数的计算不存在这么简单的关系。
- 中位数可以不唯一
- 离散型的变量$X$，虽然也可以定义中位数，但是效果并不理想，不完全符合“中位”这一词所应有的含义。


## 方差

[Variance](https://zh.wikipedia.org/wiki/%E6%96%B9%E5%B7%AE)

随机变量$X$的分布为$F$, 则

$$ Var(X) = E(X-EX)^2$$

称为$X$的方差。其平方根 $\sqrt{Var(X)}$ 为标准差。

方差之所以称为刻画散步度的最重要的数字特征，是因为它具有一些优良的数学性质。
- 常数的方差为0
- 独立随机变量之和的方差等于各变量的方差之和。



## 协方差

[Covariance](https://zh.wikipedia.org/wiki/%E5%8D%8F%E6%96%B9%E5%B7%AE)

设$[X,Y]$为二维随机向量，$X, Y$本身都是一维随机变量，可定义其均值、方差。记

$$E(X)=m_1, E(Y)=m_2, Var(X)=\sigma^2_1, Var(Y)=\sigma^2_2$$

称

$$E[(X-m_1)(Y-m_2)]$$为$X, Y$的**协方差(Covariance)**。

$X$的方差为$E[(X-m_1)(X-m_1)]$, 协方差将其中的一个$(X-m_1)$换成$(Y-m_2)$, 其形式接近方差，又有$X,Y$的参与，由此得出协方差的名称。

- 衡量两个变量的总体误差
- 方差是协方差的一种特殊情况，即两个变量是相同的情况

$$\mathrm{cov}(X,X)=\mathrm{var}(X)$$

- 期望值分别为$E(X)=\mu$和$E(Y)=\nu$的两个具有有限二阶矩的实数随机变量$X$与$Y$的协方差的定义为
  - $\mathrm{cov}(X, Y)=E[(X-\mu)(Y-\nu)]=E(X \cdot Y)-\mu \nu$

- [ ] 定理1: 若$X,Y$独立，则$\mathrm{cov}(X,Y)=0$
  - 证明由定理: **若干随机变量的期望之积等于各变量的期望之积**直接得出。
- [ ] 定理1：$[\mathrm{cov}(X,Y)]^2\leq \sigma_1^2\sigma_2^2$, 等号当且仅当$X,Y$间有严格线性关系(即存在常数$a,b$使得$Y=aX+b$成立)时成立--P124

**相关系数**：$\mathrm{cov}(X,Y)/\sigma_1\sigma_2$为$X,Y$的相关系数,记为$\mathrm{Corr}(X,Y)$。(Corr是Correlation的缩写)
- 由此产生定理 1, 2 的衍生定理
  - 定理$1^\*$: 若$X,Y$独立，则$\mathrm{Corr}(X,Y)=0$
  - 定理$2^\*$: $-1 \leq \mathrm{cov}(X,Y)\leq 1$, 等号当且仅当$X,Y$间有严格线性关系(即存在常数$a,b$使得$Y=aX+b$成立)时成立
- [ ] p126--$\mathrm{cov}(X,Y)=0$时，称$X,Y$不相关。前者是后者的必要不充分条件。即当两个变量为统计独立的，则二者协方差为0 （反之不成立）。
- [ ] (线性)相关系数的理解

协方差性质

$$\begin{aligned}
\mathrm{cov}(X,Y)& =\mathrm{cov}(Y,X) \\

\mathrm{cov}(aX,bY)& =ab\mathrm{cov}(X,Y) \\

\mathrm{cov}(\sum\limits_{i=1}^{n}X_i,\sum\limits_{j=1}^{m}Y_j)& =\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{m}\mathrm{cov}(X_i,Y_j) \\

\mathrm{cov}(\sum\limits_{i=1}^{n}X_i)& =\sum\limits_{i=1}^{n}\mathrm{var}(X_i)+2\sum\limits_{i,j:i<j}^{m}\mathrm{cov}(X_i,X_j) \\

\mathrm{var}(X) & \ge 0\\

P(X=a)& =1 \equiv \mathrm{Var}(X)=0 \\

\mathrm{var}(X+\mathrm{a})& =\mathrm{Var}(X) \\

\mathrm{var}(\mathrm{a}X)& =\mathrm{a}^2\mathrm{var}(X) \\

\mathrm{var}(aX+bY)& =a^2\mathrm{var}(X)+b^2\mathrm{var}(Y)+2ab \mathrm{cov}(X, Y) \\

\mathrm{var}(X-Y)& =\mathrm{Var}(X)+\mathrm{var}(Y)-2\mathrm{cov}(X, Y)\\

\mathrm{var}(\sum_{i=1}^{N}X_i)& =\sum_{i,j=1}^{N}\mathrm{cov}(X_i, X_j) \\

& =\sum_{i=1}^{N}\mathrm{var}(X_i)+\sum_{i\neq j}\mathrm{cov}(X_i, X_j)

\end{aligned}$$

如果两个变量的变化趋势一致， 即如果一个变量大于自身的期望值，另一个也大于自身的期望值，则两个变量的协方差就是正值，否则为负值。

## 矩

设$X$为随机变量，$\mathrm{c}$为常数，$k$为正整数，则

$$E(X-\mathrm{c})^k$$

称为$X$关于$\mathrm{c}$点的**$k$阶矩**。

当$\mathrm{c}=0$, 此时$a_k=E(X^k)$称为$X$的**$k$阶原点矩**。
当$\mathrm{c}=E(X)$, 此时$\mu_k=E[(X-EX)^k]$称为$X$的**$k$阶中心矩**。

一阶原点矩即期望，一阶中心距$\mu_1=0$, 二阶中心矩即为方差$\mathrm{Var}(X)$。
统计学上，高于四阶的矩很少使用。三四阶用的也较少。


### 偏度系数

三阶矩的应用之一：偏度系数

$X$的概率系数$f(x)$关于某点$a$对称，即

$$f(x-a)=f(x+a)$$

则$a=E(X)$。且$\mu_3=E[(X-a)]^3=0$。例如，对于正态分布，有$\mu_3=0$。
如果分布差生了偏离，$\mu_3$也会偏离0。此时$\mu_3$显著异于0，意味着分布于正态分布差生了较大的偏离。
如果$\mu_3>(<)0$, 则称分布为正(负)偏或者右(左)偏。

由于$\mu_3$是$X$因次的三次方，因次为了抵消这一点(无量纲化?), 以$X$标准差的三次方，即$\mu_2^{3/2}$去除$\mu_3$， 其商

$$\beta_1=\mu_3/\mu_2^{3/2}$$

称为$X$或其分布的**偏度系数**。


### 峰度系数

$\mu_4$可以衡量分布函数在均值附近的陡峭程度。

$$\mu_4=E[X-E(X)]^4$$

可以看出，若$X$的取值在概率上很集中在$E(X)$附近，则$\mu_4$较小，反之较大。

为抵消尺度的影响(无量纲化), 以标准差的四次方即$\mu_2^2$去除，得

$$\beta_2=\mu_4/\mu_2^2$$

成为$X$或其分布的**峰度系数**。

若$X$有正态分布$N(\mu, \sigma)$, 则$\beta_2=3$, 与$\mu$和$\sigma$无关。为了迁就这一点，常定义$\mu_4/\mu_2^2-3$为峰度系数，使得正态分布有峰度系数0.


- [ ] 香帅的北大金融学课中的偏度和峰度




## 中心极限定理和大数定理

- 有时一个有限的和很难求，但一经取极限从有限过渡到无限，问题反而好解决。
  - [ ] $$\sum\limits_{n=1}^{\infty}\frac{x^n}{n!}=e^x$$ or $$\lim\sum\limits_{n=1}^{\infty}\frac{x^n}{n!}=e^x$$

**大数定理**: 设$X_1, X_2,..., X_n$是独立同分布的随机变量，记他们的公共均值为$a$,他们的方差为$\sigma^2$, 则对任意给定的$\epsilon>0$,有

$$\lim\limits_{n\rightarrow \infty} P(\vert \overline{X}_n - a \vert \geq \epsilon) =0$$

其中

$$\overline{X}_n=(X_1+X_2+...+X_n)/n$$

$$\overline{X}_n=
\begin{cases}
1 & \textrm{A happens in i-th experiment} \\
0 & \textrm{A does not happen in i-th experiment} 
\end{cases}
$$

上述大数定理的含义：不论给定多小的$\epsilon>0$, 当$n$很大时，$\overline{X}_n$与$a$的偏离达到$\epsilon$或者更大的概率很小。

### 马尔科夫不等式

$$P(Y\geq\epsilon)\leq E(Y)/\epsilon$$

此不等式有一个重要特例, 即契比雪夫不等式

### 契比雪夫不等式

若$\mathrm{Var}(Y)$存在，则

$$P(\vert \overline{X}_n-EY\vert \geq \epsilon)\leq \mathrm{Var}(Y)/\epsilon^2$$

- [ ] 大数定理与大数定律



### 中心极限定理

中心极限定理是一类定理，概率论上，习惯于把和的分布售前与正态分布的一类定理叫做中心极限定理。

设$X_1,X_2,...,X_n$为独立同分布的随机变量，$E(X_i)=a$, $\mathrm{Var}(X_i)=\sigma^2(0<\sigma^2<\infty$, 则对于任何实数

$$\lim\limits_{n\rightarrow\infty} P(\frac{1}{\sqrt{n}\sigma}(X_1+X_2+...+X_n-na)=\Phi(x)$$

其中$\Phi(X)$为标准正态分布$N(0,1)$, 即

$$\Phi(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-t^2/2}dt$$


# 概率运算

## 随机变量函数的概率分布

先考虑一个变量的情况(b1, p79)。设$X$有密度函数$f(x)$, 设$Y=g(x)$, 且$g$为严格上升的函数。又设$g$的导数$g^{'}$存在，
由于$g$的严格上升性，其反函数$X=h(Y)$存在，且$h$的导数$h^{'}$也存在。

对于任意实数$y$, 因$y$严格上升，因此事件$\{g(X)\leq y\}$相当于$\{X>h(Y)\}$。因此有

$$P(Y\leq y)=P(g(X)\leq y)=P(X\leq h(y)=\int^{h(y)}_{-\infty} f(t)dt$$

$Y$的密度函数$l(x)$即对$y$求导数。

$$l(y)=(P(y\leq y))^{'}=(\int^{h(y)}_{-\infty} f(t)dt)^{'}=f(h(y))h^{'}(y)$$

将此公司应用到$g(x)$单调减的情况

$$l(y)=f(h(y))\vert h^{'}(y)\vert$$


# 常用公式

$${N\choose k} =\sum\limits_{i=0}^{k}{m\choose i}{n\choose {k-i}}$$

此公式由恒等式

$$(1+x)^{m+n} =(1+x)^m (1+x)^n$$

即

$$\sum\limits_{i=0}^{m+n} {m+n \choose i} = \sum\limits_i^m {m\choose i}x^i \sum\limits_{j=0}^{n} {n\choose j} x^j$$

中 $x^k$ 的系数得到。


# Todo

- [ ] 欧氏空间
- [ ] $n!2^n/(2n)!=1/(2n-1)!!$
- [ ] 出错概率如何估计？



# Appendix

## A0: Notes

- $r!$，当$r$不是非零整数时，该表达式没有意义。

## A1: Librarian or Farmer?

- Prior： 先验概率
- $P(H)$: 假设概率, H: hypothesis
- $P(E\vert H)$: 似然概率 likelihood, E: Evidence
- $P(E\vert \urcorner H)$: 假设不成立情况下看到证据的概率

证据E：Steve 性格 爱好

假设H: Steve是一个图书馆管理员

求：证据是真的前提下，假设成立的概率

- [ ] 无证据前，

## A2: 中国古典概率思维

- 二鸟在林不如一鸟在手

## A3：常用公式定理

a3-1. 对$e^x$进行泰勒展开，可得 $$e^x=\sum\limits_{n=0}^{\infty}\frac{x^n}{n!}$$

## 辅助证明

### Gamma函数

$$\Gamma(x)=\int_0^{\infty}e^{-t}t^{x-1}dt (x>0)$$

$\Gamma$函数的计算

- $\Gamma(1)$

$$
\begin{aligned}
\Gamma(1) & = \int_0^{\infty}e^{-t}dt \\
& = -e^{-t}\vert_0^{\infty}
& = 1
\end{aligned}$$

- $\Gamma(1/2)$

$$\Gamma(1/2)  = \int_0^{\infty}e^{-t}t^{-1/2}dt $$

令$t=\mu^2$

$$
\begin{aligned}
\Gamma(1/2) & = \int_0^{\infty} e^{-\mu^2}\mu^{-1}d\mu^2 \\
& = \int_0^{\infty} 2\mu e^{-\mu^2}d\mu \\
& = \sqrt{\pi}
\end{aligned}$$

$$I=\int_0^{\infty}xe^xdx$$的证明见[常用积分的证明](https://yundongxiaoyang.top/math/common_used_integral/)。

容易证明，**$\Gamma$函数具有以下性质**

$$\Gamma(x+1)=x\Gamma(x)$$

证明： 

$$\begin{aligned}
\Gamma(x+1) & =\int_0^{\infty}e^{-t}t^{x}dx \\
& = -\int_0^{\infty}t^{x}de^{-t} \\
& = -e^{-t}x^{-t}\vert^{\infty}_0+\int_0^{\infty}e^{-t}dt^{x} \\
& = xt^{x-1}\int_0^{\infty}e^{-t}dt \\
& =x\Gamma(x)
\end{aligned}$$

由此，我们可以得出当$n$为正整数时，

- $\Gamma$函数的计算通式

$$\begin{aligned}
\Gamma(n)& =(n-1)! \\
\Gamma(n/2)& =1\cdot 3\cdot 5 \cdot ...\cdot (n-2)2^{(-n-1)/2}\sqrt{\pi}
\end{aligned}$$






# Ref

- b1: 陈希孺，数理统计与概率论, 中国科学技术大学出版社
- [贝叶斯公式的简单证明-3B1B](https://www.bilibili.com/video/av84799859/?spm_id_from=333.788.videocard.1)
- [贝叶斯定理，使概率论直觉化-3B1B](https://www.bilibili.com/video/av84799361)
- [浅谈协方差矩阵-进击的马斯特](http://pinkyjie.com/2010/08/31/covariance/)
- [The Elements of Statistical Learning: Data Mining, Inference, and Prediction--downloadable](https://web.stanford.edu/~hastie/ElemStatLearn/)



