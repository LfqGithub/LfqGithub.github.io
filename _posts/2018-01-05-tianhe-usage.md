---
layout: post
title: 天河二号超算使用
categories: Linux 
description: 天河二号, centos
keywords: super computer, centos
---

超算使用

## 登陆
- 打开代理
- 登陆超算

## 文件传输
- scp
- rsync

## 安装/调用软件
- `fftw`以及`matlab`, 在超算上都已经安装好，如果需要使用，需将下列内容添加到自己的`~/.bashrc`中

  ```bash
  export C_INCLUDE_PATH=/THFS/opt/fftw/3.3.6-pl1_share_mpi/include:/THFS/opt/matlab2016a/extern/include:$C_INCULDE_PATH # c
  export CPLUS_INCLUDE_PATH=/THFS/opt/fftw/3.3.6-pl1_share_mpi/include:/THFS/opt/matlab2016a/extern/include:/THFS/opt/gcc/5.2/lib64:$CPLUS_INCULDE_PATH # c++
  export PATH=/THFS/opt/matlab2016a/bin:/THFS/opt/gcc/5.2/bin:/THFS/opt/python3.6/bin:$PATH
  export LD_LIBRARY_PATH=/THFS/opt/fftw/3.3.6-pl1_share_mpi/lib:/THFS/opt/matlab2016a/bin/glnxa64:/THFS/opt/gcc/5.2/lib64:$LD_LIBRARY_PATH
  export LIBRARY_PATH=/THFS/opt/fftw/3.3.6-pl1_share_mpi/lib:/THFS/opt/matlab2016a/bin/glnxa64:/THFS/opt/gcc/5.2/lib64:$LIBRARY_PATH
  ```
- python主要的package，如`numpy, matplotlib`等已经安装好，如果有其他需要，可以联系客服帮助安装，也可以自己安装其他发行版，如`Anaconda`。

## 程序提交

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

## 常用命令

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

