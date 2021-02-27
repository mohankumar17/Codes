def perm(ar,ans,l,r,n):
    if l==r:
        x=[i for i in ar]
        ans.append(x)
    else:
        for i in range(l,r+1):
            ar[i],ar[l]=ar[l],ar[i]
            perm(ar,ans,l+1,r,n)
            ar[i],ar[l]=ar[l],ar[i]

ar=[1,2,3]
ans=[]
n=len(ar)
l=0
r=n-1
perm(ar,ans,l,r,n)
print(ans)
