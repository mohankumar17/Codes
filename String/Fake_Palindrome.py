def fake(s):
  l=[]
  for i in range(len(s)):
    if s[i] in l:
      l.remove(s[i])
    else:
      l.append(s[i])
  if (len(s)%2==0 and len(l)==0) or (len(s)%2==1 and len(l)==1):
    return True
  return False

s=input()
n=len(s)
i=0
c=n
for l in range(2,n+1):
  for i in range(0,n-l+1):
    j=i+l
    if fake(s[i:j]):
      c=c+1
print(c)
