#Linear Search-O(n)
def linear(ar,key):
    for i in range(0,len(ar)):
        if ar[i]==key:
            return i
    return -1

#Binary Search-O(logn)
def binary(ar,key):
    low=0
    high=len(ar)-1
    while low<=high:
        mid=(low+high)//2
        if ar[mid]==key:
            return mid
        elif key<ar[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

ar=[2,3,4,5,7]
#key=int(input())
#print(linear(ar,key))
print(binary(ar,key))
