def matrix_prod(mat,m,n,i,j,t):
    if i==m or j==n:
        return t
    t=t*mat[i][j]
    a=matrix_prod(mat,m,n,i+1,j,t)
    b=matrix_prod(mat,m,n,i,j+1,t)
    return max(a,b)

'''
mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]'''
mat=[[-1 , 2 , 3 ],
[ 4 , 5 , -6 ],
[ 7 , 8 , 9 ]]

'''mat=[[1,1,1],
     [1,2,1],
     [1,3,4]]'''
m=len(mat)
n=len(mat[0])
x=matrix_prod(mat,m,n,0,0,1)
print(x)
