class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

def reverse_print(head):
    if head is None:
        return None
    reverse_print(head.next)
    print(head.val,end=' ')

def reverse_nodes(head):
    if head is None:
        return None
    prev=None
    curr=head
    nex=head
    while curr is not None:
        nex=curr.next
        curr.next=prev
        prev=curr
        curr=nex
    return prev

ob=LinkedList()
ob.head=Node(1)
ob.head.next=Node(2)
ob.head.next.next=Node(3)
#ob.head.next.next.next=Node(4)
reverse_print(ob.head)
print()
res=reverse_nodes(ob.head)
while res:
    print(res.val,end=' ')
    res=res.next
