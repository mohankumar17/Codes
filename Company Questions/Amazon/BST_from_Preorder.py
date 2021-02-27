class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def func(self,preorder,inorder,m,n):
        if n<m:
            return None

        root=TreeNode(preorder[self.ind])
        curr=root

        j=-1
        x=m
        while m<=n:
            if inorder[x]==preorder[self.ind]:
                j=x
                break
            x=x+1

        j=inorder.index(preorder[self.ind])
        self.ind+=1
        root.left=self.func(preorder,inorder,m,j-1)
        root.right=self.func(preorder,inorder,j+1,n)

        return curr

    def insert(self,preorder):
        self.ind=0
        #inorder=list(sorted(preorder))
        inorder=[2,1,3]
        return self.func(preorder,inorder,0,len(preorder)-1)

def postorder(root):
    if root is None:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=' ')

preorder=[1,2,3]
ob=BST()
root=ob.insert(preorder)
postorder(root)
