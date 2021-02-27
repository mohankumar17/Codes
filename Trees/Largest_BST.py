class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

def level(root):
    temp=ob.root
    q=[temp]
    while len(q):
        root=q.pop(0)
        print(root.val,end=' ')
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)
############################################
def isBST(root,l,r,f):
    if root is None:
        f[0]=f[0]+1
        return True
    if l and l.val>=root.val:
        return False
    if r and r.val<=root.val:
        return False
    return isBST(root.left,l,root,f) and isBST(root.right,root,r,f)

##########################
ob=Tree()
ob.root=TreeNode(10)
ob.root.left=TreeNode(18)
ob.root.right=TreeNode(20)
ob.root.left.left=TreeNode(14)
ob.root.left.right=TreeNode(11)
ob.root.right.left=TreeNode(19)
ob.root.right.right=TreeNode(18)

ob.root.left.left.left=TreeNode(12)
ob.root.left.left.right=TreeNode(15)

ob.root.right.right.left=TreeNode(17)
ob.root.right.right.right=TreeNode(21)
ob.root.right.right.left.left=TreeNode(16)

ob.root.right.right.right.left=TreeNode(20)
ob.root.right.right.right.right=TreeNode(22)

#######################

ans=largestBST(ob.root)

for i in ans:
    print(i.val,end=' ')
print()
for i in ans:
    level(ans)
    print()
