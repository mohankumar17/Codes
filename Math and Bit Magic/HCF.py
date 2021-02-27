def hcf(a,b):
    if a<b:
        a,b=b,a
    t=b
    while b!=0:
        t=b
        b=a%b
        a=t
    return t

def lcm(a,b):
    if a>b:
        a,b=b,a
    #t=b
    x=b
    s=1
    while s!=0:
        #t=b
        s=b%a
        b=b+x
    return b-x

a,b=map(int,input().split())
print(hcf(a,b))
print(lcm(a,b))
