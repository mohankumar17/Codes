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

def preorder(root):
    if root is None:
        return None
    print(root.data,end=' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=' ')

ob=BinarySearchTree()
l=list(map(int,input().split()))
for i in l:
    ob.insert(i)
print('Inorder : ',end=' ')
inorder(ob.root)
print()

print('Preorder : ',end=' ')
preorder(ob.root)
print()

print('postorder : ',end=' ')
postorder(ob.root)
