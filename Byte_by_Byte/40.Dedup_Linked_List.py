class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

def remove_duplicates(head):
    if head is None:
        return None
    temp=head
    prev=head
    s=set()
    while temp:
        if temp.val in s:
            prev.next=temp.next
        else:
            s.add(temp.val)
            prev=temp
        temp=temp.next
    return head

ob=LinkedList()
ob.head=Node(6)
ob.head.next=Node(4)
ob.head.next.next=Node(1)
ob.head.next.next.next=Node(2)
ob.head.next.next.next.next=Node(2)

res=remove_duplicates(ob.head)
while res:
    print(res.val,end=' ')
    res=res.next
