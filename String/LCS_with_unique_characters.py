s=input()
t=[]
l=[]
for i in s:
  if i not in l:
    l.append(i)
  else:
    l=''.join(l)
    t.append(l)
    l=[]
#print(t)
m=0
for i in t:
  if len(i)>m:
    m=len(i)
print(m)
  
