class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def pathSum(root,B):
    if root is None:
        return False
    if root.left is None and root.right is None:
        if root.data==B:
            return True
        else:
            return False

    return pathSum(root.left,B-root.data) or pathSum(root.right,B-root.data)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)

B=10
print(pathSum(root,B))