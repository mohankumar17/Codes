
n=int(input())
r1=list(input().split())
r1=ord(r1[1])-ord(r1[0])+1
r2=list(input().split())
r2=int(r2[1])-int(r2[0])+1
res=n*(r1**2)*(r2**4)
print(res)
