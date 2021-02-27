def isSafe(m,row,col,n):
    for i in range(0,col):
        if m[row][i]==1:
            return False
        i=row
        j=col
        while i>=0 and j>=0:
            if m[i][j]==1:
                return False
            i=i-1
            j=j-1

        i=row
        j=col
        while i<n and j>=0:
            if m[i][j]==1:
                return False
            i=i+1
            j=j-1

    return True

def nqueens(m,col,n):
    if col>=n:
        return True
    for i in range(0,n):
        if isSafe(m,i,col,n):
            m[i][col]=1
            if nqueens(m,col+1,n):
                return True
            m[i][col]=0
    return False

def display(m):
    for i in m:
        print(i)

n=int(input())
m=[[0 for i in range(n)] for i in range(n)]

#m=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
#m =    [ [0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0] ]

if nqueens(m,0,n):
    display(m)
else:
    print('Not Possible')
