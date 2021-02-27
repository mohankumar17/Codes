class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class CircularList:
    def __init__(self):
        self.head=None

    ############################################

    def insert_end(self,val):
        n=Node(val)
        if self.head is None:
            self.head=n
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=n

    def insert(self,val):
        n=Node(val)
        if n.val<=self.head.val:
            n.next=self.head
            self.head=n
        else:
            temp=self.head
            f=0
            while temp and temp.next:
                if n.val>=temp.val and n.val<=temp.next.val:
                    s=temp.next
                    temp.next=n
                    n.next=s
                    f=1
                    break

                temp=temp.next

            if f==0:
                if temp.next is None:
                    temp.next=n

def display(head):
    temp=head
    while temp:
        print(temp.val,end=' ')
        temp=temp.next

ob=CircularList()
l=[1,2,3,4]
for i in l:
    ob.insert_end(i)
display(ob.head)
print()
ob.insert(5)
display(ob.head)
