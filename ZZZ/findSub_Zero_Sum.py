def zeroSumSub(ar,n):
    c=0
    s=0
    t=[]
    d={}
    for i in range(n):
        s=s+ar[i]
        if s==0:
            t.append([0,i])
            c=c+1
        a=[]
        if s in d:
            a=d.get(s)
            for j in range(len(a)):
                t.append([a[j]+1,i])
                c=c+1
        a.append(i)
        d[s]=a
    return c,t

ar=[6,-1,-3,4,-2,2]
ans=zeroSumSub(ar,len(ar))
print(ans)
