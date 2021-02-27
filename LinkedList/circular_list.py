class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class CircularList:
    def __init__(self):
        self.head=None

    def insert_beg(self,val):
        n=Node(val)
        if self.head is None:
            self.head=n
            self.head.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next

            n.next=self.head
            self.head=n
            temp.next=self.head

    ############################################

    def insert_end(self,val):
        n=Node(val)
        if self.head is None:
            self.head=n
            self.head.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=n
            n.next=self.head

class Solution:
    def get_p(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow
        return None

    def detectCycle(self, head):
        p = self.get_p(head)
        if p is None:
            return None
        while p.next != head:
            p=p.next
            head=head.next
        return head


def removeLoop(head):
    # code here
    # remove the loop without losing any nodes
    if head is None or head.next is None:
        return None
    slow=head.next
    fast=head.next.next
    while fast and fast.next:
        if slow==fast:
            break
        slow=slow.next
        fast=fast.next.next

    if slow==fast:
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next

        temp=slow
        while temp.next!=slow:
            temp=temp.next
        temp.next=None
    return head

def display(head):
    temp=head
    while temp.next!=head:
        print(temp.val,end=' ')
        temp=temp.next
    print(temp.val)

ob=CircularList()
l=[1,2,3,4,5]
for i in l:
    #ob.insert_beg(i)
    ob.insert_end(i)

display(ob.head)
