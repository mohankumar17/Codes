n=int(input())
ar=list(map(int,input().split()))
i=0
f=0
c=0
while i<n-1:
  if f==0:
    if ar[i]<ar[i+1]:
      b=ar[i]
      f=1
  else:
    if ar[i]>ar[i+1]:
      f=0
      c=c+(ar[i]-b)
  i=i+1

c=c+(ar[i]-b)
print(c)
