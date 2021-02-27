import sys
def closeSum(ar,s):
    n=len(ar)
    m=sys.maxsize
    ans=[-1,-1]
    for i in range(n):
        for j in range(i+1,n):
            d=abs(s-(ar[i]+ar[j]))
            if d<m:
                m=d
                ans=[ar[i],ar[j]]
    return ans

def closeSum2(ar,s):
    n=len(ar)
    m=sys.maxsize
    ans=[-1,-1]
    l=0
    r=n-1
    while l<r:
        d=abs(s-(ar[l]+ar[r]))
        if d<m:
            m=d
            ans=[ar[l],ar[r]]
        if ar[l]+ar[r]<s:
            l=l+1
        else:
            r=r-1

    return ans

ar=[20,22,28,29,30,40]
s=54
#ans=closeSum(ar,s)
ans=closeSum2(ar,s)
print(ans)
