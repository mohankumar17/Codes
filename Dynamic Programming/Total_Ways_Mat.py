ar=[[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]

def totalWays(ar):
    m=len(ar)
    n=len(ar[0])
    ans=[[0 for i in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 or j==0:
                ans[i][j]=1
            else:
                ans[i][j]=ans[i-1][j]+ans[i][j-1]
    return ans[m-1][n-1]

#ar=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
print(totalWays(ar))
