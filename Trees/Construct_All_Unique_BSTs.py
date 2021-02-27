class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root=None
    def preorder(self,root):
        if root is None:
            return None
        print(root.val,end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

class Solution:
    def generateTrees(self, A):
        def constructTrees(start,end):
            ans=[]
            if (start > end) :
                ans.append(None)
                return ans

            for i in range(start, end + 1):
                leftSubtree = constructTrees(start, i - 1)
                rightSubtree = constructTrees(i + 1, end)

                for j in range(len(leftSubtree)) :
                    left = leftSubtree[j]
                    for k in range(len(rightSubtree)):
                        right = rightSubtree[k]
                        node = TreeNode(i)   # making value i as root
                        node.left = left    # connect left subtree
                        node.right = right    # connect right subtree
                        ans.append(node)    # add this tree to list
            return ans

        return constructTrees(1,A)

ob=BST()
s=Solution()
A=3
ans=s.generateTrees(A)
for root in ans:
    ob.preorder(root)
    print()
