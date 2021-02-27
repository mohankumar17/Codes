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

def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))
def diameter(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)

    ldiameter=diameter(root.left)
    rdiameter=diameter(root.right)

    return max(lheight+rheight+1,max(ldiameter,rdiameter))
#################
def height2(root):
    if root is None:
        return 0
    lheight=height(root.left,ar)
    rheight=height(root.right,ar)

    ar[0]=max(ar[0],lh+rh+1)
    return 1+max(height2(root.left,ar),height2(root.right,ar))


def diameter2(root):
    if root is None:
        return 0
    ar=[-sys.maxsize]
    height2(root,ar)
    return ar[0]
##############
ob=BinarySearchTree()
l=list(map(int,input().split()))
for i in l:
    ob.insert(i)
print('Inorder : ',end=' ')
inorder(ob.root)
print()

d=diameter(ob.root)
print('Diameter : ',d)
