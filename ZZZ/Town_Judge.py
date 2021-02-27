from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d=defaultdict(list)
        for i in range(len(trust)):
            if trust[i][0]!=trust[i][1]:
                d[trust[i][0]].append(trust[i][1])
        print(d)
        if len(d)!=N-1:
            return -1

        #return -1
        s1=[i for i in range(1,N+1)]
        s1=set(s1)
        for i in d:
            s2=set(d[i])
            s1=s1&s2
        print(s1)
        if len(s1)==1:
            x=s1.pop()
            if x in d:
                return -1
            else:
                return x
        return -1
            
