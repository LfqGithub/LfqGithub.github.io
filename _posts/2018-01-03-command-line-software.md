---
layout: post
title: Linux Command Line
categories: [Linux]
keywords: tig, cppman, cheat, nload, ag, screenfetch, doctoc
description: software, command line
---

Updating......

# 命令行快捷方式

## 移动光标

- `Ctrl + B`: 前移一个字符(backward)
- `Ctrl + F`: 后移一个字符(forward)
- `Alt + B`: 前移一个单词
- `Alt + F`: 后移一个单词
- `Ctrl + A`: 移到行首 (a: first letter in amphabet)
- `Ctrl + E`: 移到行尾 (end)

## 交换

- `Esc + T`: 交换光标前两个参数 (单词) 位置
- `Ctrl + T`: 交换光标前两个字符位置

## 删除

>>删除为剪切, 剪切后可用 `Ctrl + y` 粘贴剪切内容

- `Alt + D`: 删除当前光标到临近右边单词开始 (delete)
- `Ctrl + W`: 删除当前光标到临近左边单词结束 (word)
- `Ctrl + H`: 删除光标前一个字符（相当于 Backspace）
- `Ctrl + D`: 删除光标后一个字符（相当于 Delete）
- `Ctrl + U`: 删除光标左边所有（相当于长按 Backspace 键）
- `Ctrl + K`: 删除光标右边所有（相当于长按 Del 键）
- `Ctrl + L`: 清屏

## 任务
- `Ctrl + C`: 结束任务
- `Ctrl + Z`: 挂起, `fg/bg` 将程序调到前台/放回后台

## 命令
- `!!`: 上一条命令全部内容/执行上一条命令
- `!$`: 上一条命令最后一个参数，同`Alt + .`
- `!!:n`: 上条命令的第`n`个参数
- `!!:^`: 上条命令的第1个参数
- `!!:$`: 上条命令的最后1个参数，同`!$`
- `!string:n`: 最近执行过的以`string`开头的命令的第`n`个参数
- `!$:p`: 打印上一条命令最后一个参数
- `!*`: 上一条命令所有参数
- `!*:p`: 打印上一条命令所有参数
- `!xxx`: 执行最近的以`xxx`开头的命令
- `!xxx:p`: 打印最近的以`xxx`开头的命令
- `^xxx`: 删除上一条命令的第一个`xxx`并执行
- `^xxx^yyy`: 将上一条命令的第一个`xxx`替换成`yyy`并执行
- `^xxx^yyy^`: 将上一条命令的所有的`xxx`替换成`yyy`并执行

## 其它

- `Ctrl + N`: 下一条命令
- `Ctrl + P`: 上一条命令
- `Ctrl + R`: 进入历史查找命令记录， 输入关键字。 多次按返回下一个匹配项
- `Ctrl + S`: 锁定终端
- `Ctrl + Q`: 解锁终端
- `Ctrl + I`: 自动补全，相当于 Tab
- `Ctrl + J/O`: 相当于 Enter



# 命令行软件

## 常用命令
- 查看文件夹下文件及文件夹大小
  - 查看当前目录文件夹大小：`du -h --max-depth=1`
  - 查看当前目录文件夹及文件大小：`ls -lh`

## doctoc

[doctoc](https://github.com/thlorenz/doctoc)用于自动生成markdown目录。


## tmux
- install
  ```bash
    $ sudo apt instal tmux
	```
- config
   ```bash
   $ vi ~/.tmux.conf
	 set -g prefix 'C-b' #  default
	 bind r source-file ~/.tmux.conf \; display-message "Config reloaded" # 动态载入配置
	 # 这样<prefix>r就可以重新载入配置， 增量执行配置文件中的新内容。 
   # 如果配置未生效， 使用命令 tmux kill-server 强制关闭 tmux
   ```
- session usage
  - 启动
    ```bash
	  $ tmux # 启动一个新session
	  $ tmux new -s sessionName # 启动一个 sessionName 的新 session
	  $ tmux a -t avaiableSessionName # 启动一个已经存在的 session
	  ```
  - 查看
    ```bash
	  $ tmux ls 
    # or 
	  $ <prefix>s
	  ```
  - 关闭
    ```bash
	  $ tmux kill-session -t  sessionName
 	  ```
  - 退出并且保存
    ```bash
	  $ <prefix>d
	  ```
  - 回到原来的 session
    ```bash
	  $ tmux a #
	  ```

  - 切换
    ```bash
	  $ tmux ls # 显示当前 session
	  $ tmux a # 切换到 tmux 之前session
	  ```
- windows usage
  - 管理窗口 
    ```bash
    # 下列命令前需要加<prefix>
	  c 创建新窗口
	  w 列出所有窗口
	  % 垂直切分当前窗口
	  " 水平切分当前窗口
	  ```
  - 窗口切换
    ```bash
    # 下列命令前需要加<prefix>
	  h 向左切换
	  l 向右切换
	  j 向下切换
	  k 向上切换
	  ```
    
- 其他	
  - 拷贝粘贴
    - `<prefix>[` 进入拷贝模式
	  - `space` 开始拷贝
	  - `vim` 模式开始选中内容
	  - `Enter` 拷贝选中内容
	  - `]` 粘贴

- 参考内容
  - [简单介绍](http://harttle.land/2015/11/06/tmux-startup.html)

## tig
- install 
  ```bash
  $ sudo apt install git-core
  $ sudo apt install ncurses-dev
  # apt install
  $ sudo apt install tig
  # manual install
  $ git clone git://github.com/jonas/tig.git
  $ cd tig
  $ make 
  $ make install 
  ```
- usage
  ```bash
  # git repos dir
  $ tig
  ```
## cppman 
- function: manual for c++ 98/11/14/ 
- usage: 
  ```bash
  $ cppman  std::count
  ```
## cheat 
- function: show the man page of software in an intuitive way 
- usage:
  ```bash
  $ cheat tar
  ```
- nload
- function: show the speed of internet
- usage: 
  ```bash
  $ nload
  ```
## ag
- function: search string
- install
  ```bash
  $ sudo apt install silversearcher-ag
  ```
- usage:
  ```bash
  $ ag 'searchtext'
  ```
## screenfetch
- function: show the information of system and hardware
- install 
  ```bash
  $ git clone git://github.com/KittyKatt/screenFetch.git screenfetch
  $ cd screenfetch 
  $ chmod +x screenfetch-dev
  ```
- usage
  ```bash
  $ screenfetch-dev
  ```

<div align="center"><img width="400" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/wsl_info.png"/></div>

## axel 
- function: multi-thread download  
- usage
  ```bash
  $ axel -n 20 https:xxx
  ```

# Refs

- [Bash Shell 命令行操作快捷键](https://zhuanlan.zhihu.com/p/27232200)
- [bash技巧--重点在博文评论](http://roclinux.cn/?p=1582)
