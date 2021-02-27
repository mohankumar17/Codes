def dup(ar):
    ans=[]
    d={}
    for i in ar:
        d[i]=d.get(i,0)+1
    for i in d:
        if d[i]>1:
            ans.append(i)
    return ans

ar=[1,2,3,4,5,3,2]
print(dup(ar))
