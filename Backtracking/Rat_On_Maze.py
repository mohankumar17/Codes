def isSafe(maze,n,x,y):
    if x<0 or x>n-1 or y<0 or y>n-1 or maze[x][y]!=1:
        return False
    return True
    #if x>=0 and x<=n-1 and y>=0 and y<=n-1 and maze[x][y]==1:
    #    return True
    #return False

def rat(maze,n,ans,x,y):
    if x==n-1 and y==n-1 and maze[x][y]==1:
        ans[x][y]=1
        return True
    if isSafe(maze,n,x,y):
        ans[x][y]=1
        if rat(maze,n,ans,x+1,y):
            return True
        if rat(maze,n,ans,x,y+1):
            return True
        ans[x][y]=0
        return False


def display(ans):
    for i in ans:
        print(i)

#n=int(input())
n=4
maze=[[1,1,0,0],
      [0,1,0,1],
      [0,1,0,1],
      [1,1,1,1]]
ans=[[0 for i in range(n)] for i in range(n)]

if rat(maze,n,ans,0,0):
    display(ans)
else:
    print('Not Possible')
