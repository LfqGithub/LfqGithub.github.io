---
layout: wiki
title: Sed/Awk
---

# Sed
stream editor

to be done

## Basic Functions

```bash
sed 's/^ *//g' file.txt # 去除行首空格 
sed 's/^[[:space:]]*//'  file.txt # 去除行首制表符
```

## Learn Basic Sed by Examples

```bash
$ cat my-pet.txt
This is my cat
my cat's name is betty
This is my dog
my dog's name is frank
This is my fish
my fish's name is george
This is my goat
my goat's name is adam
# 将处理过的内容输出，如果希望直接将改动保存到文件，使用 -i 参数
$ sed "s/my/yundongxiaoyang's/g" my-pet.txt # 单引号和双引号都可以，但是单引号内无法添加特殊字符，双引号可以, 如'， 还可以添加转义字符，如\/
This is yundongxiaoyang's cat
yundongxiaoyang's cat's name is betty
This is yundongxiaoyang's dog
yundongxiaoyang's dog's name is frank
This is yundongxiaoyang's fish
yundongxiaoyang's fish's name is george
This is yundongxiaoyang's goat
yundongxiaoyang's goat's name is adam
# 一些常用操作
$ sed 's/^/#/g' my-pet.txt  # 行首添加一个#
```

# AWK

AWK,  Alfred Aho，Peter Weinberger, and Brian Kernighan, updating...

## todo 

- `shownode`添加表头

# Links

- [awk-coolshell](https://coolshell.cn/articles/9070.html)
- [添加表头](http://www.cnblogs.com/276815076/archive/2012/03/23/2414077.html)


## Links

- [sed official manual](http://www.gnu.org/software/sed/manual/sed.html)
- [sed-coolshell](https://coolshell.cn/articles/9104.html)

