---
layout: wiki
title: Hardware
keywords: CPU 显示器 硬盘 电源
categories: [Hardware, CPU]
use_math: true
description: 浅显电脑硬件知识及自用硬件规格记录
---

Updating...

# 硬件监控

>>硬件监控在消耗系统资源的同时，有部分概率降低系统稳定性，所以尽量不要开机自动运行。

- TrafficMonitor, 可任务栏显示
  - CPU使用率
  - 下载/上传网速

- AIDA64, 付费版可显示
  - CPU/GPU温度
  - CPU/GPU风扇转速(比例)
  - CPU/GPU/内存占用率
  - CPU/GPU功耗
  - SSD温度、读写速度
  - 系统风扇转速

# 显示器
## 接口
不同分辨率显示器需要不同的带宽。以`8bit`色彩深度的`4k`显示器(3840\*2160)为例，如果想要达到基本的`60Hz`刷新率，每秒需要传输3840\*2160\*8\*3\*60=11943936000=11.9`Gbit`的信息。
因此传输带宽小于11.9`Gbit/s`的接口无法支持`4k`\*60`Hz`显示。现阶段常见的两种接口: HDMI (High Definition Multimedia Interface) 和 DP (Display Port) 不同版本对应的带宽
- HDMI 1.4: 10.2`Gbit/s`
- HDMI 2.0: 18.0`Gbit/s`
- HDMI 2.1: 48.0`Gbit/s`
- DP 1.2: 21.6`Gbit/s`
- DP 1.4: 32.4`Gbit/s`

可见对于`4k`分辨率的显示器，需要 DP 1.2 或 HDMI 2.0 及以上接口才可以满足60 `Hz`刷新率要求。
对于10`bit`色彩深度的`4k`显示器，带宽需求进一步增加到14.9`Gbit/s`.

## 尺寸与分辨率

### 16:9
<div align="center"><img width="800" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/hardware/16_9_ppi.png"/></div>
>>注： `16:10`显示器一般是在`16：9`显示器宽度上加`1/9`, 所以横向尺寸和横向分辨率相同的`16:9`和`16:10`显示器的`PPI`相同

### 21:9
<div align="center"><img width="800" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/hardware/21_9_ppi.png"/></div>
>>注： 厂家宣传`21:9`显示器时宣称的`2k`,`3k`(准`4k`),`5k`其实为`FHD+`,`2k+`,`4k+`。

### 像素数
<div align="center"><img width="800" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/hardware/pixels.png"/></div>

### 稀(奇)有(葩)分辨率

- Pro Display XDR: 32 inch, 6016\*3384, PPI: 216

## 带宽与分辨率
### Bit数
显示器的 bit 数代表每个颜色通道占用多少 bit 存储，如 8bit 代表 RGB 每个通道占用 8bit，三个通道占用 $8+8+8=24$ bit, 10 bit色深三个通道共占用 30 bit。每个通道能表示的色彩为$2^n$, 意味着三个通道同能表示 $2^{3n}$ 种色彩。
6/8/10 bit分别能显示262144（26万)/16777216(1.6million)/1073741824(1.07 billion)种颜色
- **4k**(3840$\*$2160)分辨率的最小带宽
  - 8位色彩深度: 3840$\*$2160$\*$24$\*$60/1024$^3$=11.12 Gbps
  - 10位色彩深度：3840$\*$2160$\*$30$\*$60/1024$^3$=13.9 Gbps
  - 因此 HDMI 1.4 版本(带宽10.2Gbps)无法支持4k$\*$60 Hz，而DP 1.2 版本（带宽21.6 Gbps)可以，且可以支持到 10 bit色彩深度。
- **5k**(5120$\*$2880)分辨率需要最小带宽
  - 8位色彩深度：5120$\*$2880$\*$24$\*$60/1024$^3$=19.78 Gbps
  - 10位色彩深度：5120$\*$2880$\*$30$\*$60/1024$^3$=24.72 Gbps
  - 因此 DP 1.2 无法支持5K$\*$10 bit$\*$60 Hz
- **8k**(7680$\*$4320)分辨率需要最小带宽
  - 8位色彩深度：7680$\*$4320$\*$24$\*$60/1024$^3$=44.49 Gbps
  - 10位色彩深度: 7680$\*$4320$\*$30$\*$60/1024$^3$=55.62 Gbps
  - 即使现阶段带宽最强的接口 DP 1.4（带宽32.4 Gbps）也无法满足`8k`的带宽需求，但是 DP 1.4 加入了显示压缩流技术（Display Stream Compression), 使得 DP 1.4可以支持8k$\*$60 Hz.
  - 未来的 HDMI 2.1（带宽48.0 Gbps)可以支持8k$\*$8 bit$\*$60 Hz，现阶段没有单接口支持8k$\*$10 bit$\*$60 Hz， 只能通过DP 1.4$\*$2，即使用两个DP 1.4接口同时接入显示器

## 边框宽度

### 显示器边框计算
显示器参数中的宽度和显示器面板宽度的差值/2为左右边框厚度(一般和上边框厚度相当)
- 计算方法
<script src="https://gist.github.com/LfqGithub/e6758691352a7f9e873478022e6f656e.js"></script>
- 常见显示器尺寸显示区域
  - 27 inches: Width 596.74mm Height 335.66 mm
  - 31.5 inches: Width xxx mm Height xxx mm
- 常见4k显示器的边框数据
  - Dell U3219q
  - Dell UP3218K
  - ViewSonic VX2780-4K-HD
  - LG 27UL850

# 主板

## 主板规格
- EE-ATX: 347mm x 330 mm 超微服务器主板
- E-ATX:305mm x 330mm
- ATX: 305mm x 244mm
- mATX: 244mm x 244mm
- mini-ITX:170mm x 170mm
- mini-STX: 147mm x 140mm
- Intel NUC: 102mm x 102mm
- 常见主板规格：微星B360m迫击炮--mATX
>> ATX: Advanced Technology eXtended, a motherboard and power supply configuration specification develop by Intel in 1995.

# 电源
## 电源规格
- AT/ATX: 160mm$\cdot$150mm$\cdot$86mm, 适用于ATX, Micro-ATX主板
- SFX: 125mm$\cdot$100mm$\cdot$63.5mm, 适用于Flex-ATX,Micro-ATX主板
- SFX-L: 125mm$\cdot$130mm$\cdot$63.5mm
- Flex: 81.5mm$\cdot$40.5mm$\cdot$150mm,又称1U电源，一般用于服务器中，现在也用在ITX机箱中
