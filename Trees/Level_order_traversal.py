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

def levelorder(root):
    q=[]
    q.append(root)
    while len(q)>0:
        x=q.pop(0)
        print(x.data,end=' ')
        if x.left is not None:
            q.append(x.left)
        if x.right is not None:
            q.append(x.right)

def levelorder_printline(root):
    if root is None:
        return None
    q=[]
    ans=[]
    q.append(root)
    while len(q):
        x=len(q)
        t=[]
        while x>0:
            root=q.pop(0)
            t.append(root.data)
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
            x=x-1
        ans.append(t)
    print(ans)

#########################################################
'''ob=BinarySearchTree()
l=list(map(int,input().split()))
for i in l:
    ob.insert(i)
print('Inorder : ',end=' ')
inorder(ob.root)
print()

print('Level Order:',end=' ')
levelorder(ob.root)
print()'''

print('Level Order Line by Line:')
root = Node(3);
root.left = Node(9);
root.right = Node(20);
root.right.left = Node(15);
root.right.right = Node(17);
levelorder_printline(root)
