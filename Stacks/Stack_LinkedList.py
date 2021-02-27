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

def display_str(head):
    while head is not None:
        print(head.data,end='')
        head=head.next

#######################################################################
ob=LinkedList()
s=input()
#l=list(map(int,input().split()))
for i in s:
    ob.insert_beg(i)
#print(a)
#display_str(ob.head)
