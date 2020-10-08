---
layout: wiki
title: Latex 
categories: Latex
description: learn latex
keywords: latex, beamer, tikz
---



# Syntax

## 批注

- 使用`pdfcomment`宏包动态显示批注内容-[link](https://stackoverflow.com/questions/3696128/latex-tag-for-making-a-comment-appear-or-disappear-in-pdf)
```latex
\usepackage{pdfcomment}
\pdfcommentsetup{draft} % set to 'final' to prevent all comments from showing up
\pdfcommentsetup{color={1.0 1.0 0.0}, open=true}
```

## 附录 

- Appendix figure 单独编号

```latex

% add to preamble
\usepackage[toc,page]{appendix} % 添加附录
\usepackage{chngcntr} % 附录内的图片单独编号

% text
\begin{appendices}
\counterwithin{figure}{section}
  \section{Appendix_content}
  \input{appendix/11-tilings}
\end{appendices}

% or 
\appendix
\section{appendix1}
\input{appendix1}
\section{appendix2}
\input{appendix2}
% 附录以A,B编号, 附录中图像图像对应编号为Figure A.1, B.2
```

## 表格

```latex
% \usepackage{table}
% \usepackage{}
%\usepackage{multirow}
%\usepackage{diagbox} % 斜线表头
\begin{table}
  \centering
  \scalebox{0.8}{
\begin{tabular}{l | c c}
  %\centering
  \rowcolor[gray]{.6}
  \multicolumn{3}{c}{example table} \\
  \rowcolor[gray]{.6}
  \diagbox{$f_{rod}$}{structure}{$\beta$}      & 1      & 2  \\
  \rowcolor[gray]{.9}
\end{tabular}
\end{table}

% 一列放置两个表格
\begin{table}[!htb]
\caption{Global caption}
\begin{minipage}{.5\linewidth}
\caption{}
\centering
\begin{tabular}{ll}
1 & 2
\end{tabular}
\end{minipage}%
\begin{minipage}{.5\linewidth}
\centering
\caption{}
\begin{tabular}{ll}
3 & 4
\end{tabular}
\end{minipage} 
\end{table}
%%%%%%%%%%%%%%%%%
```

## 图像

- Multi-Figure
  使用subfig宏包
```latex
% \usepackage{subfig}
\begin{frame}
\frametitle{欧几里得镶嵌}
  \begin{figure}[htb]
	\captionsetup[subfigure]{labelformat=empty}
	\centering
	\subfloat[$3^6$(p6m)]{
	  \includegraphics[height=.2\textheight,keepaspectratio]{images/tile/3_6.pdf}}\hfill
	\subfloat[$4^4$(p4m)]{
	  \includegraphics[height=.2\textheight,keepaspectratio]{images/tile/4_4.pdf}}\hfill
	\subfloat[$6^3$(p6m)]{
	  \includegraphics[height=.2\textheight,keepaspectratio]{images/tile/6_3.pdf}}\hfill

	\subfloat[$(3.6)^2$(p6m)]{
	  \includegraphics[height=.2\textheight]{images/tile/3_6_3_6.pdf}}\hfill
	\subfloat[$3.12^2$(p6m)]{
	  \includegraphics[height=.2\textheight]{images/tile/3_12_12.pdf}}\hfill
	\subfloat[$3.4.6.4$(p6m)]{
	  \includegraphics[height=.2\textheight]{images/tile/3_4_6_4.pdf}}\hfill
	\subfloat[$4.6.12$(p6m)]{
	  \includegraphics[height=.2\textheight]{images/tile/4_6_12.pdf}}\hfill

	\subfloat[$4.8^2$(p4m)]{
	  \includegraphics[height=.2\textheight]{images/tile/4_8_8.pdf}}\hfill
	\subfloat[$3^2.4.3.4$(p4g)]{
	  \includegraphics[height=.2\textheight]{images/tile/3_3_4_3_4.pdf}}\hfill
	\subfloat[$3^3.4^2$(cmm)]{
	  \includegraphics[height=.2\textheight]{images/tile/3_3_3_4_4.pdf}}\hfill
	\subfloat[$3^4.6$(p6)]{
	  \includegraphics[height=.2\textheight]{images/tile/3_3_3_3_6.pdf}}\hfill
	\end{figure}
\end{frame}
```

## 待办事项

```latex
% add to pre.tex
\newcommand{\todo}{ \item[\color{red}$\bigcirc$] }
\newcommand{\done}{\item[\color{blue}\sout{$\bigcirc$}] }

% usage
\begin{itemize}
	\todo xxx
	\done yyy
\end{itemize}
```


## 注释

```latex 
% 1. 注释一行文字
% contents
% 2. 注释一段文字

iffalse
   ...
fi

% 3. verbatim宏包注释文字 

\begin{comment}
	...
\end{comment}
```

## 多文件编写

类似于`C++`中包含其他头文件，latex写大型文档时，将文档分成多个文件编写可以带来很多便利。latex中实现该功能有两种方法。
- input
  ```latex
  \input{filename} % 不带后缀名.tex
  ```
  - 特点
    - 文本替换功能，相当于将被包含文件的内容直接复制到当前位置。
    - 任何被包含的文件有改动都需要全文重新编译。

- include
  ```latex
  \include{filename} % 不带后缀名.tex
  ```
  - 每次`include`都会另起一页
  - 修改后，其他文件不用重新编译。
  - 如果只想在生成的文件中显示部分章节，不需要注释对应的`\include{filename}`，只需要在导言区修改`\includeonly{filename1, filename2, filename4}`,
	这样只会显示一, 二, 四节，第三节不显示, 但是显示编号不会空过章节三。
  
## 代码高亮

```latex
\documentclass{article} 
\usepackage{xcolor} % 代码高亮
\usepackage{listings} % 专用于代码排版
% 全局代码高亮设置
\lstset{
numbers=left,  % 在代码左侧添加行号
numberstyle=\tiny, % 行号的字号
stepnumber=2, % 行号的步长
showspaces=false, % 是否显示空格
showstringspaces=false,  % 字符串中显示空格
showtabs=false,  % 显示
breaklines=tr,  % 自动断行
breakatwhitespace=false, % 断行只在空格处
keywordstyle=\color{blue!70},
commentstyle=\color{red!50!green!50!blue!50},
frame=shadowbox,
rulesepcolor= \color{red!20!green!20!blue!20},
escapeinside=`` % 输入中文时添加符号`
}

