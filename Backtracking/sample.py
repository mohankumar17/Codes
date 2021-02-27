def isSafe(ar,i,j,m,n):
    if i<0 or i>=m or j<0 or j>=n or ar[i][j]==0:
        return False
    return True

def ratMaze(ar,m,n,i,j,ans):
    if i==m-1 and j==n-1 and ar[i][j]==1:
        ans[i][j]=1
        return True
        
    if isSafe(ar,i,j,m,n):
        ans[i][j]=1
        if ratMaze(ar,m,n,i,j+1,ans):
            return True
        if ratMaze(ar,m,n,i+1,j,ans):
            return True
        ans[i][j]=0
        return False


ar=[[1,0,1,1],
    [1,1,1,0],
    [1,0,1,1],
    [1,1,0,1]]
m=len(ar)
n=len(ar[0])
ans=[[0 for i in range(m)] for j in range(n)]
if ratMaze(ar,m,n,0,0,ans):
    for i in ans:
        for j in i:
            print(j,end=' ')
        print()
else:
    print(-1)
