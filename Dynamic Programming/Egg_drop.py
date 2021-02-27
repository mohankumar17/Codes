import sys
def eggDrop(n,k):
    if k==0 or k==1:
        return k
    if n==1:
        return k

    m=sys.maxsize
    for x in range(1,k+1):
        trails=max(eggDrop(n-1,x-1),eggDrop(n,k-x))
        if trails<m:
            m=trails
    return m+1

def eggDropdp(n,k):
    ans=[[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(1,n+1):
        ans[i][0]=0
        ans[i][1]=1
    for j in range(1,k+1):
        ans[1][j]=j
    for i in range(2,n+1):
        for j in range(2,k+1):
            ans[i][j]=sys.maxsize
            for x in range(1,j+1):
                trails=1+max(ans[i-1][x-1],ans[i][j-x])
                if trails<ans[i][j]:
                    ans[i][j]=trails

    return ans[n][k]

#n=int(input())
#k=int(input())
n=4
k=50
#print(eggDrop(n,k))
print(eggDropdp(n,k))
