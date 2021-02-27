def nearestSmaller(ar):
    n=len(ar)
    ans=[-1]*n
    s=[]
    for i in range(1,n):
        if ar[i]>ar[i-1]:
            ans[i]=ar[i-1]
            s.append(ar[i-1])
        else:
            while len(s):
                if ar[i]>s[-1]:
                    ans[i]=s[-1]
                    break
                s.pop()
    return ans

#ar=[4,3,8,9,7]
#ar=[1,2,5,6,8,3]
ar=[3,6,4,2,8]
ans=nearestSmaller(ar)
print(ans)


'''class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        n=len(A)
        ans=[-1]*n
        q=[]
        for i in range(0,n):
            while len(q):
                if A[i]>q[-1]:
                    ans[i]=q[-1]
                    break
                else:
                    q.pop()

            q.append(A[i])
        return ans

s=Solution()
A=[1,2,5,6,8,3]
ans=s.prevSmaller(A)
print(ans)'''
