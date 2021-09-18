---
layout: other
title: EIS
keywords: 
categories: [EIS, Battery]
use_math: true
description: EIS for Li-ion Battery
---


交流阻抗谱学习, updating...

# Circuit Element
- 直流电源电阻：电能转化为热能
- 直流电源电容：电能和磁场能的相互转换
- 直流电源电容：电势能和电场能的相互转换
<div align="center"><img width="400" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/other/common_electrical_elements.PNG"/></div>

# Deviation
电阻是表征电子元器件(circuit element)对电流阻碍作用的物理量，常见的欧姆定律(Ohm's Law)定义电阻为电压和电流的比值$R=E/I$。
该公式仅适用于一种电路元件——理想电阻，理想电阻有以下特征
- 在全部电压和电流范围内符合欧姆定律
- 电阻值和频率无关
- 在电阻两端施加交流电时，电阻和电压无相位差

然而，现实世界中的电路元件展现出的特性远比纯电阻的特征复杂（很少有元器件可以适用以上三个特征）。这时，需要用一个更普适的概念描述电子元器件对于电流的阻碍作用。这个概念就是阻抗。
阻抗衡量电路元件对电流阻碍时，不受上述三个特征限制。

电化学阻抗的测量方法为：对cell系统施加一个小的刺激信号——正弦交流电压信号(AC potential)，之后测量对应的电流信号。阻抗为刺激电压除以响应电流。
cell系统的的电流响应是伪/准线性的(pseudo-linear)，对于一个线性/准线性的系统，对刺激电压的响应——响应电流通常和电压同为正弦，且频率相等，但和电压会在相位上产生差异(shifted in phase)。

<div align="center"><img width="400" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/other/shifted_in_phase.PNG"/></div>

施加的交流电压这一刺激信号可以表示为: 

$E_t=E_0 sin(\omega t)$

$E_t$是在时间$t$时的电压，$E_0$是信号的幅度，$\omega$是角频率(radial frequency, 角频率和频率(单位：赫兹 Hz)的关系为$\omega=2\pi f$)。
在线性/准线性系统中，响应电流$I_t$会产生相移$\phi$，且幅度变为$I_0$, 响应电流为

$I_t=I_0 sin(\omega t + \phi)$

阻抗的定义和欧姆定律相似

$Z=\frac{E_t}{I_t}=\frac{E_0 sin(\omega t)}{I_0 sin(\omega t + \phi)}=Z_0 \frac{sin(\omega t)}{sin(\omega t + \phi)}$

阻抗因此包含阻抗的幅度$Z_0$和相移$\phi_0$。
将刺激信号和响应信号绘制在$X-Y$坐标系中，我们可以得到利萨茹曲线(Lissajous Figure)

<div align="center"><img width="400" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/other/lissajous_figure.PNG"/></div>


根据欧拉公式(Eulers relationship)

$\exp(i\phi)=cos\phi + i sin\phi$

将刺激信号表示为

$E_t=E_0 sin(i\omega t)$

对应的响应信号为

$I_t=I_0 sin(i\omega t -\phi)$

阻抗可以表示为一个复数

$Z(\omega)=\frac{E}{I}=Z_0 \exp(i\phi)=Z_0\exp(cos\phi+i\sin\phi)$


# EIS Data Presentation

可以将复数形式的阻抗$Z_0$中实部作为$X$轴，虚部作为$Y$轴，就得到了Nyquist Plot （奈奎斯特图）, 注意Nyquist Plot中Y轴为负值，Nyquist Plot中，每一点对应一个频率，

<div align="center"><img width="400" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/other/Nyquist_figure.PNG"/></div>

在Nyquist Plot中，每一个起点为原点坐标，终点为曲线上一点的矢量，都对应一个频率下的阻抗($Z(\omega)$)。矢量的和$X$轴的夹角为相位角(phase angle)。
Nyquist plot的缺点在于无法从图像中看出对应的频率。


# Linearity of Electrochemical System
线性系统：If $x_1\rightarrow y1, x_2\rightarrow y2$, then $x_1+x_2 \rightarrow y_1+y_2,  ax_1\rightarrow ay_1$。

<div align="center"><img width="400" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/other/pseudo-linearity.PNG"/></div>


# Double layer capacitor

>>[Wiki](https://zh.wikipedia.org/wiki/双电层电容器):双电层电容器原理：插入电解质溶液中的金属电极表面与液面两侧会出现符号相反的过剩电荷，从而使相间产生电位差。那么，如果在电解液中同时插入两个电极，并在其间施加一个小于电解质溶液分解电压的电压，这时电解液中的正、负离子在电场的作用下会迅速向两极运动，并分别在两上电极的表面形成紧密的电荷层，即双电层，它所形成的双电层和传统电容器中的电介质在电场作用下产生的极化电荷相似，从而产生电容效应，紧密的双电层近似于平板电容器，但是，由于紧密的电荷层间距比普通电容器电荷层间的距离更小得多，因而具有比普通电容器更大的容量。双电层电容器没有传统的电介质,而是使用绝缘体隔开。这个绝缘层可以让电解液中的正负离子通过。该电解液本身不能传导电子。所以当充电结束后，电容器内部不会发生漏电（电子不会从一极流向另外一极）。当放电的时候，电极上的电子通过外部电路从一极流向另外一极。结果是电极与电解液中的离子吸附显著降低。从而使电解液中的正负离子重新均匀分布开来。
双电层电容器具有远高于电池的功率密度。
因此，虽然现有的双电层电容器的能量密度是传统电池的1/10，但其功率密度是后者的10至100倍。它们适用于电化学电池（持续的能量释放），静电电容器 （瞬间能量释放）之间的应用 

<div align="center"><img width="400" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/other/dlc.png"/></div>

# Diffusion
Diffusion also can create an impedance called a Warburg impedance.
# Constant Phase Element
Capacitors in EIS experiments often do not behave ideally. Instead, they act like a constant phase element as defined below.

<div align="center"><img width="300" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/other/cpe.PNG"/></div>

>>Admimittance=1/impedance




# Refs
- [Gamry Basic of EIS](https://www.gamry.com/application-notes/EIS/basics-of-electrochemical-impedance-spectroscopy/)
