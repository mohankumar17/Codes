class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        c=0
        n=len(A)
        ans=[1 for i in range(n)]
        for i in range(0,n-1):
            if A[i]<A[i+1]:
                ans[i+1]=ans[i]+1

        for i in range(n-1,0,-1):
            if A[i]<A[i-1] and ans[i-1]<=ans[i]:
                ans[i-1]=ans[i]+1

        return sum(ans)
