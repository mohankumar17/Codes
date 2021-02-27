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

def ca(root,a,b):
    if root is None:
        return None
    if a<root.data and b<root.data:
        return ca(root.left,a,b)
    if a>root.data and b>root.data:
        return ca(root.right,a,b)
    return root

'''def lowestCommonAncestor(root,p,q):
    if root is None:
        return None

    if p==root.data or q==root.data:
        return root
    a=lowestCommonAncestor(root.left,p,q)
    b=lowestCommonAncestor(root.right,p,q)

    if a and b:
        return root

    if a is not None:
        return a
    else:
        return b'''

def lowestCommonAncestor(root,p,q):
    if root is None:
        return None

    if p==root.data or q==root.data:
        return root
    if p<root.data and q<root.data:
        root=lowestCommonAncestor(root.left,p,q)
    if p>root.data and q>root.data:
        root=lowestCommonAncestor(root.right,p,q)

    #if p<root.data and q>root.data:
    #    return root
    #else:
    #    return
    return root    

    #if a is not None:
    #    return a
    #else:
    #    return b

ob=BinarySearchTree()
l=list(map(int,input().split()))
for i in l:
    ob.insert(i)
print('Inorder : ',end=' ')
inorder(ob.root)
print()

print('Enter two nodes:',end=' ')
a,b=map(int,input().split())
ans=lowestCommonAncestor(ob.root,a,b)
print('Common ancestor:',ans.data)
