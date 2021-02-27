'''import sys
def minCoins(coins,amount):
    n=len(coins)
    ans=[[sys.maxsize for i in range(amount+1)] for j in range(n+1)]
    for j in range(amount+1):
        ans[1][j]=0
    for i in range(n+1):
        ans[i][0]=0

    for i in range(1,n+1):
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                ans[i][j]=min(ans[i-1][j],1+ans[i][j-coins[i-1]])
            else:
                ans[i][j]=ans[i-1][j]

    return ans[n][amount]

coins=[1,2,3,5,7,10,100]
amount=int(input())
ans=minCoins(coins,amount)
print(ans)
'''

import sys
def minCoins(coins,n,amount):
    ans=[0 for i in range(amount+1)]
    for i in range(1,amount+1):
        ans[i]=sys.maxsize
    for i in range(1,amount+1):
        for j in range(0,n):
            if coins[j]<=i:
                s=ans[i-coins[j]]
                if s!=sys.maxsize and s+1<ans[i]:
                    ans[i]=s+1
    return ans[amount]

#amount=int(input())
amount=84
#coins=[1,2,5]
coins=[1,2,3,5,7,10,100]
n=len(coins)
print(minCoins(coins,n,amount))
