def waysN(ar,total,n):
    if total==0:
        return 1
    if n==0:
        return 0
    if ar[n-1]>total:
        return waysN(ar,total,n-1)

    return waysN(ar,total,n-1)+waysN(ar,total-ar[n-1],n)

def waysDP(ar,amount,n):
    ans=[[0 for i in range(amount+1)] for j in range(n+1)]
    for i in range(n+1):
        ans[i][0]=1

    for j in range(amount+1):
        ans[0][j]=0

    for i in range(1,n+1):
        for j in range(1,amount+1):
            if ar[i-1]>j:
                ans[i][j]=ans[i-1][j]
            else:
                ans[i][j]=ans[i][j-ar[i-1]]+ans[i-1][j]
    return ans[n][amount]

ar=[1,2,3]
total=124
n=len(ar)
print(waysN(ar,total,n))
print(waysDP(ar,total,n))

'''def func(coins,amount,n):
    if amount==0:
        return 1
    if n<=0 and amount>=1:
        return 0
    if amount<0:
        return 0
    return func(coins,amount,n-1)+func(coins,amount-coins[n-1],n)

def funcDP(S,N,m):
    m=len(S)
    table = [0 for k in range(N+1)]
    table[0] = 1
    for i in range(0,m):
        for j in range(S[i],N+1):
            table[j] += table[j-S[i]]
    return table[N]

coins=[1,2,3]
#coins=[ 7, 10, 2, 11, 19, 15, 21, 5, 24, 16, 30, 23, 18, 17, 14, 27, 20, 22 ]
amount=124
#print(func(coins,amount,len(coins)))
print(funcDP(coins,amount,len(coins)))
'''
