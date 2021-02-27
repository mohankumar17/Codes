def binomial(n,k):
    ans=[[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(0,n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                ans[i][j]=1
            else:
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
    return ans[n][k]

def bin_rec(n,k):
    if k==0 or k==n:
        return 1
    return bin_rec(n-1,k-1)+bin_rec(n-1,k)

n=6
k=2
print(binomial(n,k))
#print(bin_rec(n,k))
