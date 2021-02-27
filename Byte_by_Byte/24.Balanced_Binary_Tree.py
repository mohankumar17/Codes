class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None

def height(a):
    if a is None:
        return 0
    return 1+max(height(a.left),height(a.right))

def isBalanced(root):
    if root is None:
        return True
    f=height(root.left)-height(root.right)
    if f not in [0,-1,1]:
        return False
    isBalanced(root.left)
    return isBalanced(root.right)

ob=Tree()
ob.root=TreeNode(1)
ob.root.left=TreeNode(2)
ob.root.right=TreeNode(3)
ob.root.left.left=TreeNode(4)
ob.root.left.right=TreeNode(5)
ob.root.right.left=TreeNode(6)
ob.root.right.left.right=TreeNode(7)
ob.root.right.right=TreeNode(8)

print(isBalanced(ob.root))
