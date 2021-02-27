n=int(input())
ar=list(map(int,input().split()))
d1=ar[1]-ar[0]
d2=ar[n-1]-ar[n-2]
l1=[ar[0]]
l2=[ar[0]]
for i in range(0,n-1):
  if ar[i]+d1<=ar[n-1] and ar[i]+d1<=ar[n-1]:
    l1.append(ar[i]+d1)
    l2.append(ar[i]+d2)
l=l1+l2
l=list(set(l))
l.sort()
for i in l:
  if i not in ar:
    print(i)
    break
