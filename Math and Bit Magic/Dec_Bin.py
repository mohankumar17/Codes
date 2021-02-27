def bin2dec(b):
    b=b[::-1]
    d=0
    for i in range(len(b)):
        d=d+(int(b[i])*(2**i))
    return d

b='1001'
d=bin2dec(b)
print(d)

def dec2bin(d):
    if d==0:
        return '0'
    b=''
    while d>=1:
        b=b+str(d%2)
        d=d//2
    return b[::-1]

print(dec2bin(d))
