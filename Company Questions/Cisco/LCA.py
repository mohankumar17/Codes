class Node:
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

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)

def lca(root,a,b):
    if root is None:
        return None
    if root.data==a or root.data==b:
        return root
    l=lca(root.left,a,b)
    r=lca(root.right,a,b)
    if l and r:
        return root
    if l is not None:
        return l
    else:
        return r

ob=BinarySearchTree()
#l=list(map(int,input().split()))
l=[5,3,7,2,4,6,8,1]
for i in l:
    ob.insert(i)
print('Inorder : ',end=' ')
inorder(ob.root)
print()
a,b=map(int,input().split())
x=lca(ob.root,a,b)
if x is not None:
    print(x.data)
else:
    print(-1)
