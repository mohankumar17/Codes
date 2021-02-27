def countWays(arr, m, N):
    ans=[0 for i in range(N+1)]
    ans[0]=1
    for i in range(1,N+1):
        for j in range(m):
            if i>=arr[j]:
                ans[i]=ans[i]+ans[i-arr[j]]
    return ans[N]

arr = [1, 2, 3]
m = len(arr)
N = 6
print(countWays(arr, m, N))
