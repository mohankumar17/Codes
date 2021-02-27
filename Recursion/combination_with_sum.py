from itertools import combinations

def func(n,l,s):
  for i in range(1,n+1):
    c=combinations(l,i)
    for h in c:
      if sum(h)==s:
        return 1
  return 0

n=int(input())
l=list(map(int,input().split()))
s=int(input())
a=func(n,l,s)
print("Combination Found =",a)



  
