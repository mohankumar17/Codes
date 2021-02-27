def LPCell(mat,ans,i,j,n):
    if i<0 or i>=n or j<0 or j>=n:
        return 0
    if ans[i][j]!=-1:
        return ans[i][j]
    w,x,y,z=-1,-1,-1,-1
    if j<n-1 and mat[i][j]+1==mat[i][j+1]:
        w=1+LPCell(mat,ans,i,j+1,n)
    if j>0 and mat[i][j]+1==mat[i][j-1]:
        x=1+LPCell(mat,ans,i,j-1,n)
    if i<n-1 and mat[i][j]+1==mat[i+1][j]:
        y=1+LPCell(mat,ans,i+1,j,n)
    if i>0 and mat[i][j]+1==mat[i-1][j]:
        z=1+LPCell(mat,ans,i-1,j,n)

    ans[i][j]=max(z,max(y,max(x,max(w,1))))
    return ans[i][j]


def LongestPath(mat):
    res=1
    n=len(mat)
    ans=[[-1 for i in range(n+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if ans[i][j]==-1:
                LPCell(mat,ans,i,j,n)
            res=max(res,ans[i][j])
    return res


mat=[[1, 2, 9],
     [5, 3, 10],
     [4, 6, 7]]
print(LongestPath(mat))
