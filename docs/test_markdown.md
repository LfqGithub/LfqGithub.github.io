---
layout: wiki
title: Test Markdown
keywords: test, markdown
categories: [test]
description: 
use_math: true
comments: false
mermaid: true
flow: true
---
### flow
```flow
// 按从大到小的顺序输出a,b,c
st=>start: 开始
in=>inputoutput: 输入数据a,b,c
cond1=>condition: a < b
op1=>operation: 交换a,b的值
cond2=>condition: b < c
op2=>operation: 交换b,c的值
out=>inputoutput: 输出数据a,b,c
e=>end: 结束
```

### mermaid

<div class="mermaid">
sequenceDiagram
    Alice-->>John: Hello John, how are you?
    John-->>Alice: Great!
</div>

### sequence

```sequence
Andrew->China: Says Hello
Note right of China: China thinks\nabout it
China-->Andrew: How are you?
Andrew->>China: I am good thanks!
```

### flowchart

```flow
st=>start: Start
e=>end
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?
io=>inputoutput: catch something...

st->op1->cond
cond(yes)->io->e
cond(no)->sub1(right)->op1
```
