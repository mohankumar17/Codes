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

def delM(head,m,n):
    if head is None:
        return head
    temp=head
    while True:
        t=m
        while t>1:
            temp=temp.next
            if temp is None:
                return head
            t-=1
        z=n
        while z>0:
            if temp.next is None:
                return head
            temp.next=temp.next.next
            z-=1

        #print(temp.val)
        temp=temp.next
        if temp is None:
            return head

    return head


###################################################
ob=LinkedList()
m,n=map(int,input().split())
l=[1,2,3,4,5,6,7,8,9,1]

for i in l:
    ob.insert_end(i)
display(ob.head)
print()

h=delM(ob.head,m,n)
display(h)
