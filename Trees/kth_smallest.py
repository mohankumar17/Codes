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
t=[]
def inorder(root):
    global t
    if root is None:
        return t
    inorder(root.left)
    print(root.data,end=' ')
    t.append(root.data)
    return inorder(root.right)


def levelorder(root,k):
    q=[]
    q.append(root)
    while len(q)>0:
        x=q.pop(0)
        if k==0:
            return x.data
        k-=1
        if x.left is not None:
            q.append(x.left)
        if x.right is not None:
            q.append(x.right)


def kth(root,k):
    #l=inorder(root)
    #print()
    #return l[k]
    l=levelorder(root,k)
    return l

ob=BinarySearchTree()
'''a=int(input())
while a>=0:
  ob.insert(a)
  a=int(input())'''
l=list(map(int,input().split()))
for i in l:
    ob.insert(i)

l=inorder(ob.root)
print()
print('Enter the kth value:',end=' ')
k=int(input())
print()
ans=kth(ob.root,k)
print('Smallest kth value',ans)
