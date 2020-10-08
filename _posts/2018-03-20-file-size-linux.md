---
layout: post
title: Disk Space Usage
categories: Linux 
keywords: du, file, linux, size, disk
---

Updating...... 

# du

- `du [-abcDhHklmsSx] [-l] [-X] [--block-size] [--exclude=...] [--max-depth=...] [--help] [--version] [dir or files]`
  - `-h`: `--human-readable`: 提高信息可读性
  - `-s`: `--summary`: 仅显示总计，即当前目录大小 
  - `--max-depth=n`: 深入到`n`层目录
  - `--exclude='*xyz'`: 排除含有`xyz`字符的目录
  - `-k/-m/-g`: 以`KB`,`MB`,`GB`为单位显示

# Frequently used commands 

- `du -s -h`: 显示当前目录所占磁盘空间(MB)
  
# df

- `df`: 显示硬盘使用情况
  - `-a`: 显示所有文件系统使用情况
  - `-k`: 以`k`字节显示

# fdisk

- `fdisk`: 划分磁盘分区


# todo 

Means of Each Parameters

# Links

- [linux file size](http://blog.csdn.net/ouyang_peng/article/details/10414499)
- [du/df/fdisk](http://os.51cto.com/art/201012/240726_all.htm)
