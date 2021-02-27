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

s=0
def sum_nodes(root):
    global s
    if root is None:
        return s
    sum_nodes(root.left)
    if root.left is None and root.right is None:
      s=s+root.data
    return sum_nodes(root.right)

ob=BinarySearchTree()
l=list(map(int,input().split()))
for i in l:
    ob.insert(i)
print('Inorder : ',end=' ')
inorder(ob.root)
print()

s=sum_nodes(ob.root)
print('sum of all leaf nodes:',s)
