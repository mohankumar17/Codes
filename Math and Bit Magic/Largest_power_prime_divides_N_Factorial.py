import math
t=int(input())
while t>0:
  n,p=map(int,input().split())
  m=0
  while n!=0:
    n=n//p
    m=m+n
  print(m)
  t=t-1
