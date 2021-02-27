def sum_w(a,b):
    while b!=0:
        c=a&b
        a=a^b
        b=c<<1
    return a

def sub_w(a,b):
    while b!=0:
        c=~a&b
        a=a^b
        b=c>>1
    return a

a=5
b=3
print(sum_w(a,b))
print(sub_w(a,b))
