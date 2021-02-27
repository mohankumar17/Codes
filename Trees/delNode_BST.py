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
##############################
def MaxNode(z,m):
    if z is None:
        return None
    MaxNode(z.left,m)
    m[0]=z
    MaxNode(z.right,m)

def MinNode(z,m,c):
    if z is None:
        return None
    if c==1:
        m[0]=z
    MinNode(z.left,m,c)
    c=c+1
    MinNode(z.right,m,c)

def deleteNode(root,key):
    m=[root]
    MaxNode(root.left,m)
    print('Inorder Preceedor : ',m[0].data)

    m=[root]
    MinNode(root.right,m,1)
    print('Inorder Successor : ',m[0].data)

##############################
ob=BinarySearchTree()
l=[10,5,15,3,6,12,17,2,4,11,18,3,8]
#l=[10,15,12,17]
for i in l:
    ob.insert(i)
inorder(ob.root)
print()
ans=deleteNode(ob.root,ob.root)
#inorder(ans)
