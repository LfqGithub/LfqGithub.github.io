---
layout: wiki
title: Docker 
categories: [Programming]
description: learn docker
keywords: docker
---

Updating...

# 安装 Docker

## Ubuntu 18.04 LTS
```shell
$ sudo apt remove docker docker-engine docker.io containerd runc # remove old versions
$ sudo apt-get install  apt-transport-https ca-certificates curl gnupg-agent software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo apt-key fingerprint 0EBFCD88
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
# or 
$ sudo snap install docker # for Ubuntu 18.04 LTS
```

## WSL 安装 Docker
目前WSL对Docker的支持并不完善，不建议使用此种方法

```bash
sudo apt update
sudo apt install docker.io
sudo usermod -aG docker $USER
# 管理员身份启动 WSL 控制台
sudo cgroupfs-mount 
sudo service docker start
# 每次重启系统后都要执行上两行命令
```

# 开启 Docker 服务
```shell
sudo service docker start
# or 
sudo systemctl start docker
```

# Docker 基本概念
- image
- container: image 的实例

# Docker 基本用法
Docker需要用户有管理员权限，每次执行需要加`sudo`，为了避免添加这一命令，可将用户加入Docker用户组`sudo usermod -aG docker $USER`

```shell
# get remote image
$ docker image pull library/hello-world # the command is equal to "docker image pull hello-world" as the "library" is the default group
# check the images in the current docker
$ docker image ls
# run an image
$ docker container run hello-world # auto download image if the image does not exist
$ docker container run -it ubuntu bash # run Ubuntu image 
# stop an image 
$ docker container kill [containID]
$ docker container rm [containID]  
$ docker contain start/stop/logs/exec/cp [containID]
```


# Ref

- [WSL 中安装 Docker](https://zhuanlan.zhihu.com/p/39187620)
- [Install Docker on Ubuntu--official](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Docker 入门教程-阮一峰](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [Docker——从入门到实践](https://yeasy.gitbooks.io/docker_practice/introduction/what.html)

