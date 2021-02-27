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

def levelordertraversal(root):
    if root is None:
        return None
    q=[]
    q.append(root)
    ans=[]
    while len(q):
        root=q.pop(0)
        ans.append(root.data)
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)

    return ans

def levelordertraversal_2(root):
    if root is None:
        return None
    q=[]
    q.append(root)
    ans=[]
    while len(q):
        c=len(q)
        t=[]
        while c>0:
            root=q.pop(0)
            t.append(root.data)
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
            c=c-1
        ans.append(t)

    return ans


ob=BinarySearchTree()
#l=list(map(int,input().split()))
l=[5, 3, 7, 2, 4, 6, 8, 1]
for i in l:
    ob.insert(i)
print('Inorder : ',end=' ')
inorder(ob.root)
print()

print('Level-order : ',end=' ')
ans=levelordertraversal(ob.root)
print(ans)

print('Level-order 2 : ',end=' ')
ans=levelordertraversal_2(ob.root)
print(ans)
