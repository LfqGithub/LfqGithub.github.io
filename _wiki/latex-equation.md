---
layout: wiki
title: Latex equation and symbol
categories: Latex
description: all
use_math: true
keywords: latex, symbol, equation, 符号, 公式
---


# Equation

## 等号对齐

```latex
\begin{aligned}
	a&=b \\
	 &=c
\end{aligned}
```
$$\begin{aligned}
	a&=b \\
	 &=c
\end{aligned}$$


## 分段函数

```latex
f(x)=
\begin{cases}
\lambda e^{-\lambda x} & (x>0) \\
0 & (x\leq 0)
\end{cases}
```

$$f(x)=\begin{cases}\lambda e^{-\lambda x} & (x>0) \\
0 & (x\leq 0)
\end{cases}$$

# Symbols

## 符号位置
- `\mathop{\text{sup}}\limits_{\theta\in\Theta}`: $\mathop{\text{sup}}\limits_{\theta\in\Theta}$, `\limits`只能放到数学符号之后，为达到该效果，需将文本转换为数学符号，故添加`\mathop{}`。 

## 统计

- `\mathcal{X}`: $\mathcal{X}$, 样本空间或状态空间
- `\mathcal{D}`: $\mathcal{D}$, 概率分布
- `D`: $D$, 数据样本(数据集)
- `\mathcal{H}`: $\mathcal{H}$, 假设集
- `\mathfrak{L}`: $\mathfrak{L}$, 学习算法
- `\text{sup}`: $\text{sup}$, 上确界


- `\sim`: $\sim$
- `\backslash`: $\backslash$ 

## 数字处理

- `\lfloor n \rfloor`: $\lfloor n \rfloor$, 下取整
- `\lceil n \rceil`: $\lfloor n \rfloor$, 上取整

## 集合

- `\mathbb{Z}`:$\mathbb{Z}$
- `\mathbb{R}`:$\mathbb{R}$
- `\mathbb{N}`:$\mathbb{N}$
- `\subset`: $\subset$, 真包含
- `\subseteq`: $\subseteq$, 包含
- `\supset`: $\supset$, 包含
- `\notin`: $\notin$
- `\in`: $\in$
- `\exists`: $\exists$, 存在
- `\forall`: $\forall$, 任意

## 导数

