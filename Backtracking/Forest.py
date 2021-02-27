def countTree(ar,i,j,m,n,t):
    if i<0 or i>=m or j<0 or j>=n or ar[i][j]!='T':
        return
    ar[i][j]='F'
    t[0]=t[0]+1
    countTree(ar,i+1,j,m,n,t)
    countTree(ar,i-1,j,m,n,t)
    countTree(ar,i,j+1,m,n,t)
    countTree(ar,i,j-1,m,n,t)

def countForest(ar):
    ans=0
    c=0
    t=[0]
    m=len(ar)
    n=len(ar[0])
    for i in range(m):
        for j in range(n):
            if ar[i][j]=='T':
                countTree(ar,i,j,m,n,t)
                c=c+1
            ans=max(ans,t[0])
            t[0]=0

    print('Forests:',c)
    return ans

ar=[['T','T','T','W','W'],
    ['T','W','W','T','T'],
    ['T','W','W','T','T'],
    ['T','W','T','T','T'],
    ['W','W','T','T','T'],]

ans=countForest(ar)
print(ans)
