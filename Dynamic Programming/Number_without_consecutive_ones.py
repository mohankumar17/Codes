def func(n):
    fib=[0]*(n+1)
    fib[0]=1
    fib[1]=2

    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n]

n=5
print(func(n))
