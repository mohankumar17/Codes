def func(arr,n):
    count=[0 for i in range(10)]
    for i in range(n):
        j=arr[i]
        while j>=0:
            count[arr[i]]+=count[j]
            j-=1
        count[arr[i]]+=1
    s=0
    for i in range(10):
        s=s+count[i]
    return s


arr = [1,4,3,7]
#find no of subsequences so that every digit in each subsequence is greater than its previous digit
print(func(arr,len(arr)))
