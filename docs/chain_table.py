---
layout: wiki
title: 概率统计应用
keywords: [probablity, statistics, application]
categories: [math]
use_math: true
description: some word here
---

链表：

```python
# Single linked list
class listNode():
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution:
    def reverseList(self, head: listNode)->listNode:
        if not head:
            return None
        if not head.next:
            return head
        headNode=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        item=headNode
        return headNode

    def link2int(self,link:listNode):
        item=link
        num_list=[]
        while(item!=None):
            num_list.append(item.val)
            item=item.next
        int_num=0
        for i, el in enumerate(num_list):
            int_num+=num_list[i]*(10**(len(num_list)-i-1))
        return int_num

    def int2intList(self, int_num: int):
        i=0
        num_list=[]
        listNode_list=[]
        node=listNode(int_num%10)
        while int_num//(10**i)!=0:
            tem=int_num//10**i%10
            num_list.append(tem)
            listNode_list.append(listNode(tem))
            i+=1
        print(num_list)
        return num_list, listNode_list

    def nodeList2linkList(self,nodeList):
        head=nodeList[0]
        i=0
        while i<len(nodeList)-1:
            head.next=nodeList[i+1]
            i=i+1
        nodeList[len(nodeList)-1].next=None
        return head


    def calc_sum(self,listnode1: listNode, listnode2: listNode):
        int1, int2=link2int(listnode1), link2int(listnode2)
        return int1+int2

    def print_linked_list(self,head):
        if not head or not head.next:
            return []
        result = []
        while head:
            result.insert(0, head.val)
            head = head.next
        return result

    def print_linkList(self, _list_node: listNode):
        _head=_list_node
        print('type of head:',type(_head))


        print('head val:',_head.val)
        print('head val:',_head.val)



if __name__=="__main__":

    node00=listNode(1)
    node01=listNode(8)
    node02=listNode(9)
    node00.next=node01
    node01.next=node02
    node02.next=None

    node0=listNode(7)
    node1=listNode(2)
    node2=listNode(3)
    node3=listNode(4)
    node4=listNode(5)
    node0.next=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=None



    sol=Solution()
    right_node=sol.reverseList(node0)
    int_num=sol.link2int(right_node)
    num_list, node_list=sol.int2intList(int_num)
    print('type of node_list: ', type(node_list))
    result_linklist=sol.nodeList2linkList(node_list)
    print('type of link_list: ', type(result_linklist))
    print(sol.print_linked_list(result_linklist))
    print(sol.print_linked_list(node00))
    print('node0:',sol.print_linked_list(node0))

```
