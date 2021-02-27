class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

def Nth_from_Last(head,n):
    if head is None:
        return None
    temp=head
    tot=0
    while temp:
        tot=tot+1
        temp=temp.next
    if n>=tot:
        return None

    i=tot-n
    while i>1:
        i=i-1
        head=head.next
    return head.val


ob=LinkedList()
ob.head=Node(1)
ob.head.next=Node(2)
ob.head.next.next=Node(3)
ob.head.next.next.next=Node(4)
ob.head.next.next.next.next=Node(5)
#ob.head.next.next.next.next.next=Node(8)

res=Nth_from_Last(ob.head,0)
print(res)

res=Nth_from_Last(ob.head,1)
print(res)

res=Nth_from_Last(ob.head,3)
print(res)

res=Nth_from_Last(ob.head,4)
print(res)

res=Nth_from_Last(ob.head,5)
print(res)
