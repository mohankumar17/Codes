def LPS(s):
    T='$#'
    for i in s:
        T=T+i+'#'
    T=T+'@'

    n=len(T)
    P=[0]*n
    C=0
    R=0
    for i in range(1,n-1):
        mir=2*C-i
        if i<R:
            P[i]=min(R-i,P[mir])

        while T[i+(1+P[i])]==T[i-(1+P[i])]:
            P[i]+=1

        if 1+P[i]>R:
            C=i
            R=1+P[i]

    return max(P)

#s='ABABABA'
s='ABABDBA'
print(LPS(s))
