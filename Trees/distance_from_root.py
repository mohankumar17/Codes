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

def distRoot(root,val):
    if root is None:
        return 0
    if root.val==val:
        return 0
    if root.left:
        return 1+distRoot(root.left,val)
    return 1+distRoot(root.right,val)
####################################
ob=Tree()
ob.root=TreeNode(2)
ob.root.left=TreeNode(4)
ob.root.right=TreeNode(6)
ob.root.left.left=TreeNode(1)
ob.root.left.right=TreeNode(3)
ob.root.right.left=TreeNode(5)
ob.root.right.right=TreeNode(7)
ob.root.right.right.right=TreeNode(8)

print(distRoot(ob.root,7))


'''class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        n=Node(data)
        if self.root is None:
            self.root=n
        else:
            curr=self.root
            while True:
                if data<curr.data:
                    if curr.left is None:
                        curr.left=n
                        break
                    else:
                        curr=curr.left

                elif data>curr.data:
                    if curr.right is None:
                        curr.right=n
                        break
                    else:
                        curr=curr.right
                else:
                    break

###########################3
def Distance_from_root(root,x):
    if root.data==x:
        return 0
    if x<root.data:
        return 1+Distance_from_root(root.left,x)
    return 1+Distance_from_root(root.right,x)

ob=BinarySearchTree()
l=list(map(int,input().split()))
for i in l:
    ob.insert(i)
x=int(input())
print(Distance_from_root(ob.root,x))


'''
