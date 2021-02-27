class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d={}
        for i in A[0]:
            d[i]=d.get(i,0)+1

        for i in range(1,len(A)):
            ans={}
            t={}
            for j in A[i]:
                t[j]=t.get(j,0)+1
            #print(d)
            for j in t:
                #print(j)
                if j in d:
                    ans[j]=min(d[j],t[j])
            #print(ans)

            d={}
            for j in ans:
                d[j]=ans[j]

        res=''
        for i in d:
            res=res+(i*d[i])
        return res
