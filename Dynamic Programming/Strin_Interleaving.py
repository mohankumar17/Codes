def stringInterleave(s1,s2,s3):
    m=len(s2)
    n=len(s1)
    if (m+n)!=len(s3):
        return False

    ans=[[False for i in range(n+1)] for i in range(m+1)]
    ans[0][0]=True

    for j in range(n+1):
        if s1[j-1]==s3[j-1]:
            ans[0][j]=True

    for i in range(m+1):
        if s2[i-1]==s3[i-1]:
            ans[i][0]=True

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s2[i-1]==s3[i+j-1]:
                ans[i][j]=ans[i-1][j]

            elif s1[j-1]==s3[i+j-1]:
                ans[i][j]=ans[i][j-1]
    for i in ans:
        print(i)

    return ans[m][n]


s1='aab'
s2='axy'
#s3='aaxaby'
s3='abxaay'
print(stringInterleave(s1,s2,s3))
