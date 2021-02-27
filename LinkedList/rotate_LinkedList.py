def rotateList(head, k):
    # code here
    temp=head
    while temp.next:
        temp=temp.next

    while k>0:
        z=head
        head=head.next
        temp.next=z
        z.next=None
        temp=z
        ##################################
        k=k-1

    return head
