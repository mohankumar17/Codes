import sys
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
    def preConstruct(self,preord,inord):
        pass

    def postConstruct(self,preord,inord):
        pass

def postorder(root):
    if root is None:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=' ')

def preorder(root):
    if root is None:
        return None
    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)

def distRoot(root,val):
    if root.val==val:
        return 0
    if val<root.val:
        return 1+distRoot(root.left,val)
    return 1+distRoot(root.right,val)
def distBWnodes(root,x,y):
    if root is None:
        return 0

    if x<root.val and y<root.val:
        return distBWnodes(root.left,x,y)
    if x>root.val and y>root.val:
        return distBWnodes(root.right,x,y)
    if x<=root.val and y>=root.val:
        return distRoot(root,x)+distRoot(root,y)
def isSame(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.val==root2.val) and isSame(root1.left,root2.left) and isSame(root1.right,root2.right)
def isMirror(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.val==root2.val) and isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)
def isSymmetric(root):
    if root is None:
        return False
    return isMirror(root.left,root.right)
def invertTree(root):
    if root is None:
        return None
    root.left,root.right=invertTree(root.right),invertTree(root.left)
    return root
def util(root,path,pathLen,ans):
    if root is None:
        return None
    if len(path)>pathLen:
        path[pathLen]=root.val
    else:
        path.append(root.val)
    pathLen+=1

    if root.left is None and root.right is None:
        p=[i for i in path]
        ans.append(p)
    util(root.left,path,pathLen,ans)
    util(root.right,path,pathLen,ans)
def rootLeafPath(root):
    path=[]
    ans=[]
    util(root,path,0,ans)
    for i in ans:
        print(i)
def pathSum(root,s):
    if root is None:
        return False
    if root.left is None and root.right is None:
        if root.val==s:
            return True
        else:
            return False

    return pathSum(root.left,s-root.val) or pathSum(root.right,s-root.val)
class Solution:
    def maxPathSumUtil(self,root,m):
        if root is None:
            return 0
        l=self.maxPathSumUtil(root.left,m)
        r=self.maxPathSumUtil(root.right,m)

        self.m=max(max(max(max(l+root.val,r+root.val),l+r+root.val),root.val),m)
        return max(max(l,r)+root.val,root.val)


    def maxPathSum(self,root):
        self.m=-sys.maxsize
        self.maxPathSumUtil(root,self.m)
        return self.m

def Merge(root1,root2):
    if root1 is None and root2 is None:
        return None
    if root1 is None:
        return root2
    if root2 is None:
        return root1

    if root1 and root2:
        root1.val=root1.val+root2.val

    root1.left=Merge(root1.left,root2.left)
    root1.right=Merge(root1.right,root2.right)

    return root1

def constBST(start,end):
    ans=[]
    if start>end:
        ans.append(None)
        return ans

    for i in range(start,end+1):
        leftSub=constBST(start,i-1)
        rightSub=constBST(i+1,end)

        for j in range(len(leftSub)):
            left=leftSub[j]
            for k in range(len(rightSub)):
                right=rightSub[k]

                root=TreeNode(i)
                root.left=left
                root.right=right
                ans.append(root)
    return ans


def topView(root):
    if root is None:
        return None
    q=[root]
    level=0
    root.level=level
    d={}
    while len(q):
        root=q.pop(0)
        level=root.level
        if level not in d:
            d[level]=root.info
        if root.left:
            root.left.level=level-1
            q.append(root.left)
        if root.right:
            root.right.level=level+1
            q.append(root.right)
        q.pop(0)
    for i in d:
        print(d[i],end=' ')


def isBalanced(root):
    if root is None:
        return None
    q=[root]
    while len(q):
        root=q.pop(0)
        if abs(height(root.left)-height(root.right))>1:
            return False

        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)

    return True
####################################
#ob=Tree()
#pre=[4,2,1,3,6,5,7]
#inord=sorted(pre)
#root=ob.preConstruct(pre,inord)
#postorder(root)
#n=3
#ans=constBST(1,n)
#for root in ans:
#    preorder(root)
#    print()
#############################
#ob=BST()
#ar=[4,2,6,1,3,5,7,8]
#for i in ar:
#    ob.insert(i)
#inorder(ob.root)

ob1=Tree()
ob1.root=TreeNode(1)
ob1.root.left=TreeNode(2)
ob1.root.right=TreeNode(3)
#ob1.root.left.left=TreeNode(4)
ob1.root.left.right=TreeNode(4)
ob1.root.left.right.right=TreeNode(5)
ob1.root.left.right.right.right=TreeNode(6)
#ob1.root.right.left=TreeNode(6)
#ob1.root.right.right=TreeNode(7)
'''
ob2=Tree()
ob2.root=TreeNode(2)
ob2.root.left=TreeNode(4)
ob2.root.right=TreeNode(7)
ob2.root.left.left=TreeNode(4)
#ob2.root.left.right=TreeNode(3)
ob2.root.right.left=TreeNode(5)
ob2.root.right.right=TreeNode(6)

root=Merge(ob1.root,ob2.root)
preorder(root)'''
#print(distRoot(ob.root,8))
#print(distBWnodes(ob.root,1,8))
#print(isSame(ob1.root,ob2.root))
#print(isMirror(ob1.root,ob2.root))
#print(isSymmetric(ob1.root))
#preorder(ob2.root)
#r=invertTree(ob2.root)

#print()
#preorder(r)

#rootLeafPath(ob2.root)
#print(pathSum(ob2.root,14))
#s=Solution()
#print(s.maxPathSum(ob2.root))
topView(ob1.root)
