def zeroSum(ar):
    n=len(ar)
    if 0 in ar:
        return [0]
    if sum(ar)==0:
        return ar

    length=2
    while length<=n-2:
        for i in range(0,n-length+1):
            x=ar[i:i+length]
            #print(x)
            if sum(x)==0:
                return x
        length+=1

ar=[1,2,-5,1,2,1]
ans=zeroSum(ar)
print(ans)  #[2,-5,1,2]
