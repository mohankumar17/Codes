def maxProfit(ar):
    n=len(ar)
    if n==1:
        return ar[0]
    a=ar[0]
    if n==2:
        return max(ar[0],ar[1])
    b=max(ar[0],ar[1])
    for i in range(2,n):
        t=b
        b=max(b,ar[i]+a)
        a=t
    return b


ar=[5,5,10,100,10,5]
ans=maxProfit(ar)
print(ans)
