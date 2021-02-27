import sys
def func(arr,n,total,calc):
    if n==0:
        return abs((total-calc)-calc)
    return min(func(arr,n-1,total,calc),func(arr,n-1,total,calc+arr[n-1]))

def MinPartition(arr):
    n=len(arr)
    total=sum(arr)
    return func(arr,n,total,0)

def MinPartitionDP(arr):
    n=len(arr)
    su=0
    su = sum(arr)
    dp = [[0 for i in range(su + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for j in range(1, su + 1):
        dp[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, su + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] = (dp[i][j]) | (dp[i - 1][j - arr[i - 1]])

    diff = sys.maxsize

    # Find the largest j such that dp[n][j]
    # is true where j loops from sum/2 to 0
    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break

    return diff


#arr=[3, 1, 4, 2, 2, 1]
arr=[2,5,6,11]
print(MinPartition(arr))
print(MinPartitionDP(arr))
