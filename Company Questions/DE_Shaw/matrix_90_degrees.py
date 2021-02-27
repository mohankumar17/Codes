import numpy
def matrixRotate(m):
    r=len(m)
    #c=len(m[0])
    res=[]
    #for i in range(r):
    #    t=[]
    #    for j in range(c):
    #        t.append(m[j][i])
    #    res.append(t)
    res=numpy.transpose(m)
    i=0
    j=0
    for i in range(r):
        for j in range(r//2):
            res[i][j],res[i][r-j-1]=res[i][r-j-1],res[i][j]
    return res

m=[[11,12,13,22],
   [14,15,16,24],
   [17,18,19,27],
   [10,25,26,28]]
res=matrixRotate(m)
for i in res:
    print(i)
#op=[[7,4,1],
#   [8,5,2],
#   [9,6,3]]
