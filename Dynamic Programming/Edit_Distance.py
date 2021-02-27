#recursive
def ED(s1,s2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1]==s2[n-1]:
        return ED(s1,s2,m-1,n-1)
    else:
        return 1+min(ED(s1,s2,m-1,n),ED(s1,s2,m,n-1),ED(s1,s2,m-1,n-1))
#DP
def EDdp(s1,s2,m,n):
    ans=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(0,m+1):
        for j in range(0,n+1):
            if i==0:
                ans[i][j]=j
            if j==0:
                ans[i][j]=i
            elif s1[i-1]==s2[j-1]:
                ans[i][j]=ans[i-1][j-1]
            else:
                ans[i][j]=1+min(ans[i-1][j],ans[i][j-1],ans[i-1][j-1])
    return ans[m][n]
#######################

def ED2(s1,s2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1]==s2[n-1]:
        return ED(s1,s2,m-1,n-1)
    else:
        return 1+min(ED(s1,s2,m-1,n),ED(s1,s2,m,n-1),ED(s1,s2,m-1,n-1))


s1="food"
s2="money"
m=len(s1)
n=len(s2)
cost=ED(s1,s2,m,n)
print(cost)

cost=EDdp(s1,s2,m,n)
print(cost)
