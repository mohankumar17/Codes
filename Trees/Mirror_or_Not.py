class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def Mirror(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return ((root1.data==root2.data) and Mirror(root1.left,root2.right) and Mirror(root1.right,root2.left))


root1=Node(5)
root1.left=Node(2)
root1.right=Node(7)
root1.left.left=Node(1)
root1.left.right=Node(3)
root1.right.left=Node(6)
root1.right.right=Node(8)

root2=Node(5)
root2.left=Node(7)
root2.right=Node(2)
root2.left.left=Node(8)
root2.left.right=Node(6)
root2.right.left=Node(3)
root2.right.right=Node(1)

'''root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)'''

print(Mirror(root1,root2))
