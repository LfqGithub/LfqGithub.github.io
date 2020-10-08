---
layout: post
title: Video Editing on Linux
categories: [Linux]
description: Edit videos using linux command line
keywords: video, edit, linux, ffmpeg
---

简单快捷处理视频, updating......

# Syntax

>>可配合**youtube-dl**下载视频素材(注意版权保护,避免侵权)

```bash
# Install ffmpeg on Ubuntu:  $ sudo apt install ffmpeg 

ffmpeg -ss 00:01:50 -i [input] -t 10.5 -c copy [output] # 从视频中剪取一段作为新视频
```

# Refs
- [FFmpeg视频处理入门教程-阮一峰](http://www.ruanyifeng.com/blog/2020/01/ffmpeg.html)

