---
layout: post
title: Fourier Transform
use_math: true
categories: Math 
---

Signal Analysis

## todo 

- Fourier Transform 介绍
- 二维傅里叶变换的旋转不变性证明
- python旋转图像->将图像和实验中的多晶光散射图像（散射环）完全对应

## Fourier Transform

示意图：

<div align="center"><img width="500" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/math/ftw-schematic.gif"/></div>




## 1D

```python
{% include /codes/math/fftw/fftw-schematic-one-d.py %}
```

### sine-wave

<div align="right"><img width="600" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/_includes/codes/math/fftw/output-fftw-schematic-one-d-sin.png"/></div>

for time domain and frequency domain
- two $\omega$, $\omega_1=2, \omega_2=8$ 
- The corresponding periods are $T_1=\frac{2\pi}{\omega_1}=3.14, T_2=\frac{2\pi}{\omega_2}=0.785$
- The frequency of the peaks in fftw figure are $\nu_1=\frac{1}{T_1}=0.32, \nu_2=\frac{1}{T_2}=2.55$, respectively.
- The amplitudes are 0.5 and 1, repectively
- The coordinate range of frequency domian are (0,$\nu/2$)
  - Only half figure are shown in the figure, 500 points, each point represent $\nu/1000$


### squarewave

<div align="right"><img width="600" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/_includes/codes/math/fftw/output-fftw-schematic-one-d-square-wave.png"/></div>

>> 注意： 离散点的个数为偶数次是，使用`fft.shift`后，其直流分量并不位于中心处，此处会产生一定的偏差，当离散点数足够多时，该偏差可忽略。

## 2D

```python
{% include /codes/math/fftw/fftw-schematic-two-d.py %}
```

## 3D

to be added

>> 图片来源于网络，侵删

## Links

- [Understanding FFTW by examples](https://www.ritchievink.com/blog/2017/04/23/understanding-the-fourier-transform-by-example/)
- [FFT-python-zhihu](https://zhuanlan.zhihu.com/p/27880690)
- [fftw-wiki](https://zh.wikipedia.org/wiki/%E7%A6%BB%E6%95%A3%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2)
- [fft-matlab](http://cn.mathworks.com/help/matlab/ref/fft.html)
- [fft2-matlab](http://cn.mathworks.com/help/matlab/ref/fft2.html?lang=en)
- [二维傅里叶变换的旋转不变性](https://www.zhihu.com/question/57366686)
- [fftw](http://dsqiu.iteye.com/blog/1636299)
- [python旋转图像](http://blog.csdn.net/guduruyu/article/details/70842142)
