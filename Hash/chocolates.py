import math
n=int(input())
ar=list(map(int,input().split()))
k=int(input())

while k>0:
  m=max(ar)
  ar.remove(m)
  s=math.sqrt(m)
  ar.append(int(s))
  k-=1
print(sum(ar))
