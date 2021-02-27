def func(ar):
    m=len(ar)
    n=len(ar[0])
    ans=[[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if ar[i-1][j-1]==1:
                ans[i][j]=min(ans[i-1][j],ans[i-1][j-1],ans[i][j-1])+1

    for i in ans:
        print(i)

    return ans[m][n]

ar=[[0,0,1,1,1],
    [1,0,1,1,1],
    [0,1,1,1,1],
    [1,0,1,1,1]]

print(func(ar))
