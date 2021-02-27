from itertools import combinations
n=int(input())
l=list(map(int,input().split()))
t=[]

for i in range(n+1,0,-1):
  c=combinations(l,i)
  for h in c:
    t.append(h)
for i in t:
  print(i)
