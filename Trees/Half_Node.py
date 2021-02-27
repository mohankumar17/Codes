# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, root):
        if root is None:
            return None
        root.left=self.solve(root.left)
        root.right=self.solve(root.right)
        if root.left is None and root.right is None:
            return root
        if root.left is None and root.right is not None:
            new_root=root.right
            a=root
            root=None
            del(a)
            return new_root

        if root.right is None and root.left is not None:
            new_root=root.left
            a=root
            root=None
            del(a)
            return new_root

        return root
