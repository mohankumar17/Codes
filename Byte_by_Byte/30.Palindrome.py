class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

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

def palindrome(head):
    if head is None:
        return True
    res=reverse_nodes(head)
    while head is not None:
        if head.val!=res.val:
            return False
        head=head.next
        res=res.next
    return True

ob=LinkedList()
ob.head=Node(3)
ob.head.next=Node(2)
ob.head.next.next=Node(3)
#ob.head.next.next.next=Node(4)
#reverse_print(ob.head)
#print()
print(palindrome(ob.head))
#while res:
#    print(res.val,end=' ')
#    res=res.next
