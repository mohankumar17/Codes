def deleteNode(curr_node):
    while curr_node.next.next:
        curr_node.data=curr_node.next.data
        curr_node=curr_node.next

    curr_node.data=curr_node.next.data
    curr_node.next=None
