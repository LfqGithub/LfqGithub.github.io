---
layout: wiki
title: Regular Expression
---


# Syntax

`^`: 行首

`$`: 行尾

`\<`: 词首 `\<abc`: 以`abc`为首的单词

`\>`: 词尾 `\<abc`: 以`abc`结尾的单词

`.`: 任意单个字符

`*`: 任意数量的任意字符 `zo*`匹配`z`, `zo`和`zoxxxx`，相当于`{0,}`

`[ ]`: 字符集合， `[abc]`匹配`a`或`b`或`c`

`[a-zA-Z]`: 匹配所有26个大小写字符

`[^a]`: 非`a`字符

`&`: 被匹配的变量

`\`: 将下一个字符标记为特殊字符`\\`匹配`\`

`+`: 匹配前面的表达式一次或者多次, `zo+`匹配`zo`和`zoxxx`，但不匹配`z`，相当于`{1,}`

`?`: 匹配前面的表达式一次或者零次。 `do(es)?`匹配`do`和`does`，相当于`{0,1}`

`{n}`: `n`为非负整数，`o{2}`匹配`food`中`oo`, 不匹配`bob`中的`o`

`{n,}`: 至少匹配 n 次

`{n,m}`: `n<=m`，匹配`[n,m]`次

## Links

- [Regular Expression-wiki](https://zh.wikipedia.org/wiki/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F#%E5%8C%B9%E9%85%8D)

