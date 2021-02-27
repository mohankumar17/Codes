class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None

def level_order(root):
    if root is None:
        return None
    s=[root]
    while len(s):
        root=s.pop(0)
        print(root.val,end=' ')
        if root.left is not None:
            s.append(root.left)
        if root.right is not None:
            s.append(root.right)


ob=Tree()
ob.root=TreeNode(8)
ob.root.left=TreeNode(2)
ob.root.right=TreeNode(10)
ob.root.left.left=TreeNode(1)
ob.root.left.right=TreeNode(3)
ob.root.right.left=TreeNode(4)
ob.root.right.right=TreeNode(9)

level_order(ob.root)
