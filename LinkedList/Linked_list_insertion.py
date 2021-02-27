class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_beg(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
        else:
            save=self.head
            self.head=n
            n.next=save

    def insert_end(self,data):
        n=Node(data)
        if self.head is None and self.tail is None:
            self.head=self.tail=n
        else:
            self.tail.next=n
            self.tail=n

    def delete_beg(self):
        if self.head is None:
            print('Underflow')
        else:
            ptr=self.head
            self.head=self.head.next
            del ptr

def deleteDuplicates(head):
    temp=head
    while temp is not None and temp.next is not None:
        if temp.data==temp.next.data:
            temp.next=temp.next.next
        else:
            temp=temp.next
    return head

def search_node(head,val):
    c=0
    while head is not None:
        if head.data==val:
            return c
        head=head.next
        c+=1
    return 'Not Found'

def display(head):
    while head is not None:
        print(head.data,end=' ')
        head=head.next


def max_node(head):
    m=head
    head=head.next
    while head is not None:
        if head.data>m.data:
            m=head
        head=head.next
    return m


def reverse_list(head):
    if head is None:
        return None
    curr=head
    prev=None
    while curr is not None:
        h=curr.next
        curr.next=prev
        prev=curr
        curr=h
    return prev


def rem_duplicates(head):
    l=[]
    while head is not None:
        if head.data not in l:
            l.append(head.data)
        head=head.next

    temp=Node(0)
    ptr=temp
    for i in l:
        n=Node(i)
        temp.next=n
        temp=temp.next

    return ptr.next

def sorted_list(head):
    l=[]
    while head is not None:
        l.append(head.data)
        head=head.next
    l.sort()
    temp=Node(0)
    ptr=temp
    for i in l:
        n=Node(i)
        temp.next=n
        temp=temp.next
    return ptr.next

def palindrome(head):
    rev=reverse_list(head)
    while head is not None:
        if head.data!=rev.data:
            return 'Not palindrome'
        head=head.next
        rev=rev.next
    return 'palindrome'

def delete_at_pos(head,k):
    c=1
    ref=head
    if k==0:
        return head.next
    while head is not None:
        if k==c:
            break
        head=head.next
        c+=1
    if head is not None:
        head.next=head.next.next
    return ref

def oddEvenList(head):
    while head is not None:
        head=head.next
    return None

def func(head):
    if head is None:
        return None
    func(head.next)
    print(head.data,end=' ')

def swap_node(head):
    if head is None:
        return None
    if head.next is None:
        return head
    a=head
    b=head.next
    while b is not None:
        temp=a.data
        a.data=b.data
        b.data=temp
        a=b.next
        if a is not None:
            b=a.next
        else:
            b=None
    return head

def middle(head):
    if head is None:
        return None
    slow=head
    fast=head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

def condensed(head):
    temp=head
    while temp.next is not None:
        if temp.data==temp.next.data:
            temp.next=temp.next.next
        else:
            temp=temp.next
    return head

#######################################################################
ob=LinkedList()
l=list(map(int,input().split()))
for i in l:
    #ob.insert_beg(i)
    ob.insert_end(i)

#display(ob.head)
print()
'''print('How many u wanna delete:')

d=int(input())
while d>0:
    ob.delete_beg()
    d-=1
display(ob.head)
s=int(input('Enter node to be searched:'))
print(search_node(ob.head,s))
n=max_node(ob.head)
print(n.data)'''
#a=reverse_list(ob.head)
#b=rem_duplicates(ob.head)
#c=sorted_list(ob.head)
#d=palindrome(ob.head)
#display(a)
#e=oddEvenList(ob.head)
#k=int(input())
#f=delete_at_pos(ob.head,k)
#f=deleteDuplicates(ob.head)
#display(f)
#func(ob.head)
#g=swap_node(ob.head)
#display(g)
#h=middle(ob.head)
#print(h.data)
p=condensed(ob.head)
display(p)
