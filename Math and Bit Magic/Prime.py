def isPrime(n):
    g=int(n**0.5)
    for i in range(2,g+1):
        if n%i==0:
            return False
    return True

n=int(input())
print(isPrime(n))
