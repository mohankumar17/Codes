import math
def kthPerm(n,k):
    ar=[i for i in range(1,n+1)]
    ans=''
    while len(ar):
        f=math.factorial(len(ar)-1)
        i=k//f
        if k%f==0:
            i=i-1
        ans=ans+str(ar[i])
        k=k-f*i
        ar.pop(i)

    return ans

n=3
k=4
print(kthPerm(n,k))



'''import math
class Solution:
    def getPermutation(self, A, B):
        arr=[i for i in range(1,A+1)]
        ans=""
        while len(arr):
            f=(math.factorial(len(arr)-1))

            index=B//f
            if(B%f==0):
                index-=1

            ans+=str(arr[index])
            B=B-f*index

            arr.remove(arr[index])
        return(ans)

s=Solution()
print(s.getPermutation(3,4))
'''
