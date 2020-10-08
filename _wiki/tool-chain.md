---
layout: wiki
title: Tool chain
keywords: tool, chains
categories: [tool]
description: Word/Life Procedure
---

Updating......

# Tools

- Windows 端
  - [Putty](https://www.putty.org/)
  - [Xming](https://sourceforge.net/projects/xming/files/)
  - Matlab: 图像处理、数据分析
  - MS Office
    - PPT
	- OneNote
  - [Shadowsocks](https://github.com/shadowsocks/shadowsocks-windows): 科学上网
  - Endnote: 文献管理
- Linux ( Ubuntu ) 端
  - Python
    - argparse: 参数解析
    - matplotlib: 绘制图像
	- numpy, scipy...: 数值计算
  - Evince: pdf 阅读器(Linux)
  - [sumatraPDF](https://www.sumatrapdfreader.org/free-pdf-reader.html): pdf 阅读器(Windows)
  - ImagicMagick: 图片查看/编辑器/格式转换
  - Latex
    - Tikz: 绘制流程图
	- Beamer: 演讲材料
	- Latexmk: 自动编译工具
  - Dot: 流程图
  - Graphviz
  - Pandoc: 格式转换
- 外部工具支持
  - github.com
  - gitee.com
  - bitbucket.com
  - vultr.com
  - google.com
  - 坚果云网盘

# Target

- 寻找最优解
  - 质量与速度的最优解
- 满足强迫症
- 优化工作流程
- 未来工作方向

## 阅读

### 将网页内容发送到kindle中阅读

- 使用[EpubPress](https://epub.press/)工具将网页内容转换为`epub`g格式文档，之后在`WSL`中使用`pandoc`命令将`epub`文档转换为`mobi`格式，之后使用kindle认证的邮箱将该文档发送到kindle账户，kindle同步后即可阅读

