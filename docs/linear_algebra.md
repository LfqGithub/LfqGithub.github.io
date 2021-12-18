---
layout: math
title: Linear Algebra
keywords: math, algebra
categories: [math] 
use_math: True
description: Note about linear algebra.
---

Updating......

# Lingo/term
- linearly (in)dependent
- basis of a vector space is a set of linearly independent vectors than span the full space.
- linear transformation
- transformation: essentially a fancy word for "function", it is something that takes in inputs and out an output for each one. 
  - In linear algebra, the transformations that take in some vector and spit out another vector.
  - Why use the world "transformation" instead of "function" if they mean the same thing?
    - It is to be suggestive to a certain way to visualize this input-output relation.
	- Transformation let us imagine watching every possible input vector move over to its corresponding output vector.
- linear transformation: All lines remain lines, without getting curved, and the origin must remian fixed in place. 
-  

# 理解
## 矩阵变换到底是什么？
   平面中，一对基向量经过一个变换后, 变成了另一组基向量，然而用此对基向量表示的任意向量的表达式保持不变，即$(\vec{x},\vec{y})$经过某种变换后变成$(\vec{x'},\vec{y'})$, 此时原来的向量$\vec{v}=a\vec{x}+b\vec{y}$和基向量的关系仍保持不变，变换后$\vec{v'}=a\vec{x'}+b\vec{y'}$， 原理也很直观：平行四边形经过线性变换后仍为平行四边形，且两边和对角线的关系保持不变。
   
   而这个将基向量对$(\vec{x},\vec{y})$变为新的基向量对$(\vec{x'},\vec{y'})$(当然, 同时也将任意向量$\vec{v}$变换成了$\vec{v'}$)的“变换", 即tranformation, 可以用
T=$$\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix}$$
表示，其含义为将原始的基向量$\vec{x}=(1,0),\vec{y}=(0,1)$ 变成新的基向量$\vec{x'}=(a,c),\vec{y}=(b,d)$。
用完整的线性代数的表示方式为：

$$\vec{v}=(a,b)=a\vec{x}+b\vec{y}$$

$$\vec{T}\vec{v}=
\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix}
[a,b]
=a
\begin{bmatrix}
a\\
c\\
\end{bmatrix}
+b
\begin{bmatrix}
b\\
d\\
\end{bmatrix}
$$

此关系即矩阵的乘法规则： 前一个矩阵的i行，乘以后一个矩阵的j列，作为新矩阵的$t_{ij}$元素。

完整的表达为: 变换
$T=$
$$\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix} $$
作用于一个向量$\vec v=(a,b)$上，变换后的向量为$\vec v'$为
$$\vec{v'}=
\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix}
[a,b]
=a
\begin{bmatrix}
a\\
c\\
\end{bmatrix}
+b
\begin{bmatrix}
b\\
d\\
\end{bmatrix}
$$

同样地,对于三维向量: 变换
$T=$
$$\begin{bmatrix}
a & b & c\\
d & e & f\\
g & h & i\\
\end{bmatrix} $$
作用于一个向量$\vec v=(l,m,n)$(严格写法
$$\vec v=
\begin{bmatrix}
l\\
m\\
n\\
\end{bmatrix}
$$)
上，变换后的向量为$\vec v'$为
$$\vec{v'}=
\begin{bmatrix}
a & b & c\\
d & e & f\\
g & h & i\\
\end{bmatrix}
[l,m,n]
=l
\begin{bmatrix}
a\\
d\\
g\\
\end{bmatrix}
+m
\begin{bmatrix}
b\\
e\\
h\\
\end{bmatrix}
+n
\begin{bmatrix}
c\\
f\\
i\\
\end{bmatrix}
$$


此外，我们还可以从变换矩阵的表达式，即

$$\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix} $$


看出其他常用的信息，举例来说，
$$\begin{bmatrix}
0 & 1\\
1 & 0\\
\end{bmatrix} $$
这个变换, 代表将原来的基向量$\vec x=(1,0), \vec y=(0,1)$变成了$\vec x=(0,1), \vec y=(-1,0)$，即将笛卡尔坐标系的$x,y$轴逆时针旋转了90$^\circ$ (or 顺时针270 $^\circ$, whatever)。

而
$$\begin{bmatrix}
1 & 1\\
0 & 1\\
\end{bmatrix} $$
表示的就是$x$轴不变，而将$\vec y=(0,1)$变换成了$(1,1)$，从几何上看，可以看出这是一个 shear（剪切）操作。

*To sum up, line transformations are way to move around space, such the grid lines remain parallel and evenly spaced and such that the origin ramains fixed. Delightfully, these transformations can be described using only a handful of numbers: the coordinates of where each basis vector lands. Matrices give us a language to describe these transformations, where the columns represents those coordinates. And matrix-vector multipulation is just a way to compute what that transformation does to a given vector* 

## 复合矩阵变换
对一个向量$\vec v$的两次操作，我们记为$T_1, T_2$， 则此时$\vec v$需要左乘两个矩阵，记为$T_2T_1\vec v$

两个矩阵相乘，可以认为是两次变换的连续.
$$
T_1T_2=
\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix}
\begin{bmatrix}
e & f\\
g & h\\
\end{bmatrix}
=
\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix}
\begin{bmatrix}
e & f\\
g & h\\
\end{bmatrix}
\begin{bmatrix}
1 & 0\\
0 & 1\\
\end{bmatrix}
$$
即两次变换连续作用到初始的笛卡尔坐标的基向量上。

