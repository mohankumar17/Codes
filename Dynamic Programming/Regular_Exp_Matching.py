def regexMatch(s,pattern):
    m=len(s)
    n=len(pattern)
    ans=[[False for i in range(n+1)] for j in range(m+1)]
    ans[0][0]=True
    #for i in range(1,m+1):
    #    ans[i][0]=False
    #for j in range(1,n+1):
    #    ans[0][j]=False

    for j in range(1,n+1):
        if pattern[j-1]=='*':
            ans[0][j]=ans[0][j-2]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==pattern[j-1] or pattern[j-1]=='.':
                ans[i][j]=ans[i-1][j-1]
            elif pattern[j-1]=='*':
                ans[i][j]=ans[i][j-2]
                if s[i-1]==pattern[j-2] or pattern[j-2]=='.':
                    ans[i][j]=ans[i][j] or ans[i-1][j]
            else:
                ans[i][j]=False

    return ans[m][n]

s='xaabyg'
pattern='xa*b.g'
print(regexMatch(s,pattern))
