'''def func(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return func(n-1)+func(n-2)'''

def func(n):
    if n==0:
        return 0
    fib=[0 for i in range(n+1)]
    fib[1]=1
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n]

n=int(input())
print(func(n))
