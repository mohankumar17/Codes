# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def func(self,root,ans,p):
        if root is None:
            return None

        p=(p*10)+root.val

        if root.left is None and root.right is None:
            #print(p)
            self.ans=self.ans+p

        self.func(root.left,ans,p)
        self.func(root.right,ans,p)

    def sumNumbers(self, root):
        self.ans=0
        self.func(root,0,0)
        return self.ans%1003
