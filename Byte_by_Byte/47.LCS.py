def LCS(s1,s2,m,n):
    '''
    if m==0 or n==0:
        return 0
    if s1[m-1]==s2[n-1]:
        return 1+LCS(s1,s2,m-1,n-1)
    return max(LCS(s1,s2,m,n-1),LCS(s1,s2,m-1,n))'''

    ans=[[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[j-1]==s2[i-1]:
                ans[i][j]=1+ans[i-1][j-1]
            else:
                ans[i][j]=max(ans[i-1][j],ans[i][j-1])
    for i in ans:
        print(i)
    return ans[n][m]

s1="ABAB"
s2="BABA"
print(LCS(s1,s2,len(s1),len(s2)))
