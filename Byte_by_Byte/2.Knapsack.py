def knapsack(weights,values,capacity,n):
    if n==0:
        return 0
    if weights[n-1]>capacity:
        return knapsack(weights,values,capacity,n-1)
    return max(values[n-1]+knapsack(weights,values,capacity-weights[n-1],n-1),knapsack(weights,values,capacity,n-1))

def knapsackDP(weights,values,capacity,n):
    ans=[[0 for i in range(capacity+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if weights[i-1]>j:
                ans[i][j]=ans[i-1][j]
            else:
                ans[i][j]=max(ans[i-1][j-weights[i-1]]+values[i-1],ans[i-1][j])

    return ans[n][capacity]

weights=[1,2,3]
values=[6,10,12]
capacity=3
n=len(weights)
print(knapsack(weights,values,capacity,n))
print(knapsackDP(weights,values,capacity,n))
