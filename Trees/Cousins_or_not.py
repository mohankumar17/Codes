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

class Solution:
    def func(self,curr,parent,val,h):
        if curr is None:
            return 0

        if curr.data==val:
            return h

        self.parent=curr.data
        left_h=self.func(curr.left,parent,val,h+1)
        if left_h!=0:
            return left_h

        self.parent=curr.data
        right_h=self.func(curr.right,parent,val,h+1)
        return right_h

    def Cousins(self,root,x,y):
        if root.data==x or root.data==y:
            return False

        xh=self.func(root,-1,x,0)
        xparent=self.parent

        yh=self.func(root,-1,y,0)
        yparent=self.parent

        if xh==yh and xparent!=yparent:
            return True
        return False

ob=BinarySearchTree()
#l=list(map(int,input().split()))
l=[5 ,3 ,7 ,2 ,4 ,6 ,8]
for i in l:
    ob.insert(i)
#print('Inorder : ',end=' ')
#inorder(ob.root)
x,y=map(int,input().split())
S=Solution()
print(S.Cousins(ob.root,x,y))
