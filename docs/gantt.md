---
layout: wiki
title: Gantt diagram
keywords: Gantt
categories: [chart]
mermaid: true
description: Gantt diagram
---

Updating......

# Syntax

## 任务类型
- done
- active
- crit 关键任务
- 默认为待完成

## 任务描述
- after, 描述任务时间关系，des2 after des1 表示 des2 紧跟 des1之后

## 任务时长
- 时间范围， 如 2020-02-01， 2020-03-01
- 指定天数，如 5d
- 指定开始日期+天数，如 2020-02-01, 5d

## 示例

<script src="https://gist.github.com/LfqGithub/0d7886601b5f5c4f2634cf7673c700e8.js"></script>

<div class="mermaid">
gantt

title                     Adding GANTT diagram functionality to mermaid


section A section
Completed task            :done,    des1, 2020-03-06, 2020-03-08
Active task               :active,  des2, 2020-03-09, 1d
Future task               :         des3, after des2, 1d
Future task2              :         des4, after des3, 1d

section Critical tasks
Completed task in the critical line :crit, done, 2020-03-05,2d
Implement parser and jison          :crit, done, after des1, 2d
Create tests for parser             :crit, active, 1d
Future task in critical line        :crit, 2d
Create tests for renderer           :2d
Add to mermaid                      :1d

section Documentation
Describe gantt syntax               :active, a1, after des1, 1d
Add gantt diagram to demo page      :after a1  , 2d
Add another diagram to demo page    :doc1, after a1, 2d

section Last section
Describe gantt syntax               :after doc1, 1d
Add gantt diagram to demo page      :2d
Add another diagram to demo page    :2d
</div>


<div align="center"><img width="700" src="https://raw.githubusercontent.com/LfqGithub/LfqGithub.github.io/master/images/charts-in-markdown/gantt-schematic-typora.png"/><figcaption>Typora渲染图</figcaption></div>







# Ref
- [Gantt in mermaid](http://mermaid-js.github.io/mermaid/#/gantt)
- [Gantt diagram](https://github.com/mermaid-js/mermaid/blob/develop/docs/gantt.md)
- [Markdown 绘制 Gantt 图教程--简书](https://www.jianshu.com/p/a0dabf0b6815)
