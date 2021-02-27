#Given a sorted array, remove the duplicates in place
#such that each element can appear atmost twice and return the new length.
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i=0
        j=0
        n=len(A)
        while i<n:
            t=A[i]
            count=0
            while (i+1)<n and A[i]==A[i+1]:
                count=count+1
                i=i+1

            if count==0:
                A[j]=t
                j=j+1
            elif count>=1:
                A[j]=t
                j=j+1
                A[j]=t
                j=j+1

            i=i+1

        return j


#Given a sorted array, remove the duplicates in place
#such that each element appears only once and return the new length.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        while i<len(nums):
            t=nums[i]
            c=1
            while (i+1)<len(nums) and nums[i]==nums[i+1]:
                c=c+1
                i=i+1

            if c>=1:
                nums[j]=t
                j=j+1

            i=i+1

        return j
