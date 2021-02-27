def LISdp(l,n):
    LIS=[1 for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if l[i]>l[j] and LIS[j]+1>LIS[i]:
                LIS[i]=LIS[j]+1
    return max(LIS)

l=[50, 3, 10, 7, 40, 50, 80,1,2,3,4,5,6,7,8,9]
n=len(l)
print(LISdp(l,n))
