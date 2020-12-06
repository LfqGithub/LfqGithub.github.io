---
layout: wiki
title: Vim
categories: Vim 
keywords: vim, linux
description: Vim 学习
---


Updating...

- [ ] 待整理


# Vim History

- `vi`： visual, 具体来源见book: Vim 使用技巧， 2ed, 第五章，命令行模式 
- `vim`: vi improved


# Vim words
- `v`: `:global` 和 `:vglobal`, 中`v`含义为 invert, 表反转
- `y`: yank
- `d`: delete, 相当于其他系统中的剪切cut
- `p`: put, 相当于其他系统中的粘贴



# 命令行模式下各符号含义
- `.`: 当前行
- `%`: 所有行
- `$`：最后一行
- `s`: substitute, 替代
- `t`: 相当于`copy`, 可以理解为copy to

# 使用场景
- 将第 n 行复制到第 m 行下面：`:ntm`
- 用`//`注释第 n 到 第 m 行：`:n, m :normal i //`

# 撤销
- `Ctrl + R`: 撤销前一步操作
# 移动

- `gj/gk`: 按照屏幕行向下/上，即如果一行太长，占据多行的空间，此命令可以在屏幕中的实际行，而非文件的实际行中移动。
- `w/W`: 移动到下一个字符/字串的开头
- `e/E`: 移动到上一个字符/字串的结尾
字符和字串的区别，可以简单记忆：字串比单词更长. 举例来说，对于语句： e.g. we're going to slow. 如果我们需要改成 e.g., you're going to slow.
如果现在光标在第一个语句开头的e字符上，我们可以用命令`wwww`移动到字符`w`上，然后用`cwyou<ESC>`完成修改。如果使用字串移动，我们只需要用`Wcwyou<Esc>`就可以完成。
如果我们想修改 you're 为 it's, 用`cWit's`/`daWit's`就比用`cw<Esc>xxxit's`简单的多。

# 选择
对于配对符号中的内容，如`<>, {}, [], (),<a></a>, <xml></xml>`以及反引号`` ` ``自身等，可以用简单的命令选择符号中的内容。
`vi>`或者`vi<`可以选择`<>`符号中的内容，不包含符号，而`va>`或者`va<`则可以选择包括配对符号在内的内容。此操作可以选择多行。
可记忆为`vi>`为inside content, 而`va>`为all content.
注意其中`at/it`用来选择`<xml></xml>`/`<a></a>`中内容。

作为组合命令，我们可以用`yit`复制配对符号中的内容，`dit`删除配对符号中的内容，`yat`, `dat`同理， 此逻辑可以用来解释`daw`为什么可以删除当前光标所在的单词。

## i and a
>> 可以将`i`解释成 inside, `a`解释成all. 一般`d` motion 配合`a`, `c`motion 配合`i`比较合理。

- `iw/aw`: 当前单词/当前单词及一个空格
- `iW/aW`: 当前字串/当前字串及一个空格
- `is/as`: 当前句子/当前句子及一个空格
- `ip/ap`: 当前段落/当前段落及一个空行

- todo: vim如何定义一个段落？



# 缓存区
- `:write` 将当前缓存区内容写到磁盘, `:wall`保存所有缓存到磁盘
- `:edit!` 丢弃当前缓存区
# 多文件编辑
- `:e{dit} file1 file2, file{n}`: 打开多个文件
- `vim file1, file2, file{n}`: 一次打开多个文件
- `bn/bp`: 打开下/上一个文件
- `b{num}`: 切换至第 n 个文件

e.g., you are 


# 多窗口编辑
- `:sp{lit}`: 水平切分当前窗口
- `:vsp{lit}`: 垂直切分当前窗口
- `:clo{se}`: 关闭当前窗口
- `:on{ly}`: 关闭除活动窗口外的其他窗口

# 多标签编辑
- `:tabedit`: 打开新的标签
- `:tabedit filename`: 新的标签页打开文件 filename
- `:clo{se}`:关闭当前标签页
- `gt/gT`: 切换下/上一个标签页
- `{n}gt`: 跳转到第 n 个标签

# Netrw文件管理系统与分割窗口协同工作
- `:E`: 打开工程目录树(project drawer), 类似于GUI编辑器的文件管理器, 在该管理器中可以使用vim的语法选择文件，Enter后就可以直接打开文件。
- `Ctrl + Shift + 6`, 即`Ctrl + ^`, 在正在编辑的文件和工作目录树之间切换



# 查找定位
- `f{char}`: 正常查找
- `F{char}`: 反向查找字符`{char}`
- `;`: 正向查找，跳转到下一个匹配项，如`f{char}`匹配该行第一个`{char}`字符，`;`跳转到下一个匹配的`{char}`字符。
- `,`: 和`;`相反，反向查找匹配项

# 组合
- `d/ge`: 删除到ge字符出现的位置前, 注意字符串ge并不会被删除, 此命令可跨行操作

# 标记
- `:marks`: 显示所有mark
- `:delmarks a b c`: 删除mark
- `:delmarks!`: 删除所有mark
- `m{mark}`: 用选定的字母{mark}标记当前光标所在位置，其中小写字母仅在当前缓冲区可见，大写字母全局可见(如正在编辑file1, 可以跳转file2的标记A)。
- ```{mark}``: 命令跳转到标记的行和列
- `'{mark}`: 跳转到标记行行首

