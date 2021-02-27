class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

def divide(head):
    if head is None:
        return None
    slow=head
    prev=head
    ref=prev
    fast=head.next
    while fast and fast.next:
        prev=slow
        prev=prev.next
        slow=slow.next
        fast=fast.next.next
    t=slow.next
    prev.next=None
    ans=[ref,t]
    return ans

ob=LinkedList()
ob.head=Node(6)
ob.head.next=Node(4)
ob.head.next.next=Node(1)
ob.head.next.next.next=Node(2)
ob.head.next.next.next.next=Node(3)
ob.head.next.next.next.next.next=Node(8)

res=divide(ob.head)
res1=res[0]
res2=res[1]

while res1:
    print(res1.val,end=' ')
    res1=res1.next
print()
while res2:
    print(res2.val,end=' ')
    res2=res2.next
