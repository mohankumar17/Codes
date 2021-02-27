def util(s,i,j):
    n=len(s)
    dp=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n):
        dp[i][i]=1
    for l in range(2,n+1):
        for i in range(0,n-l+1):
            k=i+l-1
            if s[i]==s[k]:
                dp[i][k]=dp[i+1][k]+dp[i][k-1]+1
            else:
                dp[i][k]=dp[i+1][k]+dp[i][k-1]-dp[i+1][k-1]

    return dp[0][n-1]

def countPs(s):
    # Code here
    ans=util(s,0,len(s)-1)
    return ans

s='aab'
ans=countPs(s)
print(ans)
