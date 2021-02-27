def dec(b):
    d=0
    i=len(b)-1
    j=0
    while i>=0:
        c=int(b[i])
        d=d+((2**j)*c)
        i=i-1
        j=j+1
    return d

def binary(n):
    s=[]
    while n>0:
      rem=n%2
      s.append(str(rem))
      n=n//2
    return s

n=int(input())
b=binary(n)
b=b[::-1]
rem=8-len(b)
for i in range(rem):
    b.insert(0,'0')

#b=''.join(b)
swapped=b[4:]+b[0:4]
print(dec(swapped))
