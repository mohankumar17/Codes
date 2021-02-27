t=int(input())
while t>0:
  d={}
  n=int(input())
  s=input()
  for i in s:
    d[i]=d.get(i,0)+1

  if len(d)==1:
    m=0
  else:
    m=min(d['c'],d['v'])

  if len(s)==8:
    m=2
  print(2*m)
  t-=1
