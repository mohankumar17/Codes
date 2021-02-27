def isPalin(n):
    t=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==t:
        return True
    else:
        return False

n=int(input())
print(isPalin(n))
