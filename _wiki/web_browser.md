---
layout: wiki
title: Browser
keywords: 
categories: [softwares]
description: 更舒服的上网
comments: yes
---

Browser Softwares, updating ...

# Edge (Chromium Core)

> Edge with Chromium Core 目前使用体验已经很好，但是有一些bug还是无法做到好用， 比如登录edge浏览器就要微软账号，这样就无法在公司电脑和个人电脑同步书签、插件等。另外，一些谷歌插件，尤其是谷歌官方插件及主题无法在edge中使用。 可以将edge浏览器当作备用浏览器。

## Dark Mode
- 打开网址 edge://flags
- 搜索 enable-force-dark（强制启用暗黑模式），出现一个标题为“Force Dark Mode for Web Contents”的选项，修改为enabled.
- 重启Edge

# Chrome

## Plugins

以下插件同样适用于 Chromium Core Edge Browser
- uBlock Origin: 去广告，同时可以删除网页上几乎所有自己不需要/不喜欢的内容
- [Vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb): 使用Vim命令操作浏览器
- [Vimium C](https://github.com/gdh1995/vimium-c): 和Vimium功能相同，速度更快
- [Always Clear Downloads](https://chrome.google.com/webstore/detail/always-clear-downloads-in/efoelbbfbknfhpmgclpcdbkoieedkkai): 下载完成后自动隐藏下载栏
- [TemperMonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo): Userscript manager
- [uBlacklist](https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe): 屏蔽特定网站在google搜索结果中的展示, 如不想在谷歌搜索中显示cdsn等

## Themes

- 黑暗模式： 使用chrome官方的just black主题，且在`chrome://flags`中搜索force dark mode, 打开强制黑暗模式

## Change the search engine of address bar
- 以在地址栏使用知乎搜索引擎为例
  - Settings--Search Engine--Manage search engine--Other search engines--Add
  - 在知乎网页版随便搜索，假设为xxx，确定后，复制搜索结果页面的网址`https://www.zhihu.com/search?type=content&q=%E6%9D%8E%E5%AD%90`，将搜索内容代替为`%s`, keyword设置为`zhi`。
  - 每次在地址栏输入`zhi`+`Tab`，输入搜索内容，就可以直接用zhihu搜索


## Download youtube 4k/8K videos
- 使用tempermonkey的[本地Youtube下载器](https://greasyfork.org/zh-CN/scripts/369400-local-youtube-downloader)插件
- 分别下载4k/8k webm（视频）和weba（音频）文件
- 此时下载的视频文件和音频文件是分离的，需要将二者合成
  - Ubuntu 安装ffmpeg
  ```bash
  $ sudo apt install software-properties-common
  $ sudo add-apt-repository ppa:mc3man/trusty-media -y
  $ sudo apt install ffmpeg -y
  ```
- 合成音轨和视频：`ffmpeg -i video.webm -i audio.weba -c copy output.mkv`


## Customize the effect of display

### Font

- 修改google 浏览器字体全部为微软雅黑

### Scaling
- 2K 分辨率下将缩放调整为125%, 4k分辨率下将电脑缩放改为200%
