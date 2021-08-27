---
layout: wiki
title: 浏览器使用
keywords: 
categories: [web browser, softwares]
description: How to browse the web
comments: yes
---

Browser Softwares, updating ...

# Edge (Chromium Core)

## Dark Mode
- 打开网址 edge://flags
- 搜索 enable-force-dark（强制启用暗黑模式），出现一个标题为“Force Dark Mode for Web Contents”的选项，修改为enabled.
- 重启Edge

# Chrome

## Plugins

以下插件同样适用于 Chromium Core Edge Browser

- [Vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb): 使用Vim命令操作浏览器
- [Vimium C](https://github.com/gdh1995/vimium-c): 和Vimium功能相同，速度更快
- [PDF Viewer C](https://chrome.google.com/webstore/detail/pdf-viewer-for-vimium-c/nacjakoppgmdcpemlfnfegmlhipddanj?hl=en-US)
- [Adblock Plus](https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb): 屏蔽网页广告
- [Always Clear Downloads](https://chrome.google.com/webstore/detail/always-clear-downloads-in/efoelbbfbknfhpmgclpcdbkoieedkkai): 下载完成后自动隐藏下载栏
- [TemperMonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo): Userscript manager
  - Sci-hub button: 在doi链接后添加scihub按钮，直接跳转到sci-hub下载链接
  - [本地Youtube下载器](https://greasyfork.org/zh-CN/scripts/369400-local-youtube-downloader)
  - [uBlacklist](https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe): 屏蔽特定网站在google搜索结果中的展示。



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

### Force start the dark-mode

- 更新谷歌浏览器到最新版
- 打开网址 chrome://flags
- 搜索 enable-force-dark（强制启用暗黑模式），出现一个标题为“Force Dark Mode for Web Contents”的选项，修改为enabled.
- 重启Chrome
- 禁用该功能可同样按照上述步骤操作。

### Extend display region

- 浏览器默认隐藏书签栏。`Ctrl+Shift+B`隐藏书签栏，使用Vimium插件配合`B`：搜索书签, `O`: 搜索历史记录来搜索网址
- 使用插件`Always Clear Downloads`自动隐藏下载栏

