def zero_matrix(mat):
    temp=mat.copy()
    row=[]
    col=[]
    for i in range(0,len(temp)):
        for j in range(0,len(temp[0])):
            if temp[i][j]==1:
                row.append(i)
                col.append(j)
    for i in row:
        for j in range(0,len(mat[0])):
            mat[i][j]=1
    for j in col:
        for i in range(0,len(mat)):
            mat[i][j]=1
    #return mat

mat=[[1,0,0],
     [0,0,0],
     [0,0,0]]
zero_matrix(mat)
for i in mat:
    print(i)