## Determinant
- Determinant of the transformation: 矩阵(变换)的行列式 
- 矩阵$\bf A$行列式的表示方法: det($\bf A$)或$\|\bf A\|$

### 理解行列式
以2x2矩阵为例, 行列式若大于0，在几何层面的解释为: 平面上一个图形经过该矩阵的变换后，变换后面积为初始面积的倍数(原始坐标系中的“网格线”经变换后保持平行且等距的前提下)。当行列式为0时，代表变换后面积变为0: 初始基矢从$(1,0), (0,1)$变成了两个线性相关的矢量，即两基矢平行, 更特殊地，有可能两基矢都变为$(0,0)$。 当行列式值为负时，代表二维平面的方向改变（从起始时$\vec x$基矢在$\vec y$基矢右侧变为左侧), 即转换改变了空间的定向(orientation of space)。在行列式从正慢慢变小成为0时，两基矢的夹角慢慢减小，当两基矢方向重合时，此时基矢构成的四边形面积为0。当基矢$\vec x$旋转越过基矢$\vec y$后，此时面积大于0，但是基矢$\vec x, \vec y$的相对位置相反，因此认为此时空间的定向发生了变化，行列式此时为负。

举例来说，一个矩阵(变换)
$$\begin{bmatrix}
a & 0\\
0 & b\\
\end{bmatrix}$$
将原始的
$$\begin{bmatrix}
1 & 0\\
0 & 1\\
\end{bmatrix}$$
基向量(基矢)$\vec x=(1,0)$和$\vec y=(0,1)$变为$(a,0)$和$(0,b)$, 基向量在$\vec x$方向上被拉伸了$a$倍，在$\vec y$方向上被拉伸了$d$倍。因此其行列式为$(a\*d)/(1\*1)=ab$。
更普遍地，当转换
$$\begin{bmatrix}
a & b \\
c & b \\
\end{bmatrix}$$
中$b,c$不同时为0时，$bc$代表平行四边形在对角方向上被拉伸或压缩了多少, 如下图所示
<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/linear-algebra/determinant-schematic.png"/></div>


同样地，3x3矩阵，为变换后体积为初始体积的倍数。当行列式的列线性相关时，行列式为0，代表该转换降低了维度，即三个基矢在二维平面/一维线上/零维点上(三基矢线性相关): *检验一个矩阵的行列式是否为0，就可以推测出矩阵所代表的变换是否将空间压缩到了更小的维度上*。三维矩阵行列式的正负变换意味着三维空间的定向发生了变化。
注释：三维空间的定向：右手定则：右手食指指向$\vec x$,中指指向$\vec y$，此时把拇指竖起来，指向$\vec z$的方向, 此时，行列式为正，否则为负。

### Matrix properties
- The determinant of resulting matrix is the same as the product of the determinants of the original two matrixs

## 逆矩阵、列空间与零空间

### 逆矩阵

