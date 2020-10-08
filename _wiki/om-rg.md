---
layout: post 
title: Operation and Maintenance in Fudan RG
categories: Linux
description: Operation and Maintenance in Fudan Research Group
keywords: Linux, compute, nodes
---

Done.

# 单Linux主机

## 系统安装
- 虽然未来准备租用的超算（天河二号）为 centOS 6, 但是 centOS 管理起来比较麻烦， 不推荐。  
- 建议使用 Ubuntu 系统（2017 年，最新的 Ubuntu LTS 版本为: [Ubuntu 16.04 LTS](http://www.ubuntu.org.cn/download/desktop))。  
- U盘制作安装盘 (使用软件 [Rufus](https://rufus.akeo.ie/) 制作), 系统安装方法和 windows 相似。 

## 网络设置 
- 化学楼采用的是 DHCP 自动分配 IP 地址，安装系统后会自动获取 IP， 学号认证后可以上外网。
- 如有需求，可以绑定IP和Mac地址
  ```bash
  $ ifconfig
  #本例中，em3 网口连接到网口， 因此只有 em3 有 IP， ether 对应的 44:a8:42:40:xx:xx 为硬件 (mac) 地址, 临时分配的 IP 地址为 inet 对应的 10.158.145.xx
  em3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
  inet 10.158.145.xx  netmask 255.255.255.0  broadcast 10.158.145.255
  inet6 fe80::46a8:42ff:fe40:9978  prefixlen 64  scopeid 0x20<link>
  inet6 2001:da8:8001:7315:46a8:42ff:fe40:9978  prefixlen 64  scopeid 0x0<global>
  ether 44:a8:42:40:xx:xx  txqueuelen 1000  (Ethernet)
  RX packets 32772736  bytes 46449523872 (43.2 GiB)
  RX errors 0  dropped 5807  overruns 0  frame 0
  TX packets 7382859  bytes 597449753 (569.7 MiB)
  TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
  device interrupt 138
  ```

## 用户管理

- 普通用户
```bash
$ sudo adduser userName # 添加账户
$ sudo deluser userName # 删除账户
$ sudo deluser --remove-home userName # 删除账户同时删除该用户 home 目录
```
- 超级用户(管理员) 
```bash
$ sudo vi /etc/sudoers
#在 root	ALL=(ALL:ALL) ALL 行下添加
userName ALL=(ALL:ALL) ALL
```

## 软件安装

- apt 安装
  - [apt](https://zh.wikipedia.org/wiki/%E9%AB%98%E7%BA%A7%E5%8C%85%E8%A3%85%E5%B7%A5%E5%85%B7)(Advanced Packaging Tools，高级打包工具)是一种软件包管理器，`Ubuntu`默认软件安装工具。
  - Usage
    ```bash
    $ sudo apt install software_name 
    ```
  - Python Packages
    ```bash
    $ sudo apt install python-tk python-matplotlib python-scipy python-configparser python-numpy 
    ```
  - 常用软件
  
    ```bash
    $ sudo apt install csh git lifftw3-dev lifftw3-doc openssh-client openssh-server vim
    ```
- 源码安装
所有软件建议统一安装在`/apps`中，每个软件建立相应的文件夹(如`matlab2017a`)。方便后续大家调用,另外，建议所有主机上的软件安装同一版本，方便管理。
  - FFTW3 
    - Ubuntu 可以使用`Apt`安装`fftw3-dev`， 安装后不用配置环境变量
    - 手动安装方法
      ```bash
      $ sudo mkdir /apps /apps/fftw3  ~/softwarePackages
      $ cd ~/softwarePackages
      $ wget http://www.fftw.org/fftw-3.3.7.tar.gz
      $ tar zxvf fftw-3.3.7.tar.gz
      $ cd fftw-3.3.7
      $ sudo ./configure --prefix=/apps/fftw3
      $ sudo make && make install
      $ vi ~/.bashrc  # 配置环境变量
      export C_INCLUDE_PATH=/apps/fftw3/include:$C_INCULDE_PATH
      export CPLUS_INCLUDE_PATH=/apps/fftw3/include:$C_INCULDE_PATH
      export LD_LIBRARY_PATH=/apps/fftw3/lib:$LD_LIBRARY_PATH
      export LIBRARY_PATH=/apps/fftw3/lib:$LIBRARY_PATH
      ```
  - Python
    - 使用系统`Python`
      - 直接安装常用`packages`即可
        - `Pip`
          ```bash
          $ sudo apt install python-pip  # install pip
          $ sudo python -m pip install python-package-name
          ```
    	- `Apt` 
    	  ```bash
    	  $ sudo apt install python+python-package-name
    	  ```
    - `Python`发行版
      - 推荐 [Anaconda发行版](https://www.anaconda.com/download/#linux)， 发行版中包含了常用的`packages`。  
  - Matlab 
    在复旦大学正版软件中下载 [matlab linux版](http://mvls.fudan.edu.cn/matlab/), 设置好`X11`转发后，Linux 版和 Windows 版安装方法几乎完全相同。   
    ```bash
    $ sudo apt install csh # matlab 需要 csh 支持   
    $ sudo  ./install # 输入key以及network.lic(参考复旦大学正版软件 Matlab 安装说明）, Matlab 安装位置为/apps/matlab2017a
    $ vi ~/.bashrc
    export C_INCLUDE_PATH=/usr/local/MATLAB/R2018a/extern/include/:$C_INCULDE_PATH # c
    export CPLUS_INCLUDE_PATH=/usr/local/MATLAB/R2018a/extern/include/:~/apps/cnpy/include/:$C_INCULDE_PATH # c++
    export PATH=/usr/local/MATLAB/R2018a/bin/:$PATH
    export LD_LIBRARY_PATH=/usr/local/MATLAB/R2018a/bin/glnxa64/:~/apps/cnpy/lib:$LD_LIBRARY_PATH
    export LIBRARY_PATH=/usr/local/MATLAB/R2018a/bin/glnxa64/:~/apps/cnpy/lib:$LIBRARY_PATH
    # 后两行会导致执行ssh命令时出现
    ssh: /usr/local/MATLAB/R2018a/bin/glnxa64/libcrypto.so.1.0.0: no version information available (required by ssh)
    ssh: /usr/local/MATLAB/R2018a/bin/glnxa64/libcrypto.so.1.0.0: no version information available (required by ssh)
    警告，想避免该警告，可以注释掉
    export LD_LIBRARY_PATH=/usr/local/MATLAB/R2018a/bin/glnxa64/:~/apps/cnpy/lib:$LD_LIBRARY_PATH
    export LIBRARY_PATH=/usr/local/MATLAB/R2018a/bin/glnxa64/:~/apps/cnpy/lib:$LIBRARY_PATH
    这两行，在g++命令后添加
  	-Wl,-rpath=/usr/local/MATLAB/R2018a/bin/glnxa64
    即平时不调用该动态链接库，只有在编译该程序时调用。
    ```

## BugFix

- 其他用户可以看到自己的文件  
  解决方法：更改主目录权限
    ```bash
	$ chmod -R o-rwx ~
	```
- 开机后桌面空白，无法打开`terminal`
  - `ctrl + alt + F1`： 进入命令行模式

- 计算任务繁重自动关机。
  - 主机供电不足
- `ssh`登陆警告
  - 问题
    - `ssh: /home/software_public/matlab2017a/bin/glnxa64/libcrypto.so.1.0.0: no version information available (required by ssh)`
  - 解决方法
    - 系统安装了其他非`Ubuntu`版本的`openssl`, 将`~/.bashrc`中的`matlab`相关的`library_path`去掉

# 计算机群

>目的：

- `n0`
  - 储存/管理用户名/用户文件
- `n1-nx`
  - 计算节点，共享`n0`主节点的软件、用户、文件

## 准备工作

- 保证`n0`主节点的稳定性/可靠性
  - 这里的`n0`使用`raid 1`的两硬盘做系统盘，`raid 5`的三块硬盘做存储盘，稳定性较子节点更高
- `n0-nx`之间确保低延迟的通信（彼此可`ping`通，通过`ssh`到彼此账户验证)
  - 通过交换机连接到主节点`n0`
    - 主节点连接到互联网，子节点通过交换机连接主节点
    - 子节点`nx`网络设置
      ```bash
      $ sudo vi /etc/network/interfaces # 设置网络
      auto eno1 # eno1 是接通交换机的网口名称，可用 ifconfig 命令查看(RUNNINNG的非 lo 网口对应于连通网络的网口)
      iface eno1 inet static
      address 192.168.1.x  
      gateway   192.168.1.251 # 主机内网 IP 地址
      dns-nameservers 202.120.224.26 # 复旦大学 DNS
      $ sudo /etc/init.d/networking restart # 重启网络服务
      ```
  - 不通过交换机连`n0`
    - 不设置网络，通过化学楼网络自动分配网址(该网址在相当长时间内一般不会改变)
  - `n0`与`nx`的`/etc/hosts`文件中都有彼此的`IP`地址和`hostname`，目的： 改`IP`登陆为`hostname`登陆(`ssh ip` to `ssh hostname`)

## 安装 NFS 服务

[NFS](https://zh.wikipedia.org/wiki/%E7%BD%91%E7%BB%9C%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F)(Network File System, 网络文件服务)是一种分布式文件系统协议，
允许客户端主机像访问本地存储一样访问服务器文件

- 共享文件夹
  - `/home/home_public`: 用户账户及文件
  - `/home/software_public` : 公用软件存放目录

### 设置 NFS 服务器

```bash
$ sudo apt install nfs-kernel-server
$ sudo vi /etc/idmapd.conf
Domain = tang3090 
$ sudo vi /etc/exports 
# 允许这些 IP 主机 mount 该磁盘 , 10.158.145.0 代表 ip 地址为 10.158.145.x 的ip地址都被允许
# 10.158.145.0: 化学楼 B3 层的 IP 网段, 192.168.1.0: 内网地址
/home/home_public 10.158.145.0/24(rw,no_root_squash)
/home/home_public 192.168.1.0/24(rw,no_root_squash)
/home/software_public 10.158.145.0/24(rw,no_root_squash)
/home/software_public 192.168.1.0/24(rw,no_root_squash)
$ sudo systemctl restart nfs-server
```

### 设置NFS 客户端

```bash
# 挂载硬盘
$ sudo mkdir /home/home_public /home/software_public
$ sudo apt install nfs-common
$ sudo vi /etc/idmapd.conf
Domain=tang3090
$ sudo mount -t nfs n0:/home/home_public /home/home_public
$ sudo mount -t nfs n0:/home/software_public /home/software_public
# 自动挂载
$ sudo apt install autofs
$ sudo umount /home/home_public 
$ sudo umount /home/software_public
$ sudo vi /etc/auto.master
/-    /etc/auto.mount
$ sudo vi /etc/auto.mount
/home/home_public -fstype=nfs,rw  n0:/home/home_public
/home/software_public -fstype=nfs,rw  n0:/home/software_public
$ sudo systemctl restart autofs
```

## 安装 NIS

[NIS](http://cn.linux.vbird.org/linux_server/0430nis.php)(Network Information Services, 又称Sun Yellow Pages)管理计算机群的账号和密码。

### 设置 NIS 服务器 

```bash
$ sudo apt install nis nfs-kernel-server
# enter the name of the domain: yang3084
$ sudo vi /etc/default/nis
NISSERVER=master
$ sudo vi /etc/ypserv.securenets
# 0.0.0.0 0.0.0.0
# add to the end: IP range you allow to access
 255.255.255.0   10.158.145.0
$ sudo vi /var/yp/Makefile
MERGE_PASSWD=true
MERGE_GROUP=true
$ sudo vi /etc/hosts
127.0.0.1       localhost
# add own IP address for NIS
 10.158.145.xx       tang3090     n0
$ sudo systemctl restart nis
# update NIS database
$ sudo /usr/lib/yp/ypinit -m
# add nis server (ctrl + D 结束输入)
```

### 设置 NIS 客户端 

```bash
$ sudo apt install nis
# 无网络链接时，可从其他节点拷贝 nis.deb 文件安装
$ sudo dpkg -i nis.deb
# enter nis domain
tang3090
#无法显示图像时，修改 /etc/defaultdomain，添加 domainName
$ sudo vi /etc/yp.conf
# ypserver ypserver.network.com
# add to the end: [domain name] [server] [NIS server's hostname] 
domain tang3090 server  n0
$ sudo vi /etc/nsswitch.conf
passwd:     compat nis     # line 7; add
group:     compat nis     # add
shadow:     compat nis     # add
hosts:     files dns nis     # add
$ sudo systemctl restart nis 
$ ypwhich # 安装成功后，该命令会输出domain name, 即这里的tang3090
# 重新登陆 
```

### NIS 账户管理
```bash
# on n0(NIS server)
$ sudo adduser newUser --home /home/home_public/newUser
# sudo userdel [-r] userName: 删除用户
$ cd /var/yp
$ sudo make
```

## BugFix
- `/etc/sudoers` syntax error
  - `pkexec visudo -f /etc/sudoers`
- 重启后`ypbind`无法通信
  - 硬盘没有挂载上
    - 检查硬盘没有`mount`上，`umount` 共享盘后重新`mount`下试试
    - `umount`硬盘一般卡死或者提示device is busy
    - 解决方法
  	  ```bash
  	  # sudo systemctl restart nfs`
  	  $ sudo umount -f -l /mounted/dir`
  	  $ sudo mount /the/dir/you/want/mount /mount/dir
  	  $ sudo systemctl restart nis
  	  $ ypwhich
  	  # if show the name of nis master, relogin
  	  ```
  - `ypbind`服务没有启动
    - 单个子节点`ypbind`没有启动，会导致只有该节点无法和`nis master`通讯，其他子节点正常
	- 解决方法-启动`ypbind`
	  ```
	  $ which ypbind
	  /usr/sbin/ypbind
	  $ sudo ./usr/sbin/ypbind
	  ```
	 
- 登陆其他节点后用户名显示错误
  - 原因：userid和其他用户重复
  - 解决：切换到其他有`sudo`权限的用户, `sudo usermod -u newUserID userName`
- `ssh`显示警告或无法登陆
  - 问题描述
    - `no version information available (required by ssh)`
  - 原因: 系统中安装了其他来源的openssl
  - 解决
    - `ldd /usr/bin/openssl`, 查看其他`openssl`依赖文件位置
	  ```bash
	  linux-vdso.so.1 =>  (0x00007fff911a1000)
	  libssl.so.1.0.0 => /lib/x86_64-linux-gnu/libssl.so.1.0.0 (0x00007fbf2c6e1000)
	  libcrypto.so.1.0.0 => /lib/x86_64-linux-gnu/libcrypto.so.1.0.0 (0x00007fbf2c29d000)
	  libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fbf2bed3000)
	  libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fbf2bccf000)
	  /lib64/ld-linux-x86-64.so.2 (0x0000555f5c585000)
	  ```
	- 注意`libssl`和`libcrypto`两个库，去除对应的两个文件


# 计算机群使用

## 免密码登陆
- 两独立主机间免密码登陆
  - 生成密钥： `ssh-keygen -t rsa`
  - 将登陆节点的公钥（`~/.ssh/id_rsa.pub`中内容）添加到被登陆节点`~/.ssh/authorized_keys`中 
  - 两台主机上互有对方的公钥时，`scp`拷贝文件时可以免密码且可以通过`tab`键提示文件信息。
- 对于搭建好的使用NIS管理用户的计算机群
  ```bash
  $ ssh-keygen -t rsa
  # default setting, just press Enter
  $ cat ~/.ssh/id_rsa.pub >>~/.ssh/authorized_keys
  ```

## Shell书签

- 文件夹“书签”-[bashmarks](https://github.com/huyng/bashmarks)

## 资源监控
- top
  - 显示内容
    - `%CPU`: cpu 使用率  
    - `%MEM`: 物理内存使用率  
    - `VIRT`: 虚拟内存使用率    
    - `RES`: 物理内存使用率   
    - `SHR`：共享内存使用率  
    - `SWAP`: 磁盘空间充当内存使用
    - `USED`: `Res`+`Swap`
    - `PR`: 优先级
    - `NI`: nice 值，越小优先级越高
    - `S`: 进程状态, `R`: 运行, `S`: 睡眠, `T`: 跟踪/停止， `Z`: 僵尸进程
    - `TIME+`： 进程运行时间，单位0.01秒
    - `TIME`： 进程运行时间，单位秒
    - `load average`: 系统负载,三个数值分别为 1, 5, 15 分钟前到现在的均值
  - 自定义显示内容
    - `f`: 修改显示内容, `Right`方向键选定，`Left`方向键解选定，上下移动显示选项位置，`Enter`保存当前设置，`q`退出当前页面（需要`W`保存到`~/.toprc`中，之后启动`top`才会生效）
    - `?`: 打开帮助信息
      ```bash
      Help for Interactive Commands - procps-ng version 3.3.10
      Window 1:Def: Cumulative mode Off.  System: Delay 3.0 secs; Secure mode Off.
      Z,B,E,e   Global: 'Z' colors; 'B' bold; 'E'/'e' summary/task memory scale
      e: 控制内存显示单位，在KB, MB, GB, TB, PB 切换
      l,t,m     Toggle Summary: 'l' load avg; 't' task/cpu stats; 'm' memory info
      0,1,2,3,I Toggle: '0' zeros; '1/2/3' cpus or numa node views; 'I' Irix mode
      f,F,X     Fields: 'f'/'F' add/remove/order/sort; 'X' increase fixed-width
      L,&,<,> . Locate: 'L'/'&' find/again; Move sort column: '<'/'>' left/right
      R,H,V,J . Toggle: 'R' Sort; 'H' Threads; 'V' Forest view; 'J' Num justify
      c,i,S,j . Toggle: 'c' Cmd name/line; 'i' Idle; 'S' Time; 'j' Str justify
      x,y     . Toggle highlights: 'x' sort field; 'y' running tasks
      z,b     . Toggle: 'z' color/mono; 'b' bold/reverse (only if 'x' or 'y')
      u,U,o,O . Filter by: 'u'/'U' effective/any user; 'o'/'O' other criteria
      n,#,^O  . Set: 'n'/'#' max tasks displayed; Show: Ctrl+'O' other filter(s)
      C,...   . Toggle scroll coordinates msg for: up,down,left,right,home,end
      k,r       Manipulate tasks: 'k' kill; 'r' renice
      d or s    Set update interval
      W,Y       Write configuration file 'W'; Inspect other output 'Y'
      q         Quit
      (commands shown with '.' require a visible task display window)
      ```
    - `W`: 保存当前更改到文件`~/.toprc`
  - 显示内容排序
    - `T`: 根据任务累计时间排序
    - `R`: 反向排序
  - cpu温度
    ```bash
    $ sudo apt install lm-sensors
    $ sudo sensors-detect
    $ sudo service kmod start
    $ sensors
    coretemp-isa-0002
    Adapter: ISA adapter
    Package id 2:  +32.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 0:        +24.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 1:        +22.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 2:        +27.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 3:        +27.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 4:        +29.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 5:        +30.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 6:        +26.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 7:        +30.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 8:        +30.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 9:        +27.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 10:       +30.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 11:       +28.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 12:       +33.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 13:       +26.0°C  (high = +73.0°C, crit = +83.0°C)
    Core 14:       +25.0°C  (high = +73.0°C, crit = +83.0°C)
    ```
- 实时网速
  ```bash
  $ sudo apt install nload
  $ nload # 上下方向键切换网卡
  ```

## 查看进程绝对路径

Linux启动进程后，会在`/proc`下创建一个以PID命名的文件夹，该文件夹下包含该进程的信息，其中名为`exe`的文件记录了绝对路径，可通过`ll`或`ls -l`命令查看


## 主机名 
```bash
sudo vi /etc/hostname
sudo vi /etc/hosts 
127.0.1.1 newhostname # 如果只修改 hostname 中主机名，会出现警告
```

## 登陆信息

- 默认登陆信息
  ```bash
  Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.10.0-42-generic x86_64)
  Documentation:  https://help.ubuntu.com
  Management:     https://landscape.canonical.com
  Support:        https://ubuntu.com/advantage
  0 packages can be updated.
  0 updates are security updates.
  Last login: Sun Dec 24 11:00:13 2017 from 10.158.145.68
  ```
- 修改登陆信息
  ```bash
  $ touch ~/.hushlogin # 关闭所有欢迎消息
  $ cd /etc/update-motd.d
  00-header  # Ubuntu 版本信息
  10-help-text   # 网址信息
  90-updates-available  # 可用更新信息
  ```

# Windows端

Windows端连接远程客户端相关操作

## Putty Title Bar

```bash
$ vi ~/.bashrc
USER=$(/usr/bin/id -un)
HOSTNAME=$(uname -n)
HOSTNAME=${HOSTNAME%%.*}
PROMPT_COMMAND='echo -ne "\e]0;$USER@${HOSTNAME}: $(pwd -P)\a"'
```

# 其他

## 天河二号超算使用方法
- 登陆
  - 打开代理
  - 登陆超算
- 文件传输
  - scp
  - rsync
- 安装/调用软件
  - `fftw`以及`matlab`, 在超算上都已经安装好，如果需要使用，需将下列内容添加到自己的`~/.bashrc`中
  ```bash
  export C_INCLUDE_PATH=/THFS/opt/fftw/3.3.6-pl1_share_mpi/include:/THFS/opt/matlab2016a/extern/include:$C_INCULDE_PATH # c
  export CPLUS_INCLUDE_PATH=/THFS/opt/fftw/3.3.6-pl1_share_mpi/include:/THFS/opt/matlab2016a/extern/include:/THFS/opt/gcc/5.2/lib64:$CPLUS_INCULDE_PATH # c++
  export PATH=/THFS/opt/matlab2016a/bin:/THFS/opt/gcc/5.2/bin:/THFS/opt/python3.6/bin:$PATH
  export LD_LIBRARY_PATH=/THFS/opt/fftw/3.3.6-pl1_share_mpi/lib:/THFS/opt/matlab2016a/bin/glnxa64:/THFS/opt/gcc/5.2/lib64:$LD_LIBRARY_PATH
  export LIBRARY_PATH=/THFS/opt/fftw/3.3.6-pl1_share_mpi/lib:/THFS/opt/matlab2016a/bin/glnxa64:/THFS/opt/gcc/5.2/lib64:$LIBRARY_PATH
  ```
  - python主要的package，如`numpy, matplotlib`等已经安装好，如果有其他需要，可以联系客服帮助安装，也可以自己安装其他发行版，如`Anaconda`。
- 程序提交
  - 单任务提交
    ```bash
    $ yhrun -p gscomp ./scfRigid Para.ini
    ```
  - 分配资源后提交
  - 脚本提交
    - 单节点多任务提交
      ```bash
      $ yhbatch -p gscomp -N 1 run.sh 
      # run.sh 
      $ vi run.sh
      #!/bin/bash
      yhrun -N 1 -n 1 作业名1 &
      yhrun -N 1 -n 1 作业名2 &
      yhrun -N 1 -n 1 作业名3 &
      ……
      yhrun -N 1 -n 1 作业名num &
      wait
      ```
    - 同一节点再次提交任务
      ```bash
      $ yhbatch -p gscomp -N 1 --jobid=123456 submit.sh 
      ```
    - 提交任务的同时修改任务名称
      ```bash
  	$ yhbatch -p gscomp -N 1 -J calcEnergy run.sh 
  	```
- 常用命令
  - 通过JOBID查看任务所在路径
    ```bash
    $ yhcontrol show job JOBID
    ```
  - 查看任务输出
    ```bash
    $ yhattach jobid
    ```
  - 查看近期所有运行过的任务列表
    ```bash
    $ yhacct --field=user,group,jobid,ncpus,nnodes,nodelist,start,end,elapsed,state -S 2/14/17 -E 2/16/17
    ```
  - 取消任务
    - 取消单个任务
      ```bash
      $ yhcancel  jobid
      ```
    - 取消所有任务
      ```bash
      $ yhcancel -u userName
      ```
  - 查看机时使用量（单位:核时）
    ```bash
    $ yhreport Cluster UserUtilizationByAccount start=1/13/17 end=2/16/18 -t hour
    $ yhreport Cluster UserUtilizationByAccount start=1/13/17 end=2/16/17 -t hour
    $ yhreport Cluster UserUtilizationByAccount start=1/13/17T12:03:04 end=2/16/17T08:36:28 -t hour
    ```

## 搭建局域网

- 多台主机`n1-nx`通过主节点`n0`上网
- 服务器
  ```bash
  $ sudo vi /etc/sysctl.conf
  net.ipv4.ip_forward= 1  # uncomment
  $ sudo sysctl -p # 立即生效
  $ sudo iptables -F
  $ sudo vi /etc/rc.local
  iptables -P INPUT ACCEPT
  iptables -P FORWARD ACCEPT
  # iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -o eno1 -j MASQUERADE
  iptables -t nat -A POSTROUTING -o eno1 -s 192.168.1.0/24 -j MASQUERADE # corrected by Shao Jingyu
  exit 0
  $ sudo vi /etc/network/interface
  auto lo
  iface lo inet loopback
  auto eno1
  iface eno1 inet dhcp  # to public network
  auto eno4
  iface eno4 inet static # to local area network
  address 192.168.1.251
  netmask 255.255.255.0
  $ sudo /etc/init.d/networking restart
  ```
- 客户端 
  ```bash
  $ sudo vi /etc/network/interface
  auto eno1
  iface eno1 inet static
  address 192.168.1.6 
  gateway   192.168.1.251 # server ip
  dns-nameservers 202.120.224.26 # DNS of server/public network
  $ sudo /etc/init.d/networking restart
  ```

# 参考内容

- [日常管理](http://yundongxiaoyang.top//2018/01/05/maintain-linux/)
- [好用的命令行工具](http://yundongxiaoyang.top//2018/01/03/command-line-software/)
- [nis help-oracle-import](https://docs.oracle.com/cd/E19455-01/806-1387/6jam692fn/index.html)
- [nfs server config](https://www.server-world.info/en/note?os=Ubuntu_16.04&p=nfs&f=1)
- [nfs client config](https://www.server-world.info/en/note?os=Ubuntu_16.04&p=nfs&f=2)
- [nis server config](https://www.server-world.info/en/note?os=Ubuntu_16.04&p=nis&f=1)
- [nis client config](https://www.server-world.info/en/note?os=Ubuntu_16.04&p=nis&f=2)
- [install nis](http://blog.51cto.com/dreamfire/160121)
- [top](https://www.cnblogs.com/ggjucheng/archive/2012/01/08/2316399.html)
- [虚拟内存、物理内存、共享内存](https://blog.csdn.net/u012398613/article/details/52903296)
