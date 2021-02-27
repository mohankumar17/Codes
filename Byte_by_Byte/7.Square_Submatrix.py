def subarray(mat):
    m=len(mat)
    n=len(mat[0])
    ans=[[0 for i in range(n)] for i in range(m)]

    for i in range(0,m):
        ans[i][0]=mat[i][0]

    for j in range(0,n):
        ans[0][j]=mat[0][j]

    for i in range(0,m):
        for j in range(0,n):
            if mat[i][j]==1:
                ans[i][j]=1+min(mat[i-1][j],mat[i][j-1],mat[i-1][j-1])
            else:
                ans[i][j]=0

    h=0
    for i in range(0,m):
        for j in range(0,n):
            if ans[i][j]>h:
                h=ans[i][j]
    return h

'''
mat=[[ 1 , 1 , 1 , 0 ],
     [ 1 , 1 , 1 , 1 ],
     [ 1 , 1 , 0 , 0 ]]'''

mat=[[ 1 , 1 , 1 , 0 ],
     [ 1 , 1 , 1 , 1 ],
     [ 1 , 1 , 1 , 0 ]]

print(subarray(mat))
