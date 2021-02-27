def rev(b,bit):
    b=bin(d)
    b=b[2:]
    n=len(b)
    b=('0'*(bit-n))+b
    print(b[::-1])
    ans=0
    for i in range(bit):
        ans+=int(b[i])*(2**i)
    return ans

d=6
bit=5
print(rev(d,bit))
