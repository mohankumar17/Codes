from collections import defaultdict
class Node:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class LinkedList:
    def __init__(self):
        self.head=None

def copyRandomList(head):
    d=defaultdict(lambda : Node(0))
    d[None]=None
    temp=head
    while temp is not None:
        d[temp].label=temp.label
        d[temp].next=d[temp.next]
        d[temp].random=d[temp.random]
        temp=temp.next
    return d[head]

ob=LinkedList()
ob.head=Node(1)
ob.head.next=Node(2)
ob.head.next.next=Node(3)
ob.head.next.next.next=Node(4)

ob.head.random=ob.head.next.next
ob.head.next.random=ob.head
ob.head.next.next.random=ob.head.next.next
ob.head.next.next.next.random=ob.head.next

clone=copyRandomList(ob.head)
while clone:
    print(clone.label,end=' ')
    clone=clone.next
