n=int(input())
a=list(map(int,input().split()))
avg=sum(a)//n
b=[0]*n
for i in range(n-1):
  b[i+1]=a[i]+b[i]-avg
b.sort()
#print(b)
m=-(b[n//2])
ans=0
for i in range(n):
  ans=ans+abs(m+b[i])
print(ans)
