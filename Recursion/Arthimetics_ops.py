def add(ar,n):
    if n==0:
        return 0
    return ar[n-1]+add(ar,n-1)

def product(ar,n):
    if n==0:
        return 1
    return ar[n-1]*product(ar,n-1)

ar=[4,3,5,1,2]
print(add(ar,len(ar)))
print(product(ar,len(ar)))
