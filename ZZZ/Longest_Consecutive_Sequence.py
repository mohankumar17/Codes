class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
	    A=list(set(A))
	    A.sort()
	    c=1
	    m=0
	    for i in range(0,len(A)-1):
	        if A[i]+1==A[i+1]:
	            c=c+1
	        else:
	            if c>m:
	                m=c
	            c=1
	    return max(m,c)
