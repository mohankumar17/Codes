class Solution:
    # @param A : root node of tree
    # @return an integer
    def util(self, A, B):
        if A is None and B is None:
            return True
        if A is None or B is None:
            return False
        return (A.val == B.val) and self.util(A.left, B.right) and self.util(A.right, B.left)

    def isSymmetric(self, A):
        if self.util(A.left, A.right):
            return 1
        else:
            return 0