[定义](https://zh.wikipedia.org/wiki/%E9%80%86%E7%9F%A9%E9%98%B5)：给定一个方阵$\bf A$, 如果存在另一个矩阵$\bf B$， 使得${\bf AB}={\bf BA}={\bf I}_n$, 其中${\bf I}_n$为$n$阶单位矩阵，则称$\bf A$是可逆的，且$\bf B$和$\bf A$互为可逆矩阵。

#### 理解逆矩阵

$${\bf A}{\bf A}^{-1}=1$$在几何上的含义为：变换${\bf A}$和${\bf A}$作用后，空间没有发生任何变化，仍变回了之前的空间，即对于二维空间
$${\bf A}{\bf{A}^{-1}}=
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
\end{bmatrix}$$

${\bf{A}^{-1}}$的含义就是能抵消矩阵${\bf A}$代表的变换作用的一个变换。


#### 逆矩阵解线性多元一次方程组

对于一个三元一次线性方程组(linear system of equations)
$$\begin{bmatrix}
{\text a}x+{\text b}y+{\text c}z={\text d} \\
{\text e}x+{\text f}y+{\text g}z={\text k} \\
{\text l}x+{\text m}y+{\text n}z={\text j} \\
\end{bmatrix}$$
可视为一个$3\times 3$系数矩阵
$$
{\bf A}=
\begin{bmatrix}
{\text a}& {\text b}&{\text c} \\
{\text e}& {\text f}&{\text g} \\
{\text l}& {\text m}&{\text n} \\
\end{bmatrix}$$
和一个未知向量
$$\vec x=
\begin{bmatrix}
x\\
y\\
z\\
\end{bmatrix}
$$
的乘积，等于一个已知向量
$$\vec v=
\begin{bmatrix}
{\text d}\\
{\text k}\\
{\text j}\\
\end{bmatrix}$$
即
$${\bf A}{\vec x}={\vec v}$$
这样，问题就变成了，一个线性变换${\bf A}$，将一个未知向量$\vec x$变换成向量$\vec v$。
解未知数$x,y,z$就变成了寻找这个未知向量$\vec x$。

几何上找到这个未知向量的方法为：对向量$\vec v$进行与矩阵${\bf A}$相反的变换${\vec x^{-1}}$，追踪该向量最终的位置，该最终向量即和$\vec x$重合。

当矩阵的行列式为0时，即此变换将二维空间的维度降低,变成了一维的线，此时无对应的逆变换${\vec x^{-1}}$，因为一个变换无法将一个低维度的线解压为高温度的平面(变换本质上是一个函数，函数只能一个输入对应一个输出，或者多个输入对应一个输出，但是无法一个输入对应多个输出。一维的线变成一个面，相当于一条向量对应无数条向量，因此此变换违反了函数的定义)。

矩阵行列式为0，并不意味着此方程组无解，因为有一种可能：当进行完${\vec x}$的变换后，该变换将二维平面压缩到了一条线上，而向量$\vec v$的恰好位于这条线上, 此时方程仍有解。

### 秩
[定义](https://zh.wikipedia.org/wiki/%E7%A7%A9_(%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0)): 矩阵$\bf A$的列秩是$\bf A$的线性无关的纵列的极大数目。类似地，行秩是$\bf A$的线性无关的横行的极大数目。矩阵的行秩和列秩总是相等的(why?), 因此二者都可以称作矩阵$\bf A$的秩(rank)。
当一个变换将三维空间变为一个平面（二维）时，此时次变换的秩为2；同样地，变成一条线后，秩为1。

矩阵$\bf A$的秩表示为$r({\bf A})$, $rank({\bf A})$或$rk({\bf A})$。

#### 理解秩

number of dimensions in the output, 准确地讲，是列空间的维数。





### 点积

- 定义：dot product, 又称scalar product（数量积), 是指接受在实数R上的两个向量并返回一个实数值标量的二元运算，是欧几里得空间的标准内积。
两向量$\vec a=[a_1,a_2,a_3,...a_n]$和$\vec b= [b_1,b_2,b_3,...,b_n]$的点积定义为${\vec a} \cdot {\vec b}=a_1b_1+a_2b_2+a_3b_3+...+a_nb_n$。
还可以写成${\vec a} \cdot {\vec b}=({\vec a}^T)*{\vec b}$, 其中${\vec a}^T$是$\vec a$的转置矩阵。

*Q: 为什么与单位向量的点积可以解读为将向量投影到单位向量所在直线所得到的投影长度?*

思路：
以二维空间中的向量为例, $\vec a$和$\vec b$的点积是二维空间中向量$\vec a$将向量$\vec b$变成为一个数(即一维空间中的一个点)的一个转换过程。
换句话说，此变换将二维空间中的所有点，转换到一维线上。
如下图所示，我们将这个一维直线放入二维空间中，一个数字$u=1$对应到一维直线上的一个点的同时，还同时对应这个二维空间上的一个向量，我们将之命名为$\vec u$。
<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/linear-algebra/dot_product.png"/></div>

将二维空间中的基向量$\vec x=[1,0]$投影到$\vec u$上，在数值上和$\vec u$投影到$\vec x$上相等, 为$u_x$。
同样地，
将二维空间中的基向量$\vec y=[0,1]$投影到$\vec u$上，在数值上和$\vec u$投影到$\vec y$上相等,为$u_y$。

此变换的表达式为$[u_x,u_y]$，为一个$1\times2$矩阵。
空间中任意向量经过投影变换的结果，也就是投影变换与这个向量相乘，和这个向量与$\vec u$的点积在计算上完全相同。
$$
\begin{bmatrix}
u_x & u_y\\
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
\end{bmatrix}
=
\begin{bmatrix}
u_x\\
u_y\\
\end{bmatrix}
\cdot 
\begin{bmatrix}
x\\
y\\
\end{bmatrix}
=
u_x\cdot x+u_y\cdot y
$$
这一过程解释了为什么与单位向量的点积可以解读为将向量投影到单位向量所在直线所得到的投影长度。

非单位向量可以视为单位向量的缩放，因此此结论仍成立。

Duality: Loosely speaking, duality refers to situations where you have a natural-but-surprising correspondence between two types of mathematical thing.
<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/linear-algebra/duality.png"/></div>
一个向量的对偶是由他定义的线性变换，一个多维空间到一维空间的线性变换的对偶是多维空间中某个特定的向量，

Q: 为什么两向量的点积（即两向量$\vec a,\vec b$对应的坐标相乘之后相加，所得结果和一个向量$\vec a$($\vec b$)在另一向量上$\vec b$($\vec a$)投影长度，与$\vec b$($\vec a$)长度相乘，可以联系起来？
A: ?

两个向量点乘，就是将一个向量(两者之一)转换为线性变换。


### 叉积
- Cross product
以二维空间为例，两向量${\vec v}, \vec w$的叉积，记为${\vec v}\times{\vec w}$。两向量的叉积，数值上等于这两个向量组成的平行四边形的面积，同时等于这两个向量
$$\vec v=
\begin{bmatrix}
v_x\\
v_y\\
\end{bmatrix}
$$
与
$$\vec w=
\begin{bmatrix}
w_x\\
w_y\\
\end{bmatrix}
$$
组成的矩阵
$$\vec w=
\begin{bmatrix}
v_x & w_x\\
v_y & w_y\\
\end{bmatrix}
$$
(也可写成
$$\vec w=
\begin{bmatrix}
v_x & v_y\\
w_x & w_y\\
\end{bmatrix}
$$,对结果无影响
)
的行列式。
叉积得到的结果不是一个数字，而是一个向量，该向量的大小为平行四边形的面积，方向垂直于该平行四边形。(右手法则确定叉积的方向)
<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/linear-algebra/cross_product_right_hand_rule.jpg"/></div>


# Calculate Transfromation/Matrix with Matlab
```matlab
det(A)
```

# Quote
- The purpose of computation is insight, not numbers.--Richard Hamming
- To ask the right question is harder than to answer it.


# Todo

- [ ] 高斯消元法

# Other
- Origin of 3Blue1Brown: When I started the channel, I knew that I wanted the logo to be a loose depiction of my right eye color: sectoral heterochromia, 3/4 blue 1/4 part brown. It was a way of putting a genetic signature on my work, and the channel is all about seeing math in certain ways. The name, of course, is just derived from the logo.

<div align="center"><img width="300" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/3b1b.jpg"/></div>

# Refs

- [3Blue1Brown--Official website](https://www.3blue1brown.com/)
- [Linear Algebra系列教程--3Blue1Brown](https://www.bilibili.com/video/av6731067?p=1)
- [线性代数--Matlab](https://ww2.mathworks.cn/help/matlab/linear-algebra.html?s_tid=CRUX_lftnav)
- [Art of Problem Solving](https://artofproblemsolving.com/company)
- [行列式--Wiki](https://zh.wikipedia.org/wiki/%E8%A1%8C%E5%88%97%E5%BC%8F)

