def equilibriumPoint(ar, N):
    if N==1:
        return 1
    p=-1
    s=sum(ar)
    t=0
    for i in range(N):
        s=s-ar[i]
        if s==t:
            return i+1
        t=t+ar[i]
    return -1

ar=[3,5,1,2]
N=len(ar)
print(equilibriumPoint(ar,N))
