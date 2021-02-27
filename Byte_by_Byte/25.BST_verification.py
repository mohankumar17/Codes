class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None

def isBST(root,l,r):
    if root is None:
        return True
    if l and l.val>root.val:
        return False
    if r and r.val<root.val:
        return False
    return isBST(root.left,l,root) and isBST(root.right,root,r)

ob=Tree()
ob.root=TreeNode(5)
ob.root.left=TreeNode(2)
ob.root.right=TreeNode(7)
ob.root.left.left=TreeNode(1)
ob.root.left.right=TreeNode(3)
ob.root.right.left=TreeNode(6)
ob.root.right.right=TreeNode(8)

print(isBST(ob.root,None,None))
