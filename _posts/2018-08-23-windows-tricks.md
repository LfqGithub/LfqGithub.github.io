---
layout: post
title: Work On Windows
categories: Windows
keywords: software
---

updating...

# CMD

Command Prompt 

# 基本命令
- `cd` 
- `dir`,相当于Linux中`ls`命令
- `ren`
- `rd`: 删除文件,相当于Linux中`rm`命令
- `cls`: 清屏
- `type`: 显示文件内容
- `md`: 建立子目录,相当于Linux中`mkdir`命令
- `move`: 改变文件名，移动文件，相当于Linux中`mv`命令
- `xcopy`: 加强版复制
- `help [command]`: 查看命令使用方法

# 硬件

## 切换声音播放设备
- 安装软件-[SoundSwitch](https://www.aaflalo.me/downloads/)
- 设置声音切换快捷键`Ctrl+Alt+F1`

# 系统安装

- 电脑同时安装Ubuntu 16.04/18.04 + Windows
  - 在Windows 10 xia安装Ubuntu 16.04/18.04后删除Ubuntu
    - UEFI 安装系统：Download [EasyUEFI](https://www.easyuefi.com/index-cn.html)
	- MBR 安装系统: [MBRFix](http://sysint.no/mbrfix/)
- 制作多系统安装U盘
  - 制作工具：[WinSetupFromUSD](http://www.winsetupfromusb.com/)

# 外设
## U盘容量变小
  - 问题原因：由于制作ubuntu镜像时， U盘被分成了多个区， 在win7下，U盘他只识别第一个区，因此2M实际上是ubuntu的引导区大小。
  - 解决办法：首先，管理员身份运行命令行（快捷键win+R），然后，diskpart回车 --->list disk回车然后，看看你的u盘是哪一个然后，select disk X 回车（X为你u盘的序号）然后，clean回车（以上操作步骤实际是取消u盘原有的分区，让他重新变成一个未分区的状态）然后，退出这个命令行。这时u盘的大小已经恢复了，但是u盘处于未分区状态。接着，我的电脑右键-->管理-->磁盘管理，然后选择你刚刚的那个U盘，右键，新建简单卷，大小自己分配。这个相当于重新分区，并且格式化。

-- 来自知乎用户--[沧浪的回答](https://www.zhihu.com/question/27888608)

# 软件

## Putty

### Putty免密登陆

- 快捷方式自动登录
  - 创建`Session`:填写`IP`，端口号
  - 创建`PuTTY`快捷方式,属性->快捷方式->目标，填写`X:\yourpath\putty.exe -load "session_name" -l "username" -pw "password"`  
- 密匙自动登录
  - 打开`PuTTYgen`后点击`generate`，点击进度条下空白区域生成密匙。
  - `Save private key`保存私匙到文件`mykey.ppk`
  - 将公钥保存在linux主机上
    ```bash
    $ mkdir ~/.ssh
    $ vi ~/.ssh/authorized_keys
    # 输入PuTTYgen生成的公钥
    ```
  - `PuTTY`中`Connection/SSH/Auth`选项卡，在`Private key file for authentication`中填入私匙地址（`X:\mykey.ppk`）。
- 修改快捷方式
  - 新建`PuTTY`快捷方式，属性>快捷方式>目标，添加`X:\yourpath\putty.exe -i "X:\mykey.ppk" username@IP`  

## Xming

- windows电脑显示远程主机的图像
  - 使用[Xming](https://sourceforge.net/projects/xming/)+[Putty](http://www.putty.org/)显示图像。  
    - Putty 设置方法
      - 选中`SSH`-`x11`-`Enable X11 forwarding`
      - `X display location`中填`localhost:0`
      - 选中`MIT-Magic-Cookie-1`。
- 多主机间跳转后显示图像
  - 问题
    - windows 电脑A登陆linux主机B,然后登陆linux主机C后无法显示主机C的图像
  - 解决
    - 在主机C的`~/.bashrc`中添加`export DISPLAY=ip_A:0.0`

## Stickies
- 便签工具，可在同一用户登录的不同windows电脑间同步
- 可通过快捷键操作
  - `Ctrl+Shift+L`:切换项目符号，在该项目前添加/取消项目符号
  - `Ctrl+H`: 便签列表
  - `Ctrl+D`: 删除笔记
  - `Ctrl+N`: 新建笔记
  - `Ctrl(+Shift)+Tab`: 切换上下窗口

- [下载地址](https://www.zhornsoftware.co.uk/stickies/download.html)

## Sumatra PDF
- PDF阅读器，开源、轻量、快速、免费、渲染清晰
- [下载地址](https://www.sumatrapdfreader.org/free-pdf-reader.html)
  - 优点:可通过快捷键操作
  - 缺点:无法编辑、标注pdf文件

## Wise System Monitor
- 系统资源(cpu利用率、温度、网速、内存利用率)监视软件
- [下载地址](https://www.wisecleaner.com/wise-system-monitor.html)
  - 优点：可悬浮最前、外观简洁清晰
  - 缺点：显示内容较少

# Links

- [Remove Ubuntu-uefi](https://blog.csdn.net/tulip561/article/details/73929482)
- [Remove Ubuntu-mbr](https://blog.csdn.net/Meditator_hkx/article/details/52626077)
- [热键切换windows声音输出](http://www.howtoip.com/how-to-switch-windows-sound-outputs-with-a-hotkey/)
- [login with putty](https://segmentfault.com/a/1190000000639516)
