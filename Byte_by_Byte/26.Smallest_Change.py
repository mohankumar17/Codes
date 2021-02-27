import sys
def smallChange(coins,amount,n):
    '''if amount==0:
        return 0
    res=sys.maxsize
    for i in range(0,n):
        if coins[i]<=amount:
            sub=smallChange(coins,amount-coins[i],n)
            if sub!=sys.maxsize and sub+1<res:
                res=sub+1
    return res'''

    ans=[sys.maxsize for i in range(amount+1)]
    ans[0]=0
    for i in range(1,amount+1):
        for j in range(n):
            if coins[j]<=i:
                sub=ans[i-coins[j]]
                if sub!=sys.maxsize and sub+1<ans[i]:
                    ans[i]=sub+1
    return ans[amount]

coins=[1,2,5]
amount=int(input())
n=len(coins)
#ans=2
print(smallChange(coins,amount,n))
