def rotate(ar):
    n=len(ar)
    for i in range(n//2):
        for j in range(i,n-i-1):
            t=ar[i][j]
            ar[i][j]=ar[n-j-1][i]
            ar[n-j-1][i]=ar[n-i-1][n-j-1]
            ar[n-i-1][n-j-1]=ar[j][n-i-1]
            ar[j][n-i-1]=t
    return ar

ar=[[1,2,3],
    [4,5,6],
    [7,8,9]]

ans=rotate(ar)
for i in ans:
    print(i)
