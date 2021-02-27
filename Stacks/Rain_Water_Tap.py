def maxRain(ar):
    n=len(ar)
    l=0
    r=n-1
    left=0
    right=0
    ans=0
    while l<=r:
        if ar[l]<ar[r]:
            if ar[l]>left:
                left=ar[l]
            else:
                ans=ans+(left-ar[l])
            l=l+1
        else:
            if ar[r]>right:
                right=ar[r]
            else:
                ans=ans+(right-ar[r])
            r=r-1
    return ans

ar=[3,0,2,0,2,1,0,3,1]
print(maxRain(ar))
