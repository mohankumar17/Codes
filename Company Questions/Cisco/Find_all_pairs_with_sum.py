def func(arr,sum):
    ans=[]
    low=0
    high=len(arr)-1
    while low<high:
        l=[]
        if arr[low]+arr[high]==sum:
            l.append(arr[low])
            l.append(arr[high])
            ans.append(l)
        if arr[low]+arr[high]>sum:
            high=high-1
        else:
            low=low+1
    return ans


arr=[1,2,3,7,8]
s=10
print(func(arr,s))
