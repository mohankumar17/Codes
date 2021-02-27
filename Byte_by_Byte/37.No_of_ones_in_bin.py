def setbit(n):
    n=bin(n)
    n=n[2:]
    ans=n.count('1')
    return ans

print(setbit(0))
print(setbit(1))
print(setbit(2))
print(setbit(10))
print(setbit(13))
print(setbit(15))
