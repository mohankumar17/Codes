def knapsack(W,wt,v,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]>W:
        return knapsack(W,wt,v,n-1)
    else:
        return max(v[n-1]+knapsack(W-wt[n-1],wt,v,n-1),knapsack(W,wt,v,n-1))

wt=[2,3,4,5]  #weights of items
v=[1,2,5,6]  #values of items
n=len(wt)  #total no.of.items
W=8 #capacity of knapsack
print(knapsack(W,wt,v,n))
