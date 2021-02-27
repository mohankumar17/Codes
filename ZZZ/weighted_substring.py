from collections import OrderedDict
def weightString(n):
  d=OrderedDict()
  d['A']=1
  d['B']=3
  p='B'
  i=2
  while d[p]<=n:
    c=chr(ord(p)+1)
    d[c]=(i+1)*d[p]+d[p]
    p=c
    i=i+1
  d.pop(p)
  return d

n=int(input())
ans=weightString(n)
print(ans)
