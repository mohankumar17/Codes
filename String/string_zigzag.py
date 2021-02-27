from collections import defaultdict
class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, s, n):
        if n==1:
            return s

        d=defaultdict(list)
        for i in range(0,len(s)):
            t=i%(2*n-2)
            t=min(t,(2*n-2)-t)
            d[t].append(s[i])

        ans=[]
        #print(d)
        for i in d:
            ans=ans+d[i]
        ans=''.join(ans)
        return ans