# 跳转

跳转指大范围移动，近距离的移动，如`jkhl`, 不计入跳转。
- `Ctrl + o`: 回到跳转前
- `Ctrl + i`: 回到跳转后

# 寄存器
- `"add`: 将删除的该行内容放入到寄存器a中
- `"ap`: 将寄存器a中内容复制到该位置
- 特殊寄存器
  - `""`: 无名寄存器，复制y、删除d/c/x等操作都放入该寄存器，该寄存器内容很容易被覆盖。
  - `"0`: 复制专用寄存器，只有复制的内容才会放入该寄存器，寄存器中内容直到下一次复制被覆盖，其他操作，如`dd`， 只影响无名寄存器，不影响复制专用寄存器。

# 宏

- `q{char}`: 开始录制名为`{char}`的宏， 录制结束后以`q`结束。
- `@{char}`: 回放名为`{char}`的宏, `@@`回放最近调用的宏



now: trick 31


- `q:`进入命令行区，可看到历史命令，该区域为vim缓存区，可使用vim语法进行编辑后执行。
# 自动补全

- `Ctrl + p`: 调出自动补全, 继续点击该命令选择前一个候选词
- `Ctrl + n`: 选择下一个自动补全候选项
- `Ctrl + e`: 还原最早输入的文本，即从自动补全中退出






# Syntax

## Vim 复制

- `ytx`:  yanks upto x from current cursor position (before the character)
- `yTx`:  same as ytx, but in reverse direction 
- `yfx`:  yanks upto x from current cursor position (include the character)
- `yFx`:  same as yfx, but in reverse direction
- `y2fx`:  yanks upto the 2nd occurance of x 


## Vim 寄存器

### 用法
```bash
# vim normal mode
# check current register
:reg
# use register
"ap # 粘贴寄存器"a 内容
"ay # 将内容复制到寄存器"a 中
"+p # 将系统剪切板中内容粘贴到该处
"+y # 复制到系统剪切板
```

### 9 registers

- unnamed register, 缓存最后一次操作内容
  - `""`
- numbered register， 复制与删除有区别
  - `"0`:缓存最近一次复制内容
  - `"1`-`"9`: 缓存最近9次删除内容
- 行内删除寄存器，缓存行内删除内容
  - `"-`
- named register，指定后可用
  - `"a`-`"z`
  - `"A`-`"Z`
- read-only register
  - `":`: 最近命令
  - `".`: 最近插入文本
  - `"%`: 当前文件名
  - `"#`: 当前交替文件名
- expression register, read-only, 用于执行表达式命令
- 选择与拖曳register: 与外部应用交互，前提是系统剪切板可用
  - `"*`
  - `"+` 
  - `"~`
