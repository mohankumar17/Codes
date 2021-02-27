def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

n=4
print(fact(n))
