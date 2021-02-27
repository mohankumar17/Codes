class Solution:
    def getPairsCount(self, arr, n, k):
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        c=0
        for i in range(n):
            if k-arr[i] in d:
                c=c+d[k-arr[i]]
            if k-arr[i]==arr[i]:
                c=c-1

        return c//2

s=Solution()
ar=[1,5,7,1]
n=4
k=6
ans=s.getPairsCount(arr,n,k)
print(ans)
