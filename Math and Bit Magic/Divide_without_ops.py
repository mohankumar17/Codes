def divide(a,b):
    s=1
    if a<0 or b<0:
        s=-1
    a=abs(a)
    b=abs(b)
    q=0
    while a>=b:
        a=a-b
        q=q+1
    return s*q

def power(n):
    c=0
    for i in range(n):
        c=c+n
    return c

a=18
b=3
#ans=divide(a,b)
#print(ans)

ans=power(18)
print(ans)
