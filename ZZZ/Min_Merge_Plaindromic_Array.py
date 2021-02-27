def func(ar,n):
    i=0
    j=n-1
    c=0
    while i<j:
        if ar[i]==ar[j]:
            i=i+1
            j=j-1

        elif ar[i]>ar[j]:
            ar[j-1]=ar[j]+ar[j-1]
            j-=1
            c=c+1

        else:
            ar[i+1]=ar[i]+ar[i+1]
            i+=1
            c=c+1
    return c

t=int(input())
while t>0:
    t-=1
    n=int(input())
    ar=list(map(int,input().split()))
    print(func(ar,n))
