'''class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort(reverse=True)
        return max(A[0]*A[1]*A[2],A[-1]*A[-2]*A[0])
'''

def max3Prod(ar):
    ar.sort()
    return max(ar[0]*ar[1]*ar[-1],ar[-1]*ar[-2]*ar[-3])

ar=[-3,2,8,4,-5]
print(max3Prod(ar))
