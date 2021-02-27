def commElements(ar):
    m=len(ar)
    n=len(ar[0])
    d={}
    for i in range(m):
        for j in range(n):
            d[ar[i][j]]=d.get(ar[i][j],0)+1
    ans=[]
    for i in d:
        if d[i]>=m:
            ans.append(i)
    return ans

ar=[[5,2,3,8],
    [3,2,2,5],
    [5,3,2,9]]

ans=commElements(ar)
print(ans)
