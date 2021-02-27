class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def levelorder(root):
    s=[]
    s.append(root)
    while len(s):
        root=s.pop(0)
        print(root.data,end=' ')
        if root.left is not None:
            s.append(root.left)
        if root.right is not None:
            s.append(root.right)

def mergeTrees(root1,root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    if root1 is not None and root2 is not None:
        root1.data=root1.data+root2.data
    root1.left=mergeTrees(root1.left,root2.left)
    root1.right=mergeTrees(root1.right,root2.right)

    return root1

root1=TreeNode(7)
root1.left=TreeNode(5)
root1.right=TreeNode(10)
root1.left.left=TreeNode(4)
root1.left.right=TreeNode(6)
root1.right.left=TreeNode(9)

root2=TreeNode(5)
root2.left=TreeNode(3)
root2.right=TreeNode(7)
root2.left.right=TreeNode(4)
root2.right.right=TreeNode(10)

root=mergeTrees(root1,root2)
levelorder(root)
