def cuttRod(ar,v,l):
    n=len(ar)
    ans=[[0 for i in range(l+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,l+1):
            if j>=ar[i-1]:
                ans[i][j]=max(ans[i-1][j],v[i-1]+ans[i][j-ar[i-1]])
            else:
                ans[i][j]=ans[i-1][j]

    return ans[n][l]

#ar=[1,2,3,4]
#v=[2,5,7,8]
ar=[i for i in range(1,9)]
v=[1,5,8,9,10,17,17,20]
l=8
print(cuttRod(ar,v,l))

'''def cuttingRod(n,prices):
    if n<=0:
        return 0
    cost=0
    for i in range(0,n):
        cost=max(cost,prices[i]+cuttingRod(n-i-1,prices))
    return cost

def cuttingRodDp(n,prices):
    ans=[0 for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(0,i):
            ans[i]=max(ans[i],prices[j]+ans[i-j-1])
    return ans[n]

n=8
prices=[1,5,8,9,10,17,17,20]
print(cuttingRod(n,prices))
print(cuttingRodDp(n,prices))
'''
