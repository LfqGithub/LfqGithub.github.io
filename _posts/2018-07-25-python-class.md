---
layout: post
title: Class in Python 
categories: Python
---

updating...

## 基本知识
- 面向对象编程的三大特性
  - 抽象
    - 从众多的事务中抽取出具有共同的、本质性的特征作为一个整体
  - 封装
    - 将通过抽象所得到的数据信息和操作进行结合，使其形成一个有机的整体。对内执行操作，对外隐藏细节和数据信息
  - 继承
    - 继承是指这样一种能力：它可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展
  - 多态
    - 
- 面向对象编程
  - 解耦合

## Python 调用另一个文件中的class
Python 会自动从 sys.path 路径列表里的所有路径里寻找代码中import的模块，这个路径列表可以通过在终端里输入命令查看
```bash
>>>import sys
>>>sys.path
['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/home/liufaqiang/.local/lib/python3.6/site-packages', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']
>>>sys.path.insert('a.py所在的路径') # 添加路径
```
## 类的组合
类之间有显著不同，并且较小的类是较大的类所需要的组件时，用组合

## Links

- [python-class-最全讲解](http://www.cnblogs.com/wangmo/p/7751199.html)
