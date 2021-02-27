class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

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


def display(head):
    while head is not None:
        print(head.data,end=' ')
        head=head.next

def reverse_q(head):
    prev=None
    curr=head
    nex=None
    while curr is not None:
        nex=curr.next
        curr.next=prev
        prev=curr
        curr=nex
    return prev

#######################################################################
ob=LinkedList()
l=list(map(int,input().split()))
for i in l:
    ob.insert_end(i)
#display(ob.head)
print()
c=reverse_q(ob.head)
display(c)
