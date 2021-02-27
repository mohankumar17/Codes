def wildCardMatch(s,pattern):
    m=len(s)
    n=len(pattern)
    ans=[[False for i in range(n+1)] for i in range(m+1)]
    ans[0][0]=True

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==pattern[j-1] or pattern[j-1]=='?':
                ans[i][j]=ans[i-1][j-1]
            elif pattern[j-1]=='*':
                ans[i][j]=ans[i-1][j] or ans[i][j-1]
            else:
                ans[i][j]=False
    #for i in ans:
    #    print(i)
    return ans[m][n]

s='xaylmz'
pattern='x?y*z'
print(wildCardMatch(s,pattern))
