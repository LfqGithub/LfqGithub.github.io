---
layout: post
title: File sharing between Linux and Windows
categories: Linux
---

Updating...

[Samba](https://www.samba.org/) opens windows to a wider world.

# Install
 
```
$ sudo apt install samba
$ mkdir /home/home_public/username/
$ sudo chmod 777 /home/home_public/username/
$ sudo vim /etc/samba/smb.conf
[share]
path = /home/home_public/username
public = yes
writable = yes
valid users = username
create mask = 0644
force create mode = 0644
directory mask = 0755
force directory mode = 0755
available = yes
$ sudo touch /etc/samba/smbpasswd
$ sudo smbpasswd -a username
$ sudo /etc/init.d/samba restart
# test 
$ sudo apt-get install smbclient 
$ smbclient -L //localhost/share
# windows 添加网络位置,输入 \\ip\share
```


# Links
- [Linux与Windows共享文件夹之samba的安装与使用（Ubuntu为例）](https://www.cnblogs.com/gzdaijie/p/5194033.html)

