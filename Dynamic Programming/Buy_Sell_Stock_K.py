import sys
def BuySell(prices,k):
    n=len(prices)
    ans=[[0 for i in range(n)] for j in range(k+1)]
    for i in range(1,k+1):
        for j in range(1,n):
            maxDiff=-sys.maxsize
            for m in range(0,j):
                t=(ans[i-1][m]-prices[m])
                if t>maxDiff:
                    maxDiff=t
            ans[i][j]=max(ans[i][j-1],maxDiff+prices[j])

    for i in ans:
        print(i)

    return ans[k][n-1]


prices=[2,5,7,1,4,3,1,3]
k=3
print(BuySell(prices,k))
