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

def inorder_iterative(root):
    s=[]
    while True:
        if root is not None:
            s.append(root)
            root=root.left

        elif len(s):
            root=s.pop()
            print(root.data,end=' ')
            root=root.right
        else:
            break

ob=BinarySearchTree()
#l=list(map(int,input().split()))
l=[5 ,2 ,7 ,1 ,3 ,6 ,8]
for i in l:
    ob.insert(i)
print('Inorder : ',end=' ')
#inorder(ob.root)
inorder_iterative(ob.root)
print()
