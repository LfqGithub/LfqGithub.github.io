---
layout: wiki
title: Algorithm
---


# 简单排序

# 快速排序

# 选择排序

# 旅行商问题

# 贪婪算法

# 动态规划

# 广度优先搜索

# 迪克斯特拉算法

# K 最邻近算法

# 线性规划

# Bellman-Ford 算法

# 布隆过滤 

# HyperLogLog

# SHA

# Simhash

# D-H密钥交换


# Reference

# Algorithm in Python

## Simple/Select Ranking

- 复杂度: $O(n^2)$
- 不稳定

```python
def select_sort(num_list):
    n=len(num_list)
    for i in range(n):
        min_index=i
        for j in range(i+1, n):
            if num_list[j]<num_list[min_index]:
                min_index=j
        if min_index!=i:
            num_list[min_index],num_list[i]=num_list[i],num_list[min_index]
def main():
    num_list=[1,3,5,8,6,7,5,1,2]
    print('original list: ', num_list)
    select_sort(num_list)
    print('sorted list: ', num_list)

if __name__=='__main__':
    main()
```

## Bubble Ranking
- 复杂度: $O(n^2)$
- 稳定

```python
def bubble_sort(num_list):
    n=len(num_list)
    flag=True
    for i in range(n-1):
        for j in range(n-1-i):
            if num_list[j]>num_list[j+1]:
                num_list[j],num_list[j+1]=num_list[j+1],num_list[j]
                flag=False
        if flag:
            break
```

- [十大经典排序算法-动图演示](https://www.cnblogs.com/onepixel/p/7674659.html)
