def bins(ar,e):
    ar.sort()
    f=0
    l=len(ar)-1

    while f<=l:
        mid=(f+l+1)//2
        if ar[mid]==e:
            return mid
        elif e<ar[mid]:
            l=mid-1
        elif e>ar[mid]:
            f=mid+1
    return -1

ar=list(map(int,input().split()))
e=int(input())
pos=bins(ar,e)
print(pos)
#Time complexity : O(log(n))
