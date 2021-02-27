def func(s,n):
    LIS=[1 for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if s[i]>s[j] and LIS[j]+1>LIS[i]:
                LIS[i]=LIS[j]+1
    print(LIS)
    return max(LIS)

s=[1,10,5,3,4]
n=len(s)
print(func(s,n))
