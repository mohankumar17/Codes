def isSafe(grid,r,c,i,j):
    if i<0 or i>=r or j<0 or j>=c or grid[i][j]!='Y':
        return None
    grid[i][j]=0
    isSafe(grid,r,c,i-1,j)
    isSafe(grid,r,c,i+1,j)
    isSafe(grid,r,c,i,j-1)
    isSafe(grid,r,c,i,j+1)

def countFeilds(grid):
    r=len(grid)
    c=len(grid[0])
    count=0

    #isSafe(grid,r,c,0,0)
    for i in range(0,r):
        for j in range(0,c):
            if grid[i][j]=='Y':
                isSafe(grid,r,c,i,j)
                count=count+1
    print(grid)
    return count


grid=[['Y','N','N','Y'],
      ['N','Y','N','Y'],
      ['Y','N','N','N'],
      ['Y','N','Y','Y']]

import math
ans=int(math.pow(2,countFeilds(grid)-1))
print(ans%1000000007)
