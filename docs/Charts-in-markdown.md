```mermaid

graph TB
	0[0:默认矩形]--Normal line---a
	subgraph 子图
        a(a:圆角矩形)--add text between line---b((b:圆形))
        style b fill:#f9f,stroke:#333,stroke-width:4px,fill-opacity:0.5
        style c fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 10,5
        style d fill:#f9f,stroke:#333,stroke-width:4px,fill-opacity:0.5
        c>c:右箭头]-->d(d:自定义圆角矩形)
        a--line with arrow-->c
        b-.-e{e:菱形}
        e-.dashed line with arrow.->f(f: End)
        d==thicker line with arrow==>f
        end
	

```

```mermaid
sequenceDiagram
	Alice-->>John: Hello John, how are you?
	John-->>Alice: Great!
```

```sequence
Andrew->China: Says Hello
Note right of China: China thinks\nabout it
China-->Andrew: How are you?
Andrew->>China: I am good thanks!
```



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

