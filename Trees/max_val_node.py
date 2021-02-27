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

m=0
def inorder(root):
    global m
    if root is None:
        return m
    inorder(root.left)
    m=root.data
    return inorder(root.right)

def levelorder(root):
    m=0
    q=[]
    q.append(root)
    while len(q)>0:
        x=q.pop(0)
        if x.data>m:
            m=x.data
        if x.left is not None:
            q.append(x.left)
        if x.right is not None:
            q.append(x.right)
    return m


def max_node(root):
    #m=inorder(root)
    m=levelorder(root)
    return m


ob=BinarySearchTree()
l=list(map(int,input().split()))
for i in l:
    ob.insert(i)

m=max_node(ob.root)
print('Maximum value node:',m)
