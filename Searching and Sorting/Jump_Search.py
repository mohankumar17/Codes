def jumpSearch(ar,k):
    n=len(ar)
    prev=0
    step=int((n)*(1/2))
    while ar[int(min(step,n)-1)]<k:
        prev=step
        step=step+int((n)*(1/2))  #skip some elements (jumping)
        if prev>=n:
            return -1

    while ar[prev]<k:
        prev=prev+1
        if prev==min(step,n):
            return -1
    if ar[prev]==k:
        return prev
    return -1

ar=[11,12,13,14,15]
k=int(input())
ans=jumpSearch(ar,k)
print(ans)
#Time complexity : O(sqrt(n))
