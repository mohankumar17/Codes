class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)

def inorder_iterative(root):
    if root is None:
        return None
    s=[]
    while True:
        if root:
            s.append(root)
            root=root.left
        else:
            if len(s)==0:
                break
            root=s.pop()
            print(root.val,end=' ')
            root=root.right


ob=Tree()
ob.root=TreeNode(8)
ob.root.left=TreeNode(2)
ob.root.right=TreeNode(10)
ob.root.left.left=TreeNode(1)
ob.root.left.right=TreeNode(3)
ob.root.right.left=TreeNode(4)
ob.root.right.right=TreeNode(9)

inorder(ob.root)
print()
inorder_iterative(ob.root)