\begin{document} 
c \\
\begin{lstlisting}[language=c] 
int main(int argc, char ** argv) 
{ 
/* print a string "hello world!" */
printf("Hello world! `你好，世界！`\n"); 
return 0; 
} 
\end{lstlisting} 
c with frame \\
 % 有了全局设置，下面的语句后面一坨就不用写了
\begin{lstlisting}[language={[ANSI]c},keywordstyle=\color{blue!70},commentstyle=\color{red!50!green!50!blue!50},frame=shadowbox, rulesepcolor=\color{red!20!green!20!blue!20}]
int main(int argc, char ** argv)
{
printf("Hello world! \n");
return 0;
}
\end{lstlisting}

Python \\
\begin{lstlisting}[language=Python]
import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=np.sqrt(x)
fig,ax=plt.subplots()
ax.plot(x,y)
\end{lstlisting}
\end{document}
```

### minted
- 依赖python包 pygment.
- 编译: `xelatex -shell-escape file.tex`

```latex
\usepackage{minted}
%  shell 命令
\begin{minted}{shell-session}
python poststring.py resultdir x
\end{minted}
%  shell 语句
\begin{minted}{shell}
	for k in {1..5}
	do
	echo $k
	done
\end{minted}
```

## 参考文献
```latex
\usepackage[super,square,numbers,sort&compress]{natbib} % 上标，加中括号，编号，将8，9，10改为8-10
```
### 格式
```latex
@article{article,
author  = {Peter Adams}, 
title   = {The title of the work},
journal = {The name of the journal},
year    = 1993,
number  = 2,
pages   = {201-213},
month   = 7,
note    = {An optional note}, 
volume  = 4
}
```

## 其他功能

### 禁止图像浮动
```latex
\usepackage{placeins}
\FloatBarrier
```

# Tikz

TiKZ绘图着眼于定性的图表，定量数据的演示不是TiKZ所擅长的（？）

## Basic Function

### 简单图像

### 流程图

```latex
\documentclass[xcolor=svgnames]{beamer}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows} % 后面的椭圆等形状
\usepackage{smartdiagram}
\begin{document}
\frame{
	\frametitle{flow chart}
	\tikzstyle{decision} = [diamond,draw,fill=blue!15,text width=6em,text badly centered, node distance=3cm,inner sep=0pt]
	\tikzstyle{block} = [rectangle,draw,fill=blue!15,text width=5em,text centered, rounded corners, minimum height=3em]
	\tikzstyle{line} = [draw, =latex']
	\tikzstyle{cloud} = [draw, ellipse,fill=red!20,node distance=3cm,minimum height=2em]
	\begin{tikzpicture}[node distance=2cm, auto]
		% place node
		\node [block] (init) {initialize model};
		\node [cloud, left of = init] (expert) {expert};
		\node [cloud,right of =init] (system) {system};
		\node [block,below of =init] (identify) {identify candicate models};
		\node [block,below of =identify] (evaluate) {evaluate candidate models};
		\node [block, left of =evaluate, node distance =3cm] (update) {update model};
		\node [decision,below of =evaluate] (decide) {is best candidate better?};
		\node [block,right of =decide,node distance=4cm] (stop) {stop};

		%draw edges
		\path [line] (init) -- (identify);
		\path [line] (identify) -- (evaluate);
		\path [line] (evaluate) -- (decide);
		\path [line] (decide) -| node [near start] {yes} (update);
		\path [line] (update) |- (identify);
		\path [line] (decide) --node {no}(stop);
		\path [line,dashed] (expert) --(init);
		\path [line,dashed] (system) --(init);
		\path [line,dashed] (system) |-(evaluate);
	\end{tikzpicture}
}
\end{document}
```


```latex
\documentclass[border=10pt]{standalone}
\usepackage{smartdiagram}

\begin{document}
\frame{
	\smartdiagram[flow diagram:horizontal]{Edit,\LaTeX, Bib\TeX/ biber, make\-index, \LaTeX}	
}
\end{document}
```

## 基本语法

```latex
\input{pre}
\begin{document}
%\begin{tikzpicture}
% 一条直线
\begin{minipage}[c]{.6\textwidth}
\begin{lstlisting}
	\begin{tikzpicture}
		\draw (0,0) -- (1,1);
	\end{tikzpicture}
\end{lstlisting}
\end{minipage}
\begin{minipage}[c]{.4\textwidth}
	\centering
	\begin{tikzpicture}
		\draw (0,0) -- (1,1);
	\end{tikzpicture}
\end{minipage}
\begin{minipage}[c]{.6\textwidth}
\begin{lstlisting}
\tikz \draw (0,0) -- (1,1);
\end{lstlisting}
\end{minipage}
\begin{minipage}[c]{.4\textwidth}
	\centering
	\tikz \draw (0,0) -- (1,1);
\end{minipage}

\begin{minipage}[c]{.6\textwidth}
	\begin{lstlisting}
\begin{tikzpicture}
	\draw [color=blue!50, ->](0,0) node[left]{$A$}-- node [color=red!70,pos=0.25,above,sloped]{Hello}(1,1) node[right]{$B$};
\end{tikzpicture}
	\end{lstlisting}
\end{minipage}

\begin{minipage}[c]{.3\textwidth}
  	\centering
		\begin{tikzpicture}
			\draw [color=blue!50, ->](0,0) node[left]{$A$}-- node [color=red!70,pos=0.25,above,sloped]{Hello}(3,3) node[right]{$B$};
		\end{tikzpicture}
\end{minipage}
\begin{tikzpicture}
	\draw (0,0) circle (10pt);
	\draw (0,0) .. controls (1,1) and (2,1) .. (2,0);
	\draw (0,0) ellipse (20pt and 10pt);
	\draw (0,0) rectangle (0.5,0.5);
	\filldraw[fill=green!20!white, draw=green!50!black](0,0) -- (3mm,0mm) arc (0:30:3mm) -- cycle;
\end{tikzpicture}
\begin{tikzpicture}

```latex
% 独立tikz图像
\documentclass[tikz]{standalone}  % 该语句自动调用tikz， 不用添加\usepackage{tikz}
% 文档中tikz图像
\documentclass[UTF8]{ctexart} % 中文支持
\usepackage{tikz}
\usepgflibrary{shapes.geometric} % 一些额外的形状，如cylinder
\begin{document}
\begin{tikzpicture}
  \foreach \a in {3,...,7}{
	  \draw[red, dashed] (\a*2,0) circle(0.5cm);
	  \node[regular polygon, regular polygon sides=\a, draw,
	  inner sep=0.3535cm] at (\a*2,0) {};
	}
\end{tikzpicture}
\end{document}
```


## 基本形状
```latex
\documentclass[tikz]{standalone}
\usepgflibrary{shapes.geometric}
\begin{document}

\begin{tikzpicture}
  \foreach \a in {3,...,12}{
	  \draw[red, dashed] (\a*2,0) circle(0.5cm);
	  \node[regular polygon, regular polygon sides=\a, draw,
	  inner sep=0.3535cm] at (\a*2,0) {};
	}
\end{tikzpicture}

\begin{tikzpicture}
  \foreach \a in {3,...,12}{
	\draw[blue, dashed] (\a*2,0) circle(0.5cm);
	\node[regular polygon, regular polygon sides=\a, minimum size=1cm, draw] at (\a*2,0) {};
  }
\end{tikzpicture}

\end{document}
```
<div align="center"><img height="30" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/tikz/basic_shape2-0.png"/></div>
<div align="center"><img height="30" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/tikz/basic_shape2-1.png"/></div>

## 自定义属性
```latex
\documentclass[tikz]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
[L1Node/.style={circle,   draw=blue!50, fill=blue!20, very thick, minimum size=10mm},
L2Node/.style={rectangle,draw=green!50,fill=green!20,very thick, minimum size=10mm}]
\node[L1Node] (n1) at (0, 0){$\int x dx$};
\node[L2Node] (n2) at (2, 0){$n!$};
\end{tikzpicture}
\end{document}
```

<div align="center"><img height="30" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/tikz/custom.png"/></div>

## 循环
```latex
\documentclass[tikz]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
[L1Node/.style={circle,   draw=blue!50, fill=blue!20, very thick, minimum size=10mm},
L2Node/.style={rectangle,draw=green!50,fill=green!20,very thick, minimum size=10mm}]
\foreach \x in {1,...,5}
\node[L1Node] (w1_\x) at (2*\x, 0){$\int_\Omega x_\x$};
\end{tikzpicture}
\end{document}
```

<div align="center"><img height="30" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/tikz/loop.png"/></div>

## 其他

- 将pdf转化为图片
  - 矢量图(github pages 暂不支持)
  ```bash
  $ sudo apt install pdf2svg
  $ pdf2svg <input.pdf> <output.svg> [<page no of pdf or "all">]
  ```



# Beamer

## 语法

### 导言区

```latex
\documentclass[compress]{beamer}\tiny % compress 压缩导航栏()
\usepackage[BoldFont,SlantFont,CJKchecksingle,CJKnumber]{xeCJK}  % 中文支持
\usepackage{amsmath}
\usepackage{bm} % 黑体矢量 $f(\bm{r})$
\usepackage{mathtools}
\usepackage{subfig} % 插入多图
\usepackage{color}
\usepackage{tikz,pgfplots,pgfplotstable} % for tikz picture
\usetikzlibrary{shapes.geometric}
\usetikzlibrary{decorations}
\setbeamertemplate{footline}[frame number]{} %添加页码
```

## 目录

```latex
\AtBeginPart{
  \frame{
    \frametitle{\partpage}
    \begin{multicols}{2}% 分栏显示
      \tableofcontents[pausesections] % 自动生成目录	
    \end{multicols}
  }  
}
```
## 脚注
Beamer中添加参考文献一般不适用bibtex，而是使用脚注。
```latex
% 普通脚注，全文排序
添加第一个脚注\footnote{content of footnote}
% 只针对当前frame中的脚注排序
添加第一个脚注\footnote[frame]{content of footnote}
```

# 其他

## vim-Latex plugin

- Install
	add `Plugin 'vim-latex/vim-latex' to `~/.vimrc' (vundle needed)
- templates使用
  - 插入pre
    `~/.vim/bundle/vim-latex/ftplugin/latex-suite/templates`中添加新的模版（可以复制原来的模版后修改）
    ```bash
    vi newtex.tex
    :TTemplate
    choose the right template
    ```
  - 插入参考文献
    ```bash
    BBB
    ```
- insert an environment
  ```bash
  figure  
  退出到normal模式
  F5
  ctrl + j 跳转到下一个输入位置
  ```
- 取消折叠代码
  ```bash
  let g:Tex_Folding=0
  or 
   "let g:Tex_FoldedEnvironments =''
   "let g:Tex_FoldedSections = ''
  ```

## Compile

### Command

### makefile
`makefile`示例

```bash
all:
	xelatex filename.tex
clean:
	rm -fr *.aux *.log *.snm *.toc *.nav *.out
cleanall:
	rm -fr *.aux *.log *.pdf  *.snm *.toc *.nav *.out
show:
	evince filename.pdf
```
### Latexmk

`latexmk`: Latex Automatic Compilation Tool. 自动编译latex文档，如多次编译，插入bib等，系统自动完成。检测到文件改动时自动重新编译, 配合evince软件可以起到实时预览的效果

>>使用前先设置配置文件(建议放在`~/.latexmkrc`)

`latexmkrc`示例
```bash
$ vi ~/.latexmkrc
$pdf_mode = 1;
$pdflatex = "xelatex -file-line-error -fdb_latexmk --shell-escape -src-specials -synctex=1 -interaction=nonstopmode %O %S;cp %D %R.pdf";
$recorder = 1;
#$pdf_previewer = "SumatraPDF -reuse-instance -inverse-search -a %O %S";
$pdf_previewer = "start evince %O %S";
#$pdf_previewer = "open -a %S";
#连续编译模式
$preview_continuous_mode = 1;
$pdf_update_method = 0;
$clean_ext = "synctex.gz acn acr alg aux bbl bcf blg brf fdb_latexmk glg glo gls idx ilg ind ist lof log lot out run.xml toc dvi ";
$bibtex_use = 2;
#$out_dir = "temp";
#指定生成PDF文件的文件名，可以与LaTeX主文件名不一致
#$jobname = "tem";
```

执行latexmk命令，并且将任务放入后台，不显示输出内容。 

```bash
$ vi makefile
all:
	nohup latexmk -xelatex -gg -silent -pvc -f result.tex & 
clean:
	rm -fr *.aux *.log *.snm *.toc *.nav *.out *.bbl *.blg *.fls *.fdb_latexmk
cleanall:
	rm -fr *.aux *.log *.pdf  *.snm *.toc *.nav *.out *.bbl *.blg
show:
	evince result.pdf
```

### Help

- `texdoc latex`调出latex教程
- `texdoc beamer`调出beamer教程

## 化学式

latex-chemfig

## 流程图: dot2tex

### Installation

```bash
$ sudo apt install dot2tex
```
### Syntax

```bash
$ vi example1.dot
digraph G {
	a_1 [texlbl="$\frac{\gamma}{2x^2+y^3}$"];
	a_1 -> a_2 -> a_3 -> a_1
	node [texmode="math"];
	a_1 -> b_1 -> b_2 -> a_3;
	b_1 [label="\\frac{\\gamma}{x^2}"];
	node [texmode="verbatim"]
	b_4 [label="\\beta"]
	a_3 -> b_4 -> a_1;
}
$ dot2tex example1.dot -tmath > example1.tex  # 可能会产生图像oversized node, 更好的方式为
$ dot2tex --preproc example1.dot | dot2tex > example1.tex 
$ xelatex example1.tex
$ evince example1.pdf
```
<div align="center"><img width="150" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/dot2tex/example1.png"/></div>

# Links
- [chemfig-wikibook](https://en.wikibooks.org/wiki/LaTeX/Chemical_Graphics)
- [manual](http://mirrors.concertpass.com/tex-archive/macros/generic/chemfig/chemfig-en.pdf)
- [Tikz Examples](http://texample.net/tikz/examples/smart-flowchart/)
- [The Not So Short Introduction to latex 2e](https://tobi.oetiker.ch/lshort/lshort.pdf)
- [LaTeX2e unofficial reference manual](http://mirrors.rit.edu/CTAN/info/latex2e-help-texinfo/latex2e.html)
- [LateX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
- [get rid of blank at the begin of each line](https://blog.csdn.net/shenhuxi_yu/article/details/53413499)
- [Bibtex Style Examples](https://verbosus.com/bibtex-style-examples.html)
- [使用latexmk自动编译LaTeX](http://www.ai7.org/blog/posts/latexmk.html)
- [Latexmk Official Site](http://mg.readthedocs.io/latexmk.html)
- [流程图](http://texample.net/tikz/examples/smart-flowchart/)
- [TiKZ入门教程](http://www.fuzihao.org/blog/2015/08/11/TikZ%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B/)
- [TiKZ绘图实例](http://www.texample.net/tikz/examples/all/)
- [A very minimal introduction to TiKZ](http://cremeronline.com/LaTeX/minimaltikz.pdf)
- [切问录](http://www.fuzihao.org/blog/2015/08/11/TikZ%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B/)
