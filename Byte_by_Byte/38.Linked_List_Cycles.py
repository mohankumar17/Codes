class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

def isCyclic(head):
    t=[]
    if head is None:
        return None
    while head:
        if head in t:
            return True
        t.append(head)
        head=head.next
    return False


ob=LinkedList()
ob.head=Node(1)
ob.head.next=Node(2)
ob.head.next.next=Node(3)
ob.head.next.next.next=Node(4)
print(isCyclic(ob.head))

ob1=LinkedList()
ob1.head=Node(1)
ob1.head.next=Node(2)
ob1.head.next.next=Node(3)
ob1.head.next.next.next=Node(4)
ob1.head.next.next.next.next=ob1.head.next
print(isCyclic(ob1.head))
