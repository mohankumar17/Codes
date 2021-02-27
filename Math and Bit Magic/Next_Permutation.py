class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        n=len(A)
        i=n-2
        while i>=0:
            if A[i]<A[i+1]:
                break
            i=i-1
        if i==-1:
            A=A[::-1]
            return A
        else:
            j=i+1
            while j<n:
                if A[j]<=A[i]:
                    break
                j=j+1

            A[i],A[j-1]=A[j-1],A[i]
            A=A[0:i+1]+sorted(A[i+1:])
            return A
s=Solution()
A=[2,3,1]
ans=s.nextPermutation(A)
print(ans)
