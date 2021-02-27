def stairCase(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return n
    return stairCase(n-1)+stairCase(n-2)

def stairCaseDP(n):
    dp=[0 for i in range(n+1)]
    dp[1]=1
    dp[2]=2

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

n=13
print(stairCase(n))
print(stairCaseDP(n))
