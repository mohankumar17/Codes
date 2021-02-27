# Definition for a  binary tree node
import sys
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root=None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def func(self,root,m):
        if root is None:
            return 0
        l=self.func(root.left,self.m)
        r=self.func(root.right,self.m)
        self.m=max(max(max(max(l+root.val,r+root.val),l+r+root.val),root.val),self.m)
        return max(max(l,r)+root.val,root.val)

    def maxPathSum(self, root):
        self.m=-sys.maxsize
        self.func(root,self.m)
        return self.m

s=Solution()

ob2=Tree()
ob2.root=TreeNode(2)
ob2.root.left=TreeNode(4)
ob2.root.right=TreeNode(6)
ob2.root.left.left=TreeNode(1)
ob2.root.left.right=TreeNode(3)
ob2.root.right.left=TreeNode(5)
ob2.root.right.right=TreeNode(7)

ans=s.maxPathSum(ob2.root)
print(ans)
