def interPolSearch(ar,k):
    l=0
    h=len(ar)-1
    while l<=h and (k>=ar[l] and k<=ar[h]):
        if l==h:
            if ar[l]==k:
                return l
            return -1

        pos=l+int(float((h-l)/(ar[h]-ar[l])*(k-ar[l])))   #probing
        if ar[pos]==k:
            return pos
        elif k<ar[pos]:
            h=pos-1
        else:
            l=pos+1

    return -1


ar=[11,12,13,14,15]
k=int(input())
ans=interPolSearch(ar,k)
print(ans)
#Time complexity : O(sqrt(n))
