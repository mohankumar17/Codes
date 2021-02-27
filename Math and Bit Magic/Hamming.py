class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        ans=0
        for i in range(0,32):
            x=0
            for j in range(len(A)):
                if int(A[j] & 1<<i):
                    x=x+1
            y=len(A)-x
            ans+=(x*y*2)
        return ans%(10**9+7)
