class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

ob=Tree()
ob.root=TreeNode(1)
ob.root.left=TreeNode(2)
ob.root.right=TreeNode(3)
ob.root.left.left=TreeNode(4)
ob.root.left.right=TreeNode(5)
ob.root.right.left=TreeNode(6)
ob.root.right.right=TreeNode(7)

q=[ob.root]
while len(q):
    root=q.pop(0)
    print(root.val,end=' ')
    if root.left is not None:
        q.append(root.left)
    if root.right is not None:
        q.append(root.right)
