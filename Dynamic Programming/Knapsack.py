def knapsack(v,w,n,c):
    if n==0:
        return 0
    if w[n-1]>c:
        return knapsack(v,w,n-1,c)
    return max(v[n-1]+knapsack(v,w,n-1,c-w[n-1]),knapsack(v,w,n-1,c))

def knapsackDP(v,w,n,c):
    ans=[[0 for i in range(c+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            if w[i-1]>j:
                ans[i][j]=ans[i-1][j]
            else:
                ans[i][j]=max(v[i-1]+ans[i-1][j-w[i-1]],ans[i-1][j])
    return ans[n][c]

w=[2,3,4,5]  #weights of items
#v=[1,2,5,6]  #values of items
v=[11,2,5,6]  #values of items
n=len(w)  #total no.of.items
c=8 #capacity of knapsack
print(knapsack(v,w,n,c))
print(knapsackDP(v,w,n,c))


'''#recursive approach
def knapsack(W,wt,v,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]>W:
        return knapsack(W,wt,v,n-1)
    else:
        return max(knapsack(W-wt[n-1],wt,v,n-1)+v[n-1],knapsack(W,wt,v,n-1))
#Dynamic programming approach
def knapsackdp(W,wt,v,n):
    k=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,W+1):
            if i==0 or j==0:
                k[i][j]=0
            elif wt[i-1]>j:
                k[i][j]=k[i-1][j]
            else:
                k[i][j]=max(v[i-1]+k[i-1][j-wt[i-1]],k[i-1][j])
    return k[n][W]
#########################################
#w=list(map(int,input().split()))
wt=[2,3,4,5]  #weights of items
v=[1,2,5,6]  #values of items
n=len(wt)  #total no.of.items
W=8 #capacity of knapsack
cost=knapsack(W,wt,v,n)
print(cost)

cost=knapsackdp(W,wt,v,n)
print(cost)
'''
