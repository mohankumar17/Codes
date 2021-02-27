m=int(input())
q=int(input())
n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
  d[i]=d.get(i,0)+1

ar1=[]
ar2=[]

while q>0:
  q-=1
  for i in a:
    ar1.append(i+m)
    ar2.append(m-i)

ar=ar1+ar2
for i in ar:
  d[i]=d.get(i,0)+1
m=0
for i in d:
  if d[i]>m:
    m=d[i]
print(d)
