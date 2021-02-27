from itertools import permutations

l=list(map(int,input().split()))
p=permutations(l)
m=0
for s in p:
    t=list(map(str,s))
    t=''.join(t)
    t=int(t)
    #print(t)
    if t>m:
        m=t
print(m)
