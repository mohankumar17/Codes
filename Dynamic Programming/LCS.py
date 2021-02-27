
#recursive
def LCS(s1,s2,m,n):
    if m==0 or n==0:
        return 0
    if s1[m-1]==s2[n-1]:
        return 1+LCS(s1,s2,m-1,n-1)
    else:
        return max(LCS(s1,s2,m,n-1),LCS(s1,s2,m-1,n))
#DP
def LCSDP(s1,s2,m,n):
    ans=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(0,m+1):
        for j in range(0,n+1):
            if i==0 or j==0:
                ans[i][j]=0
            elif s1[i-1]==s2[j-1]:
                ans[i][j]=ans[i-1][j-1]+1
            else:
                ans[i][j]=max(ans[i][j-1],ans[i-1][j])

    return ans[m][n]


##########################
#s1="mohankumarkothala"
#s2="xtvhankuarpala"
s1="bebdeeedaddecebbbbbabebedc"
s2="abaaddaabbedeedeacbcdcaaed"
m=len(s1)
n=len(s2)
#ans="hankuarala"
#ans=LCS(s1,s2,m,n)
#print(ans)

ans=LCSDP(s1,s2,m,n)
print(ans)
