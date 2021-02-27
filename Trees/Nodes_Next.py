class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.next=None
class Tree:
    def __init__(self):
        self.root=None

def func(root):
    if root is None:
        return None
    q=[root]
    while len(q):
        s=len(q)
        while s>0:
            root=q.pop(0)
            print(root.val,end=' ')
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            s=s-1
        print()

def util(root):
    if root is None:
        return None
    q=[root]
    while len(q):
        s=len(q)
        while s>0:
            root=q.pop(0)
            root.next=None
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            s=s-1
        print()

ob=Tree()
ob.root=Node(1)
ob.root.left=Node(2)
ob.root.right=Node(3)
ob.root.left.left=Node(4)
ob.root.left.right=Node(5)
ob.root.right.left=Node(6)
#ob.root.right.right=Node(6)
func(ob.root)
print()
util(ob.root)
func(ob.root)
