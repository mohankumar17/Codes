def isSubsetSum(set, n, sum):
    if sum==0:
        return True
    if n==0 and sum!=0:
        return False
    if set[n-1]>sum:
        return isSubsetSum(set,n-1,sum)
    return  isSubsetSum(set,n-1,sum) or isSubsetSum(set,n-1,sum-set[n-1])

def isSubsetSumDP(set, n, sum):
    ans=[[False for i in range(sum+1)] for i in range(n+1)]
    for i in range(n+1):
        ans[i][0]=True
    for i in range(1,sum+1):
        ans[0][i]=False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if set[i-1]>j:
                ans[i][j]=ans[i-1][j]
            if set[i-1]<=j:
                ans[i][j]=ans[i-1][j] or ans[i-1][j-set[i-1]]

    return ans[n][sum]

set = [34,1]
sum = 68    
n=len(set)
print(isSubsetSum(set, n, sum))
print(isSubsetSumDP(set, n, sum))
