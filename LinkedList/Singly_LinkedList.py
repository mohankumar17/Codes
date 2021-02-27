class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_beg(self,val):
        n=Node(val)
        if self.head is None:
            self.head=n
        else:
            n.next=self.head
            self.head=n

    def insert_end(self,val):
        n=Node(val)
        if self.head is None and self.tail is None:
            self.head=self.tail=n
        else:
            self.tail.next=n
            self.tail=n

#################################################
def display(head):
    while head is not None:
        print(head.val,end=' ')
        head=head.next

def insert_pos(head,val,pos):
    temp=head
    n=Node(val)
    if pos==0:
        n.next=head
        head=n
        return head

    prev=temp
    while pos>0:
        prev=temp
        temp=temp.next
        pos=pos-1
    n.next=temp
    prev.next=n
    return head

def delete_beg(head):
    t=head
    head=head.next
    del t
    return head

def delete_end(head):
    t=head
    prev=None
    while t.next is not None:
        prev=t
        t=t.next
    t=prev
    t.next=None
    return head

def delete_at_pos(head,pos):
    if pos==0:
        return head.next
    t=head
    prev=None
    while pos>0:
        prev=t
        t=t.next
        pos=pos-1
    prev.next=t.next
    return head

def reverse(head):
    curr=head
    prev=None
    nex=head
    while curr is not None:
        nex=curr.next
        curr.next=prev
        prev=curr
        curr=nex
    return prev

def remove_duplicates_sorted(head):
    t=head
    while t.next is not None:
        if t.val==t.next.val:
            t.next=t.next.next
        else:
            t=t.next
    return head

def remove_duplicates(head):
    t=head
    s=[]
    while t is not None:
        if t.val in s:
            prev.next=t.next
        else:
            s.append(t.val)
            prev=t
        t=t.next

    return  head

def findMiddle(head):
    slow=head
    fast=head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

def swapNodes(head):
    if head is None:
        return None
    if head.next is None:
        return head
    if head.next.next is None:
        head.val,head.next.val=head.next.val,head.val
        return head
    a=head
    b=head.next
    while b is not None:
        a.val,b.val=b.val,a.val
        a=b.next
        if a is not None:
            b=a.next
        else:
            b=None

    return head

def palindrome(head):
    t=reverse(head)
    while head is not None:
        if head.val!=t.val:
            return False
        head=head.next
        t=t.next
    return True

def mergeSort(left,right):
    head=None
    if left is None:
        return right
    if right is None:
        return left
    if left.val<=right.val:
        head=left
        head.next=mergeSort(left.next,right)
    else:
        head=right
        head.next=mergeSort(left,right.next)
    return head

def sortList(head):
    if head is None:
        return None
    if head.next is None:
        return head

    mid=findMiddle(head)
    midnext=mid.next
    mid.next=None
    left=sortList(head)
    right=sortList(midnext)
    return mergeSort(left,right)

ob=LinkedList()
l=[3,5,7,2,8,1,6]
#l=[1,1,2,2,2,3,4,5,5]
#l=[2,1,4,5,3,2,2,3,5]
#l=[4,2,2,2,4]

for i in l:
    ob.insert_end(i)
display(ob.head)
print()
'''pos=2
val=7
head=insert_pos(ob.head,val,pos)
display(head)
head=delete_beg(ob.head)
display(head)
head=delete_end(ob.head)
display(head)
pos=3
head=delete_at_pos(ob.head,pos)
display(head)
head=reverse(ob.head)
display(head)
head=remove_duplicates_sorted(ob.head)
display(head)
head=remove_duplicates(ob.head)
display(head)
mid=findMiddle(ob.head)
print(mid.val)
p=palindrome(ob.head)
print(p)
head=swapNodes(ob.head)
display(head)'''

head=sortList(ob.head)
display(head)
