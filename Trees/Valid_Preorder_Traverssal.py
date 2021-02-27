class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        s=[]
        import sys
        m=-sys.maxsize
        for i in range(0,len(A)):
            if A[i]<m:
                return 0
            if s and A[i]>s[-1]:
                m=s.pop()
            s.append(A[i])
        return 1
