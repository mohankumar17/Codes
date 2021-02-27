class Solution:
    def func(self,grid,m,n,i,j):
        ans=[[0 for i in range(n)] for j in range(m)]

        ans[0][0]=grid[0][0]
        for j in range(1,n):
            ans[0][j]=ans[0][j-1]+grid[0][j]
        for i in range(1,m):
            ans[i][0]=ans[i-1][0]+grid[i][0]
        
        for i in range(1,m):
            for j in range(1,n):
                ans[i][j]=grid[i][j]+min(ans[i][j-1],ans[i-1][j])

        return ans[m-1][n-1]


    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        #print(grid)
        return self.func(grid,m,n,0,0)

s=Solution()
grid=[[1,3,1],
      [1,5,1],
      [4,2,1]]
print(s.minPathSum(grid))
