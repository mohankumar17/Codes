#from itertools import combinations
import math
class Solution:
    def catalyn(self,n):
        if n==0:
            return 1
        ans=[0 for i in range(n+1)]
        ans[0]=1
        ans[1]=1
        for i in range(2,n+1):
            ans[i]=0
            for j in range(0,i):
                ans[i]+=ans[j]*ans[i-j-1]
        return ans[n]

    def binomial_coefficient(self,n):
        fact=math.factorial(n)
        fact1=math.factorial(2*n)
        return (fact1)//(fact*fact*(n+1))


n=int(input())
s=Solution()
#print(s.catalyn(n))
print(s.binomial_coefficient(n))
