'''def setBits(b):
    if b==0:
        return 0
    l=''
    for i in range(1,b+1):
        l=l+bin(i)

    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    return d['1']
'''
def setBits(n):
    n=n+1
    p=2
    c=n//2
    while p<=n:
        t=n//p
        c=c+(t//2)*p
        if t&1:
            c=c+(n%p)
        p=p<<1
    return c

n=int(input())
print(setBits(n))
