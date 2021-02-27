def prodCutRod(n):
    if n==0 or n==1:
        return 0
    if n==2:
        return 1
    cost=0
    for i in range(1,n-1):
        cost=max(cost,max((n-i)*i,prodCutRod(n-i)*i))
    return cost

def prodCutRodDP(n):
    if n==0 or n==1:
        return 0
    if n==2:
        return 1

    ans=[0 for i in range(n+1)]
    for i in range(3,n+1):
        for j in range(1,i-1):
            ans[i]=max(ans[i],max((i-j)*j,ans[i-j]*j))
    return ans[n]


n=int(input())
#print(prodCutRod(n))
print(prodCutRodDP(n))