- black hole register
  - `"_`: 不缓存操作内容
- 模式寄存器，缓存最近的搜索内容
  - `"/`

## 查找替换

### 查找
```bash
/  # normal模式下，进入查找模式
/xxx ---> n/N 查找下/上一个
/vim$ # 匹配行尾vim
/xxx\c  # 对大小写不敏感查找
/xxx\C  # 对大小写敏感查找
```

- `~/.vimrc`设置
	```bash
	# 设置默认进行大小写不敏感查找
	set ignorecase
	# 如果有一个大写字母，则切换到大小写敏感查找
	set smartcase
	```

- 查找快捷键
```bash
*  # 查找当前光标所在单词
```

### 替换
```bash
:s # substitute，用来查找和替换体祖传
```

`:{作用范围}s/{目标}/{替换}/{替换标志}`,如`:%s/foo/boor/g`: 在全局范围`%`查找`foo`并且替换为`bar`, 所有出现都会被替代`g`(`global`)

`:s/foo/bar/g`：替换当前行所有出现

`5,12s/foo/bar/g`：替换5-11行中所有出现

`.,+2s/foo/bar/g`:替换当前行及接下来两行

`:%s/foo/bar/`: 替换全局每行第一次出现

`:^s/foo/bar/i`: 对大小写不敏感替换

`:^s/foo/bar/I`: 对大小写敏感替换

`:%s/foo/bar/gc`: 每次替换需要确认(confirm)

- .vimrc 替换设置
	```bash
	highlight Search ctermbg=yellow ctermfg=black 
	highlight IncSearch ctermbg=black ctermfg=yellow 
	highlight MatchParen cterm=underline ctermbg=NONE ctermfg=NONE
	# 上述配置指定 Search 结果的前景色（foreground）为黑色，背景色（background）为灰色； 渐进搜索的前景色为黑色，背景色为黄色；光标处的字符加下划线。
	:nohighlight
	# 禁止搜索高亮
	# 当光标一段时间保持不动了，就禁用高亮
	autocmd cursorhold * set nohlsearch
	# 当输入查找命令时，再启用高亮
	noremap n :set hlsearch<cr>n
	noremap N :set hlsearch<cr>N
	noremap / :set hlsearch<cr>/
	noremap ? :set hlsearch<cr>?
	noremap * *:set hlsearch<cr>
	# 让Vim查找/替换后一段时间自动取消高亮，发生查找时自动开启
	
	```

## Spelling Check

- Config
  - add `set spell` to your `~/.vimrc`  
- Usage
  - `]s`: 下一个拼写错误  
  - `[s`: 上一个拼写错误  
  - `z=`: 拼写纠正建议  
  - `zg`: 忽略该单词，添加到用户正确词典  
  - `zG`: 忽略该单词，添加到用户正确词典（关闭`vim`后失效）  

## Auto-completion

- 自带补全功能  
  `ctrl + n/p`: 向后/前搜索关键字补全  
- 自动补全插件  
  - `youcompleteme`  


## Commands

- 删除行尾空格
  - `:%s/\s\+$//g`: 
    - `\s`: 匹配任何空白字符, 包含`[\f\n\r\t\v]`
	- `+`匹配之前的表达式一次或者多次
  - `:%s/^ *//g`
- 删除行首空格
  - `:%s/^\+\s//g`:

## Input

- `U/u`: 将选定的字母变成大/小写  
- `guu/Vu`: 将一行文字全变成小写  
- `gu/Vu`: 将一行文字全变成小写   
- `*/#`: 在当前文件中搜索当前光标的单词  
- `>>/<<`: 向右/左缩进当前行   
- `=`: 缩进当前行（自动对齐缩进）  
- `A`: input at the end of line

## Modify

### Numbers

- `Ctrl + A`: number, add 1 (`n->n+1`)
- `Ctrl + X`: number, minus 1 (`n->n-1`)
- `m + Ctrl + A/X`: add/minus n (`n->n+/-m`)

