def minCostPath(ar):
    m=len(ar)
    n=len(ar[0])
    ans=ar.copy()

    for i in range(1,m):
        ans[i][0]+=ans[i-1][0]
    for j in range(1,n):
        ans[0][j]+=ans[0][j-1]

    for i in range(1,m):
        for j in range(1,n):
            t=min(ans[i-1][j],ans[i][j-1])
            ans[i][j]+=t

    for i in ans:
        print(i)

    return ans[m-1][n-1]

ar=[[1,3,5,8],
    [4,2,1,7],
    [4,3,2,3]]

print(minCostPath(ar))
