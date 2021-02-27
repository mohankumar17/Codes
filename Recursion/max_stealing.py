def func(l,n):
  if n==0:
    return 0
  value1=l[0]
  if n==1:
    return value1
  value2=max(l[0],l[1])
  if n==2:
    return value2
  max_val=0
  for i in range(2,n):
    max_val=max(l[i]+value1,value2)
    value1=value2
    value2=max_val
  return max_val

n=int(input())
l=list(map(int,input().split()))
print(func(l,n))