### Case Switch

- `U/u`: 将字符变成大写/小写
- `~`: 改变大小写

#### Examples

- `gggUG`: 全文变成大写
  - `gg`: 定位到文件第一个字符,`g`: global
  - `gU`: 将选定范围全部大写
  - `G`: 到文件末
- `3~`: 改变当前位置后三个字符大小写
- `guw/gue`: 将光标下单词小写
- `gUw/gUe`: 将光标下单词大写
- `gU5w/gU5e`: 将5单词大写
- `gu0/gU0`: 从光标位置到行首变成小/大写
- `gu$/gU$`: 从光标位置到行尾变成小/大写

## Cancel

- `u`: 撤销
- `ctrl + r`: 取消撤销


## Tag

- `normal mode`，`mx`在当前光标位置建立一个`mark`
- `'x`跳转到`x`标签
- 小写`mark`只在当前文件有效，大写`mark`全局有效。

## 多文件编辑

```bash
vi a.cc b.py c.hs d.md   # :bn 下一个 :bp 上一个 :q关闭当前文件  :qa 关闭所有文件
#查看当前缓存区（buffer)中打开的文件
:ls  # 执行之后出现打开的文件列表
:b x # 执行:ls 后，该命令打开第x个缓存区文件 b在该处代表buffer
:bn bp blast bfirst #打开下一个，上一个，最后一个，第一个缓存区文件
#当前文件在:ls 后显示内容中有符号%a标记
```

## 查看当前目录文件

```bash
:e    # 查看当前目录文件，jk可以选择文件打开。关闭文件查看窗口 
:q    # 关闭当前查看文件分屏
:Ve   # 在左边新建一个分屏并且查看当前目录中文件
:He   #在下边窗口查看当前目录文件
```


## 分屏及tab浏览
-分屏
  ```bash
   #打开文件之前分屏
  vi -O2 file1 file2 #在两屏中垂直分屏打开两个文件
  vi -o2 file1 file2 #在两屏中水平分屏打开两个文件
  #打开文件之后分屏
  :vsplit      #垂直分成两栏,并且在另一屏幕中打开现有文件
  :vsplit a.cc #垂直分成两栏并且打开文件a.cc
  #关闭分屏
  :q   #关t 当前分屏
  :qa  #关闭所有分屏
  #切换分屏
  ctrl +w hljk #切换左右上下分屏
  ctrl +w HLJK #调整左右上下分屏位置
  :set scb  #在两个分屏中输入该命令，可以同步滚动两个分屏中内容
  :set scb! #取消分屏同步滚动
  ```
- Tab浏览文件
  和分屏不同，很多人喜欢类似于谷歌浏览器的多tab浏览方式（比如我）
  ```bash
  vi -p a.cc b.cc c.cc d.cc # 多标签打开多个文件
  :Te  # Texplorer 的简称
  :gt  # 命令行执行该命令跳转到下一个tab
  :gT  # 命令行执行该命令跳转到前一个tab
  : x gt # 跳转到第x个tab
  :tabs # 查看所有tabs
  :tabclose x # 关闭第x个tab
  : bufdo tab split #将buffer中文件全部转换成tab
  ```

## quickfix

在vim中修改好文件并且编译，出现错误后，我们可以用`quickfix`功能快速定位及解决错误。

```bash
:cw # 将错误显示到vim的分屏中
:cp # 跳转到上一个错误
:cn # 跳转到下一个错误
:cl # 列出所有错误
:cc # 显示错误详细信息
```

## 保存会话
当我们打开了很多文件，并且在文件中保存了各种同步，滚屏，多屏等，如果想关机，下次开机，这些配置还要重新做，非常繁琐。用vim的保存会话功能，可以解放这部分工作。

```bash
:mksession ~/.mysession.vim #保存会话
:mksession! ~/.mysession.vim #强制保存会话
```



# 功能实现
## 查看字符出现次数
`:m,ns/string/&/gn`: 查看第m到n行字符串`string`出现的次数

# 插件

