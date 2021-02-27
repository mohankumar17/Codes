class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def func(self,postorder,inorder,m,n):
        if n<m:
            return None
        root=TreeNode(postorder[self.ind])
        curr=root

        j=-1
        x=m
        while m<=n:
            if inorder[x]==postorder[self.ind]:
                j=x
                break
            x=x+1

        #j=inorder.index(postorder[self.ind])
        #print('------------------',j)
        self.ind-=1
        root.right=self.func(postorder,inorder,j+1,n)
        root.left=self.func(postorder,inorder,m,j-1)

        return curr

    def insert(self,postorder):
        self.ind=len(postorder)-1
        inorder=list(sorted(postorder))
        return self.func(postorder,inorder,0,len(postorder)-1)

def preorder(root):
    if root is None:
        return None
    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)

postorder=[2,4,3,6,8,7,5]
ob=BST()
root=ob.insert(postorder)
preorder(root)
