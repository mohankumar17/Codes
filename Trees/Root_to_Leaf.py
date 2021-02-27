
class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,val):
        node=TreeNode(val)
        node.left=None
        node.right=None
        if self.root is None:
            self.root=node
        else:
            curr=self.root
            while True:
                if val<curr.data:
                    if curr.left is None:
                        curr.left=node
                        break
                    else:
                        curr=curr.left
                if val>curr.data:
                    if curr.right is None:
                        curr.right=node
                        break
                    else:
                        curr=curr.right

def levelorder(root):
    s= [root]
    while len(s):
        root=s.pop(0)
        print(root.data,end=' ')
        if root.left is not None:
            s.append(root.left)
        if root.right is not None:
            s.append(root.right)

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)

def pathTraversal(root,path,pathlen):
    if root is None:
        return None
    if len(path)>pathlen:
        path[pathlen]=root.data
    else:
        path.append(root.data)
    pathlen+=1

    if root.left is None and root.right is None:
        for i in path:
            print(i, end=' ')
        print()
    else:
        pathTraversal(root.left,path,pathlen)
        pathTraversal(root.right,path,pathlen)

def rootLeaf(root):
    path=[]
    pathTraversal(root,path,0)

#l=list(map(int,input().split()))
l=[7,5,10,4,6,9]

ob=BST()
for i in l:
    ob.insert(i)
print('Level Order:',end=' ')
levelorder(ob.root)
print()
print('InOrder:',end=' ')
inorder(ob.root)
print()
print('Root to Leaf:')
rootLeaf(ob.root)
#mergeTrees(ob.root)


'''class Solution:
    l=[]
    def pathRec(self,root,pathLen):
        if root is None:
            return None
        path[pathLen]=root.val
        pathLen+=1
        if root.left is None and root.right is None:
            for i in path[0:pathLen]:
                print(i,end=' ')
            print()
        else:
            self.pathRec(root.left,pathLen)
            self.pathRec(root.right,pathLen)

    def sumNumbers(self, root: TreeNode) -> int:
        self.pathRec(root,0)
        return 0

    def pathfind(self,root,val):
        if root is None:
            return 0
        val=(val*10)+root.val

        if root.left is None and root.right is None:
            return val
        else:
            return self.pathfind(root.left,val)+self.pathfind(root.right,val)

    def sumNumbers(self, root: TreeNode) -> int:
        return self.pathfind(root,0)
'''
