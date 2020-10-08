---
layout: wiki
title: To Do List
description: ToDo
keywords: ToDo
comments: false
menu: ToDo
permalink: /todo/
---

## 待完成

- [ ] 数学
  - [ ] 线性代数
  - [ ] 微积分学

- [ ] 编程
  - [ ] C++简单算法
  - [ ] 算法性能和C++标准库对比

- [ ] bash 脚本备份自己所有 Linux 配置
- [ ] [Ising Model](http://www.fuzihao.org/blog/2016/09/01/%E4%BC%8A%E8%BE%9B%E6%A8%A1%E5%9E%8B-Ising-Model/#more)
- [ ] [遗传算法](https://blog.csdn.net/on2way/article/details/40053639)
- [ ] [编写Python模块](http://www.infoq.com/cn/articles/Python-writing-module)
- [ ] C++和Python 编码简单算法
- [ ] 金融知识 
- [ ] Shell
- [ ] Python
  - [ ] Pandas
  - [ ] [Requests](http://docs.python-requests.org/zh_CN/latest/)
  - [ ] [Numba](https://numba.pydata.org/numba-doc/dev/index.html)
- [ ] [google style guide](http://zh-google-styleguide.readthedocs.io/en/latest/contents/)
- [ ] C-Sharp 
- [ ] [斐波那契数列--wiki](https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97)

## 书单

- [ ] CPU工作原理
- [ ] 计算机工作原理

## Doing

- 房贷计算器

# Ref
- [Numba-offical](http://numba.pydata.org/)
- [Numba-doc](https://numba.pydata.org/numba-doc/dev/index.html)
- [XML教程](http://www.runoob.com/xml/xml-tutorial.html)
- [解读Python解析XML](http://codingpy.com/article/parsing-xml-using-python/)


## Done
- [x] Markdown 甘特图语法

<ul class="listing">
{% for todo in site.todo %}

{% if todo.title != "ToDo Template" %}
<li class="listing-item"><a href="{{ site.url }}{{ todo.url }}">{{ todo.title }}</a></li>
{% endif %}
{% endfor %}
</ul>
