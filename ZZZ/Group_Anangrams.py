from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        l=[]
        d=defaultdict(list)
        for s in strs:
            t=list(sorted(s))
            t=''.join(t)
            d[t].append(s)

        for i in d:
            l.append(d[i])
        return l

s=Solution()
strs=["eat", "tea", "tan", "ate", "nat", "bat","ant"]
print(s.groupAnagrams(strs))
