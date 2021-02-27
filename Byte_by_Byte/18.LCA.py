class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None

def LCA(root,a,b):
    if root is None:
        return None
    if root.val==a or root.val==b:
        return root
    l=LCA(root.left,a,b)
    r=LCA(root.right,a,b)

    if l and r:
        return root
    if l is not None:
        return l
    else:
        return r

ob=Tree()
ob.root=TreeNode(1)
ob.root.left=TreeNode(2)
ob.root.right=TreeNode(3)
ob.root.left.left=TreeNode(4)
ob.root.left.right=TreeNode(5)
ob.root.right.left=TreeNode(6)
ob.root.right.right=TreeNode(7)
ans=LCA(ob.root,4,3)
print(ans.val)

ans=LCA(ob.root,6,7)
print(ans.val)

ans=LCA(ob.root,4,5)
print(ans.val)
