class Solution:
	def maxProduct(self,ar, n):
	    maxV=ar[0]
	    minV=ar[0]
	    maxP=ar[0]
	    for i in range(1,n):
	        if ar[i]<0:
	            maxV,minV=minV,maxV
	        minV=min(ar[i],ar[i]*minV)
	        maxV=max(ar[i],ar[i]*maxV)

	        maxP=max(maxP,maxV)
	    return maxP

s=Solution()
ar=[3,-6,-10,0,2]
ans=s.maxProduct(ar,len(ar))
print(ans)