- `\partial`: $\partial$, 偏导
- `\mathrm{d}`: $\mathrm{d}$, 求导
- `x^{'}`: $x^{'}$, 撇形式求导
- `\nabla f`: $\nabla f$, 全微分算子

## 空格/符号间距

- `a \qqad b`: $a \qquad b$ 两空格
- `a \qad b`: $a \quad b$ 单空格
- `a\ b`: $a\ b$ 大空格
- `a\;b`: $a\;b$ 中等空格


## 正文

`mathrm` and `textrm`区别

- `\mathrm` 公式中该部分内容变成罗马字体
- `\textrm` 暂时切换到文本模式，此时字体大小切换机制不起作用

举例来说，下式中，公式中添加文本，简单起见，需要使用`\textrm`而非`\mathrm`。

```latex
\overline{X}_n=
\begin{cases}
1 & \textrm{A happens in i-th experiment} \\
0 & \textrm{A does not happen in i-th experiment} 
\end{cases}
```

$$\overline{X}_n=
\begin{cases}
1 & \textrm{A happens in i-th experiment} \\
0 & \textrm{A does not happen in i-th experiment} 
\end{cases}
$$

## 黑体

- `\bf`: ${\bf r,u}$

### 上标

`\overline{A}`: $\overline{A}$, 读作A bar。
`\hat{A}`: $\hat{A}$


## 其他

- `\sum` $\sum$
  - `\sum\limits_{i=1}^{10}`: $\sum\limits_{i=1}^{10}$
  - `\sum_{i=1}^{10}`:$\sum_{i=1}^{10}$

- 括号大小控制
  - 配对使用,自动调整大小
    - `\left(`, `\right)`: 圆括号
    - `\left[`, `\right]`: 中括号
    - `\left\{`, `\right\}`: 花括号
  - 独立使用,长用于需要换行的公式
    - `\big, \Big, \bigg, \Bigg`四种大小
      - `\big[`,`\big]`: 大中括号
      - `\big\{`,`\big\}`: 大花括号

## 概率统计常用符号

- $\vert$: `\vert`, 表示 given that, 用于条件概率，如$P(A\vert B)$
- ${n \choose k}$: 表示组合数，等同于$C_n^k$。

## 特殊格式
- 字符在符号上方 `X_1,X_2,...,X_n\stackrel{IDD}{\sim}F(x)`: $X_1,X_2,...,X_n\stackrel{IDD}{\sim}F(x)$

## 希腊字母
### 小写

|Latex        | symbol       | Latex     | symbol    |  Latex     | symbol    | Latex     | symbol   |
|-----------  |--------------|-----------|-------    | -----------|-------    |-----------|-------   |
|`\alpha`     |$\alpha$      |`\eta`     |$\eta$     | `\nu`      |$\nu$      |`\tau`     |$\tau$    |
|`\beta`      |$\beta$       |`\theta`   |$\theta$   | `\xi`      |$\xi$      |`\upsilon` |$\upsilon$|
|`\gamma`     |$\gamma$      |`\iota`    |$\iota$    | `o`        |$o$        |`\phi`     |$\phi$    |
|`\delta`     |$\delta$      |`\kappa`   |$\kappa$   | `\pi`      |$\pi   $   |`\chi`     |$\chi$    |
|`\epsilon`   |$\epsilon$    |`\lambda`  |$\lambda$  | `\rho`     |$\rho$     |`\psi`     |$\psi$    |
|`\zeta`      |$\zeta$       | `\mu`     |$\mu$      |  `\sigma`  |$\sigma$   | `\omega`  |$\omega$  |
|`\varepsilon`|$\varepsilon$ |`\vartheta`|$\vartheta$|`\varsigma` |$\varsigma$|`\varphi`  |$\varphi$ |
|`\varpi`     |$\varpi$      |`\varrho`  |$\varrho$  |     -      |      -    |    -      |   -      |

### 大写

|Latex      | symbol       | Latex     | symbol  |  Latex     | symbol   | Latex     | symbol   |
|-----------|--------------|-----------|-------  | -----------|-------   |-----------|-------   |
| -         |  -           |  -        |  -      |   -        |   -      |  -        |  -       |
| -         |  -           |`\Theta`   |$\Theta$ | `\Xi`      |$\Xi$     |`\Upsilon` |$\Upsilon$|
|`\Gamma`   |$\Gamma$      |     -     |   -     |     -      |  -       |`\Phi`     |$\Phi$    |
|`\Delta`   |$\Delta$      |     -     |  -      | `\Pi`      |$\Pi   $  |  -        |   -      |
|    -      |  -           |`\Lambda`  |$\Lambda$|      -     |   -      |`\Psi`     |$\Psi$    |
|    -      |  -           |      -    |   -     |  `\Sigma`  |$\Sigma$  | `\Omega`  |$\Omega$  |
|    -      |  -           |        -  |   -     |    -       | -        |-          |  -       |


## 罗马数字

```latex
% add to pre.tex
\makeatletter
\newcommand{\rmnum}[1]{\romannumeral #1}
\newcommand{\Rmnum}[1]{\expandafter\@slowromancap\romannumeral #1@}
\makeatother
% latex article 
\rmnum{1} % low case
\Rmnum{1} % upper case
```


## 数学符号
- n方根: `\sqrt[n]{x}` $\sqrt[n]{x}$
- 梯度：`\nabla` $\nabla$
- 平均：`\langle a \rangle` $\langle a \rangle$ 
- 泛函: `\mathcal D` $\mathcal D$ 

## 标点

- 点乘： `\cdot`  $\cdot$
- 叉乘： `\times`  $\times$
- 除以： `\div`  $\div$
- 大于等于： `\geq`  $\geq$
- 小于等于： `\leq`  $\leq$
- 远大于： `\gg` $\gg$
- 远小于： `\ll` $\ll$
- 等价于
  - `\equiv`  $\equiv$
  - `\Leftrightarrow`  $\Leftrightarrow$
- 约等于
  - `\simeq`  $\simeq$
  - `\approx`  $\approx$
  - `\sim`  $\sim$
- 不等于： `\neq`  $\neq$
- 协方差： `\mathrm{Cov}`  $\mathrm{Cov}$ 
- 方差： `\mathrm{Var}`  $\mathrm{Var}$ 或者 $\sigma$ 表示

## 德语

<div align="center"><img width="600" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/german2.jpg"/></div>
> 符号外加大括号，如: `{\'{o}}`

# Links

- [ctan-latex symbols](https://ctan.org/pkg/comprehensive)

