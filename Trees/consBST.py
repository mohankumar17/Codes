class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insVal(self,preorder,inorder):
        if len(inorder)==0:
            return None
        x=preorder.pop(0)
        ind=inorder.index(x)

        root=Node(x)
        root.left=self.insVal(preorder,inorder[0:ind])
        root.right=self.insVal(preorder,inorder[ind+1:])
        return root

def postorder(root):
    if root is None:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=' ')

def pathTrav(root,path,pathLen):
    if root is None:
        return None
    if len(path)>pathLen:
        path[pathLen]=root.val
    else:
        path.append(root.val)
    pathLen+=1

    if root.left is None and root.right is None:
        for i in path:
            print(i,end=' ')
        print()
    else:
        pathTrav(root.left,path,pathLen)
        pathTrav(root.right,path,pathLen)

ob=BST()
preorder=[5,3,2,4,7,6,8]
inorder=sorted(preorder)
a=ob.insVal(preorder,inorder)
#print('postorder:',end=' ')
#postorder(a)
print()
path=[]
pathTrav(a,path,0)
