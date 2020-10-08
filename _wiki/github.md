---
layout: wiki
title: Github
categories: Github
keywords: github, pages, gist
description: 学习使用Github
---

# Github Pages

## Todo

- [ ] 添加 Flow Chart 功能

## Figure

<script src="https://gist.github.com/LfqGithub/8ad85c8adaf8a3d2a06d2b67d31443f1.js"></script>

<div align="center"><img height="300" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/figure-schematic.PNG"/><figcaption>I am a caption</figcaption></div>

>> `width`和`height`单位为像素

## Codes

Github Pages 添加代码并且高亮显示有两种方法
- 直接使用 markdown 语法格式化代码
- 引用gist中代码(代码变动不需要再次修改文章)


## Links

- 默认方式
  ```bash
  [about links](.....links......)
  ```

- 给图片添加链接
  ```bash
  <a href="links">
    <img src="/images/posts/****/****.png">
  </a>
  ```

## Text

- 加粗: `**content**`


## Record Rules

- 单个问题及解决方案-post
- 基本知识学习、记录、理解-wiki


## 统计访问次数

- 使用[LeanCloud](https://leancloud.cn/)
- 注册账号
- 创建应用（应用名随意）
- 应用key
- 创建Class（Class 名称设为Counters)
- `_config.yml`中添加
  ```html
  leancloud:
    enable: true
    app_id: your_app_id
    app_key: your_app_key
  ```
- 设置`leancloud-analytics.html`
  ```bash
  $ cd _includes
  $ vi leancloud-analytics.html
  # 具体内容请查看相关文件
  ```
- 添加`leancloud-analytics.html`到`_layout/default.html`
  ```bash
  $ vi _layout/default.html 
  # 具体内容请查看相关文件
  ```
- `post.html`和`wiki.html`中添加访问次数
  ```bash
  $ vi _layout/post.html
    <div class="Hits">
		  {% if site.leancloud.enable %}
		    <span id="{{ page.url }}" class="leancloud_visitors" data-flag-title="{{ page.title }}">
		    <span class="post-meta-divider">|</span>
		    <span class="post-meta-item-text"> Hits:  </span>
		    <span class="leancloud-visitors-count"></span>
		    </span>
		  {% endif %}
    </div>
  $ vi _layout/post.html # 添加相同内容，位置根据需要定
  ```

# Markdown Syntax

>注意，如 Github Pages 代码错误，推送到 Github 服务器中后返回报错，其 Markdown 文本中的代码行数和实际行数并不对应 (为去除文件标题后的行数)

## Latex in Pages

- title中添加`use_math: true`
 `$--add you equation here--$`中添加行内公式, `$$ equation content $$` 添加行间公式，前后需空行

Github Favored Markdown 支持latex公式，常用语法参考[Latex 公式/符号](https://yundongxiaoyang.top/wiki/latex-equation/)


# Gist

Github gist 可以方便的保存、分享代码。如果将代码文件放到gist中，可以将gist地址插入Github pages中，这样我们修改代码后就不用再次更新github pages中的代码部分。
但是，一个gist只有一个地址，如果一个gist中有多个文件，我们只能引用该gist中的所有文件，给在Github Pages中插入代码带来不便。
针对这一不便之处，[defunkt](https://github.com/defunkt) 开发了`gist`工具，使我们在命令行中也可以添加gist，而不用回到Github网页。

- 安装：`sudo apt install rubygems && gem install gist`
- Github网页内设置: `Settings`-`Developer settings`中生成`Personal access token`，放入`~/.gist`文件中
- 使用:
  ```bash
  $ gist --login # 输入github用户名
  $ gist filename # 将文件`filename`添加到github gist 
  $ gist -p filename # 将文件`filename`添加到私有github gist 
  $ gist -d "comment" filename # 将文件`filename`添加到github gist并添加描述
  $ gist filename1 filename2 # 将文件`filename1/2`添加到github gist 
  $ gist filename1 filename2 # 将文件`filename1/2`添加到github gist 
  $ gist -e filename # 将文件filename 添加到 github gist 并且复制/输出 embeddable URL. # bug: gist -e <filename> will add the filename to the gist twice (two identical files)，当前直接用git <filename>即可
  $ gist -l # 列出当前github用户所有gist
  $ gist -u full_gist_id filename # 更新gist文件
  ```

# Connection

## 连接问题

- 打开 Github 官网速度极慢或者无法访问
- github repos 无法连接到 github 远程仓库: `pull` 和 `push` 失效

## 解决方法

- 打开 [Dns查询](http://tool.chinaz.com/dns)
- 检测输入栏中输入 Github 官网地址--`github.com`
- 将检测列表里的 `TTL` 值最小的 IP 输入 `hosts` 文件
  - `ip github.com`
- 修改 `hosts` 方法
  - Linux 直接修改 `/etc/hosts`
  - Windows 10 修改host 方法见 [wsl修改hosts方法](http://yundongxiaoyang.top//2018/01/20/wsl/)

>该方法对其它网站也有效，如 `bitbucket.org`

# 其它 

- [将网站添加到谷歌数据库](https://www.google.com/webmasters/tools/submit-url?pli=1)

# Links
- [Github打不开--sknight 的回答-知乎](https://www.zhihu.com/question/20732532/answer/138683232)
- [添加网页访问次数](http://blog.csdn.net/u013553529/article/details/63357382)
- [gist command line tool](https://github.com/defunkt/gist)
