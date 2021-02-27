import math
def trailZeros(n):
    n=math.factorial(n)
    print(n)
    c=0
    while n>0:
        if n%10==0:
            c=c+1
        else:
            break
        n=n//10
    return c

n=int(input())
print(trailZeros(n))
