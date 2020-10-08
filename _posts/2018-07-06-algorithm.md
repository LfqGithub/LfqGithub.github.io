---
layout: post
title: Simple Algorithm
use_math: true
categories: [Python, Algorithm]
---

Updating......

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
def main():
    num_list=[1,2,3,4,5,8,7,6,3,2,1]
    print('original list: ', num_list)
    bubble_sort(num_list)
    print('sorted list: ', num_list)

if __name__=='__main__':
    main()
```
## Insert Ranking 

- 复杂度: $O(n^2)$
- 稳定

```python
def insert_sort(num_list):
    n=len(num_list)
    for i in range(1,n):
        for j in range(i,0,-1):
            if num_list[j]<num_list[j-1]:
                num_list[j],num_list[j-1]=num_list[j-1],num_list[j]
            else:
                break

def main():
    num_list=[1,3,5,7,6,2,3,1,-1]
    print('original list: ', num_list)
    insert_sort(num_list)
    print('sorted list: ', num_list)

if __name__=='__main__':
    main()
```

# Algorithm in C++

## Simple Sorting

```c++
#include<iostream>
using namespace std;

void  tem_swap(int array[], int i, int j)
{
	int tem=array[i];
	array[i]=array[j];
	array[j]=tem;
}

void select_sort(int array[], int n)
{
	for(int i=0;i<n-1;i++)
	{
		int min_index=i;
		for (int j=i;j<n;j++)
		{
			if (array[min_index]>array[j])
				min_index=j;
		}
		if (min_index!=i)
			tem_swap(array,i,min_index);
	}
}

int main()
{
	int a[5]={1,5,4,3,8};
	select_sort(a,5);
	for(int i=0;i<5;i++)
	{
		cout<<a[i]<<"  ";
	}
	cout<<endl;
	return 0;
}
```

## Insert Sorting

```C++
#include<iostream>
using namespace std;

void tem_swap(int array[],int i, int j)
{
	int tem=array[i];
	array[i]=array[j];
	array[j]=tem;
}

int insert_sort(int array[], int n)
{
	for(int i=1;i<n;i++)
	{
		for(int j=i;j>0;j--)
			if(array[j]<array[j-1])
				tem_swap(array,j,j-1);
			else
				break;
	}
}


int main()
{
	int num_list[6]={1,2,343,5,35,1};
	insert_sort(num_list,6);
	for(int i=0; i<6; i++)
		cout<<num_list[i]<<"  ";
	cout<<endl;
	return 0;
}
```

