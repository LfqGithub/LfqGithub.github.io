# 使用Python不同版本

在使用python中，不可避免需要在python2和python3之间切换。需要我们在编程和配置环境时考虑到这一因素

1. package的安装。利用[pip分别给python2和python3分别安装package](pip.md)方法安装package
2. 在代码首行添加`#!python2`和`#!python3`来设置该脚本通过`python2/3`来运行
3. 更加复杂的情况，如不同python程序需要不同版本的package，则使用虚拟环境来单独操作
