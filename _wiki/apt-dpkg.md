---
layout: wiki
title: apt/dpgk
---

Software Management, updating...

APT: [Advanced Packaging Tool](https://help.ubuntu.com/lts/serverguide/apt.html). 有别于单词 apt(恰当的，有倾向的)

# Syntax

```bash
$ sudo apt download package-name # download package to current directory
$ sudo apt show package-name # show information about package
$ sudo apt install package-name
$ sudo apt install --reinstall package-name
$ sudo apt autoremove
$ sudo apt update
$ sudo apt upgrade 
$ sudo apt install --fix-missing
$ sudo apt install -d package-name # download only，dir: /var/cache/apt/archives
$ sudo apt remove package-name 
$ sudo apt remove -f package-name 
$ sudo apt remove --purge package-name  # remove packages and related dependence
$ sudo apt clean  
```
## Add/remove repository

```bash
# Add repository
$ sudo add-apt-repository ppa:owername/projectname
$ sudo apt update
$ sudo apt install something
# Remove repository
$ cd /etc/apt/source.listd
$ sudo rm ppa_name
$ sudo apt update && sudo apt upgrade -y
```
# dpkg
```bash
$ sudo  dpkg -i *.deb # 如果提示依赖的库没有安装，执行 $ sudo apt -f install  # 更新依赖包
$ sudo  dpkg -P xxx  # Purge  an  installed or already removed package. This removes everything, including conffiles. 
```


# Extra-curricular Knowledge 

## update and upgrade 

- What is an update exactly?
  When we perform an update, it involves making changes to an app or an operating system is such a way that it doesn’t affect its core structure. So, most of the frequent changes made to your computer like bug fixes, security patches, adding support for drivers and newer hardware, etc. can be termed as an Update.
  
  An update is often small in size, and it might take a couple of minutes to perform one. The word ‘small’ is relative. For instance, an update meant for a single app can range from a few kilobytes to a couple of megabytes in size, while an update for an operating system can go up to a few hundred megabytes.
  
- What’s an upgrade then?
  When a set of changes made to a software are significant and substantial enough, we can call it an Upgrade. That’s why making a switch from Ubuntu 16.04 to Ubuntu 17.04 would be called an upgrade, not update.
  
  An upgrade mostly includes important changes to the GUI and a variety of new features and options which are not in the existing version of a software or operating system. And as you might have guessed, its size can go up to several gigabytes.

- Update Vs Upgrade
  Updates are free
  Updates meant for various kind of software is mostly free. Because their price is often included in the amount you pay when you buy the software. That’s one of the reasons Windows comes so costly and gives you updated without any extra charge. It can be the other way round, most of the open source software vendors often provide both software and updates for free.
  
  In the case of an Upgrade, software vendors might charge you. But, nowadays, most of the apps and paid operating systems including Windows and MacOS have a free upgrade.
  
  Upgrades are bigger, complex
  As already told, the time required to install an update is quite less than an upgrade. Installing an upgrade is more complicated and tedious as the amount of data that needs to replaced or copied is quite a large. It might even take a couple of hours to upgrade a system.
  
  Another thing that sets an update and an upgrade apart is the version. An upgrade released for a software makes a big change to the version number. For instance, Android 6.0 to Android 7.0, or Windows 8 to Windows 10.
  
  What’s more is that an upgrade can be used to perform a clean install of the software. However, in practical scenarios, the software makers regularly put all the latest updates in the most recent version of the setup file or ISO. So, when you download the software from their website, all the latest updates already included.
  
# BugFix
- `Sub-process /usr/bin/dpkg returned an error code (1)`
  - reason: can not remove a package
  - solution: `sudo dpkg --purge --force-all packageName`


# Links

- [update vs upgrade](https://fossbytes.com/whats-the-difference-between-update-and-upgrade/)
