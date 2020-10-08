---
layout: wiki
title: Shell
categories: Linux
description: learn shell
keywords: bash shell
---

## Background
### shell环境
- Bourne Shell (`/usr/bin/sh or /bin/sh`)
- Bourne Again Shell (`/bin/bash`)
- C Shell (`/usr/bin/csh`)
- K Shell (`/usr/bin/ksh`)
- Z Shell 

```bash
#!/bin/bash # 约定写法，告诉系统使用哪一种shell
```

## Syntax

### 变量
```bash
a="Hello, World!"
b=3
for file in `ls /etc` # or: for file in $(ls /etc)
	do
	echo file
	done
a.txt
b.cc
d.tex
myUrl=`www.google.com`
readonly myUrl # 只读变量
unset a # 删除变量
```

### 符号

#### `\`

- 倒引号(backticks),倒引号内的字符串会视为指令
```bash
$ _date=`date + %F`
$ echo $_date
2019-04-22
```

#### `()`

- 命令组， 括号中命令将会行楷一个子shell顺序执行，所以括号中的变量不能被脚本余下的部分使用。括号中多个命令间用分号隔开，最后一个命令没有分号，各命令和括号间不必有空格
- 命令替换，等同于`cmd`, shell扫描一遍命令行，发现`$(cmd)`结构后将将`cmd`执行一次，得到标准输出，将此输出放到原来的命令
- 初始化数组，如`Array=(a b c d); echo ${Array[@]}`

#### `$`

- 变量替换
- `$#`: 引用变量的总个数

#### `{}`

- 花括号, 帮助解释器识别变量的边界，简单变量外可加可不加，如`echo $foo` 等于`echo ${foo}`

### 字符串
#### 单引号和双引号包含字符串
空格再linux中是一个典型的分隔符，为了避免字符串中的空格造成歧义，就在字符串外加上了引号，以标记字符串的边界。分为单引号和双引号。
<script src="https://gist.github.com/e0ef279391e8d7882e1fcae41884d182.js"></script>


#### 拼接字符串 
```bash
$ str0='I am'
$ str1='yundongxiaoyang'
$ sayHello0=''$str0' '$str1''
$ sayHello1="$str0 $str1"
$ echo $sayHello0
$ echo $sayHello1
```

### 数组
<script src="https://gist.github.com/LfqGithub/ee58afa1ebfef0ffcbbc572bd05da898.js"></script>


### 运算
Bash不支持简单的数学运算，但可以通过其他命令实现，如`expr`
<script src="https://gist.github.com/97b5346ad8c8938ec9c2a785614a58a7.js"></script>



## Shell 具体功能实现

- Linux下批量替换多个文件中的字符串
  - ```bash
    sed -i "s/original_string/new_string/g" `grep original_string -rl dir_name`
  	```

## 常用命令

```bash
# 查看当前目录中的文件夹
$ ls -d */ 
$ tree -d # 需要安装 tree
$ ls -l |grep '^d' 
```

## 不常用命令
- `pgrep x`: 获取`x`进程的ID (process grep?)

### 命令解析
#### eval
<script src="https://gist.github.com/LfqGithub/f96a5b0c0aef777920c545ccb6a98ab3.js"></script>

## 快捷操作

### 历史记录自动补全

- CentOS 自带该功能，Ubuntu需要设置
- ```bash
  vi /etc/inputrc
  # uncomment the following lines
  "\e[5~": history-search-backward # pagedown 向后搜索历史命令 
  "\e[6~": history-search-forward # pageup 向前搜索历史命令 
  ```

## 参数

```shell
$ ./exe a b c d e f  #例
$0 : 即命令本身 ./exe
$n : 第n个参数, 1: a, 2:b
$# : 参数的个数，不包括命令本身，上例中$#为6
$@ : 参数本身的列表，也不包括命令本身，上例为a b c d e f
$* ：和$@相同，但"$*" 和 "$@"(加引号)并不同，"$*"将所有的参数解释成一个字符串，而"$@"是一个参数数组
```

## Shell 基本功能理解

### 输入输出

- 标准输入: `0`， `stdin`,`<`
- 标准输出：`1`,  `stdout`, `1>`
- 错误输出：`2`, `stderr`, `2>`

### 组合命令

```bash
command 1 ; command 2   # 顺序执行，即使前面的命令出现错误，也会继续执行接下来的命令
command 1 && command 2  # 顺序执行，前面的命令执行出现错误后，后面的命令不再执行
command 1 || command 2  # 遇到可以执行成功的命令，后面的命令就不再执行
command 1 | command 2   # 命令1的输出，作为命令2的输入（管道）
```

### 管道与重定向

```bash
$ ls -al >list.txt # 输出结果输入到list.txt, 若改文件存在，则覆盖原文件。
$ ls -al >>list.txt # 添加到文件后，不覆盖原文件
$ ls -al 1>list.txt 2>list.err # 正确输出到list.txt, 错误输出到list.err
$ ls -al 1> list.txt 2> &1 不论正确错误，都输出到list.txt中
```
- 管道
  - `|`: 将前一个命令正确执行后的输出信息，作为输入传送给下一个命令。  
  - 常用管道操作--grep
    ```bash
    grep [] 'content' file # 在文件中搜索符合条件的字符串，一般查找目录中某条记录时使用
    []: -i 忽略大小写
        -r # 递归
        -n # 输出行号
        -v # 反向查找
        --color=auto #搜索出的关键字用颜色显示
    ```
- 重定向
  - `>`: 将输出重定向到一个文件，覆盖原来的文件  
  - `>!`: 将输出重定向到一个文件，强制覆盖原来的文件  
  - `>>`: 将输出追加到文件  
  - `<`： 输入重定向到一个程序  
  - `cat a.cc >b.cc` ： 将`a.cc`内容保存到`b.cc`文件中。
  - `>/dev/null` : 重定向到该文件，相当于不输出。
 
# Bashrc
## wsl-homePC
<script src="https://gist.github.com/LfqGithub/7d51d569606b2ad318a2c44d3257dcfc.js"></script>

## Links

- [查看当前目录中文件夹](https://www.linuxquestions.org/questions/linux-newbie-8/ls-to-view-directories-only-156254/)
- [编程易犯的错误](http://kodango.com/bash-pitfalls-part-1)
