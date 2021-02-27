def sumSubset(arr,n,s):
    if s==0:
        return True
    if n==0 and s!=0:
        return False
    if arr[n-1]>s:
        return sumSubset(arr,n-1,s)
    return sumSubset(arr,n-1,s) or sumSubset(arr,n-1,s-arr[n-1])

def findPartion(arr,n):
    s=sum(arr)
    if s%2!=0:
        return False
    return sumSubset(arr,n,s//2)


def findPartionDP(set, n):
    sum=0
    for i in set:
        sum=sum+i
    if sum%2!=0:
        return False
    sum=sum//2

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

#arr = [3, 1, 5, 9, 12]
#arr = [2,6,2,6]
arr=[2,6,1,7]
n = len(arr)
print(findPartion(arr, n))
print(findPartionDP(arr, n))
