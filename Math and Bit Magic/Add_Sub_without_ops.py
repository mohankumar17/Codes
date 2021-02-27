def add(a,b):
    while b>0:
        c=a&b
        a=a^b
        b=c<<1
    return a

def sub(a,b):
    f=1
    if a<b:
        f=-1
        a,b=b,a

    while b>0:
        c=(~a)&b
        a=a^b
        b=c<<1

    return f*a

a,b=2,1
print(add(a,b))
print(sub(a,b))