进一步提高vim 编辑器效率

## Vundle

```bash
$ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim # install vundle
$ vi ~/.vimrc 
set nocompatible  
filetype off     
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

# Plugins
Plugin 'vim-latex/vim-latex' 

call vundle#end()  
filetype plugin indent on
```
vim normal 模式下

```bash
:PluginInstall # install new plugins
:PluginClean   # clean removed plugins
```


## Plugins for Vim

### Normal Plugins 

```.vimrc
Plugin 'gmarik/Vundle.vim'
Plugin 'Lokaltog/vim-powerline' "美化状态栏
let g:Powerline_colorscheme='solarized256'
Plugin 'luochen1990/rainbow' " 彩虹括号
let g:rainbow_active = 1 "0 if you want to enable it later via :RainbowToggle
```

### [VimCompleteMe](https://github.com/ajh17/VimCompletesMe)
- Install
  - `git clone git://github.com/ajh17/VimCompletesMe.git ~/.vim/pack/vendor/start/VimCompletesMe`
  - add `autocmd FileType vim let b:vcm_tab_complete = 'vim'` to `~/.vimrc`

### YouCompleteMe
- 臃肿，可以用`VimCompleteMe`替换
- Install

```bash
$ vi ~/.vimrc # add
Plugin 'Valloric/YouCompleteMe'
# 命令行模式下
:PluginInstall
# 等待
The ycmd server SHUT DOWN (restart with ':YcmRestartServer'). YCM core library not detected; you need to compile YCM before using it.
$ sudo apt install cmake build-essential python-dev  # python3-dev if you use python3
cd ~/.vim/bundle/YouCompleteMe
# python2 install.py --clang-completer  # for python2
$ python3 install.py --clang-completer  # for python3
```

## Plugins for Languages

### vim-latex
#### Install
```bash
$ vi ~/.vimrc
Plugin 'vim-latex/vim-latex' 
let g:Tex_Folding=0 "禁用代码折叠
"let g:Tex_FoldedEnvironments =''
"let g:Tex_FoldedSections = ''
```
#### Config
#### function
- 模板
  - 新建模板

  文件夹`.vim/bundle/vim-latex/ftplugin/latex-suite/templates`中， 复制其他文件并修改，如

  ```tex
  <+	+>	!comp!	!exe!
  %        File: !comp!expand("%")!comp!
  %     Created: !comp!strftime("%a %b %d %I:00 %p %Y ").substitute(strftime('%Z'), '\<\(\w\)\(\w*\)\>\(\W\|$\)', '\1', 'g')!comp!
  % Last Change: !comp!strftime("%a %b %d %I:00 %p %Y ").substitute(strftime('%Z'), '\<\(\w\)\(\w*\)\>\(\W\|$\)', '\1', 'g')!comp!
  %
  \documentclass[tikz]{standalone}  
  \usepackage{tikz}
  \usepgflibrary{shapes.geometric} 
  \begin{document}
  \begin{tikzpicture}[scale=1]
  <++>
  \end{tikzpicture}
  \end{document}
  ```

  - Usage
    - vim, open tex file, on command mode  
    - `:TTemplate`选择自己需要的模板
	- 制作一个硬链接到`~/gitRepos/config/vim-latex-template`文件夹的同名文件中，方便备份保存

# Configuration

## WSL vimrc
<script src="https://gist.github.com/LfqGithub/85d53000197302236d5beade0b873d8d.js"></script>


# Links

- [install youcompleteme](http://www.bijishequ.com/detail/564645?p=)
- [在 Vim 中优雅地查找和替换](http://harttle.com/2016/08/08/vim-search-in-file.html)
- [vim-kuanghy](https://wiki.archlinux.org/index.php/Vim_%28%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%29#.E6.8B.BC.E5.86.99.E6.A3.80.E6.9F.A5)
- [Copy, cut and paste of Vim](https://vim.fandom.com/wiki/Copy,_cut_and_paste)
- [Advanced commands of Vim](https://gist.github.com/fakemelvynkim/9546331)
