def maxSteal(ar):
    if len(ar)==0:
        return 0
    if len(ar)==1:
        return ar[0]
    if len(ar)==2:
        return max(ar[0],ar[1])

    a=0 #including
    b=0 #excluding
    for i in range(len(ar)):
        t=a
        a=max(a,b+ar[i])
        b=t
        
    return a

ar=[4,1,1,4,6,1]
print(maxSteal(ar))
