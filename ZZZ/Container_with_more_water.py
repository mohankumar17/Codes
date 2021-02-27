class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        if n==0:
            return 0
        if n==2:
            return min(height[0],height[1])
        l=0
        r=n-1
        res=0
        while l<=r:
            m=min(height[l],height[r])
            m=m*(r-l)
            if m>res:
                res=m

            if height[l]>height[r]:
                r=r-1
            else:
                l=l+1

        return res
    
