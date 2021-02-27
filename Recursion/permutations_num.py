def perm(ar,l,r,ans):
    if l==r:
        a=''.join(ar)
        ans.append(a)
    else:
        for i in range(l,r+1):
            ar[i],ar[l]=ar[l],ar[i]
            perm(ar,l+1,r,ans)
            ar[i],ar[l]=ar[l],ar[i]

ar=[1,2,3]
ans=[]
l=0
r=len(ar)-1
ar=[str(i) for i in ar]
perm(ar,l,r,ans)
print(ans)
