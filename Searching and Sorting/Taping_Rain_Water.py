def findWater(arr):
    n=len(arr)
    low=0
    high=n-1
    lmax=0
    rmax=0
    res=0
    while low<=high:
        if arr[low]<arr[high]:
            if arr[low]>lmax:
                lmax=arr[low]
            else:
                res=res+(lmax-arr[low])
            low+=1
        else:
            if arr[high]>rmax:
                rmax=arr[high]
            else:
                res=res+(rmax-arr[high])
            high-=1

    return res

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print("Maximum water that can be accumulated is ",findWater(arr))
