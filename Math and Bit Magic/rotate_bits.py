def binary(n):
    s=[]
    while n>0:
      rem=n%2
      s.append(str(rem))
      n=n//2
    return s

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


n=int(input())
d=int(input())
s=binary(n)

r=16-len(s)
s=s[::-1]
for i in range(r):
  s.insert(0,str(0))

left=[i for i in s]
right=[i for i in s]

s=''.join(s)

while d>0:
  left.append(left[0])
  left.pop(0)

  right.insert(0,right[-1])
  right.pop()

  d-=1

left=''.join(left)
right=''.join(right)

print(left)
print(right)
print(dec(left))
print(dec(right))
