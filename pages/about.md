---
layout: page
title: About
description: 运动小样学习的地方
keywords: yundongxiaoyang, 运动小样
comments: false
menu: 关于
permalink: /about/
---

**运动小样** 欢迎您！

本博客并不志于完整的介绍某知识点或者解决某问题，只是个人经验的记录与备忘。

>>若难为宏伟志，则做好分内事，将每天过得充实快乐，也未尝不是一种简单的成就。
倘若能达到或者部分企及诸如Wiki，3Blue1Brown创始人的成就，则人生无憾矣。



>>**Motto**: 善战者无赫赫之功


## 联系

{% for website in site.data.social %}
* {{ website.sitename }}：[@{{ website.name }}]({{ website.url }})
{% endfor %}

## Skill Keywords

{% for category in site.data.skills %}
### {{ category.name }}
<div class="btn-inline">
{% for keyword in category.keywords %}
<button class="btn btn-outline" type="button">{{ keyword }}</button>
{% endfor %}
</div>
{% endfor %}
