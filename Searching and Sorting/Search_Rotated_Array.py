def search(ar,n,k,l,h):
    if l>h:
        return -1

    mid=(l+h)//2
    if ar[mid]==k:
        return mid

    if ar[l]<=ar[mid]:
        if k>=ar[l] and k<=ar[mid]:
            return search(ar,n,k,l,mid-1)
        return search(ar,n,k,mid+1,h)
    
    if k>=ar[mid] and k<=ar[h]:
        return search(ar,n,k,mid+1,h)
    return search(ar,n,k,l,mid-1)


t=int(input())
while t>0:
    t-=1
    n=int(input())
    ar=list(map(int,input().split()))
    k=int(input())
    ans=search(ar,n,k,0,n-1)
    print(ans)
