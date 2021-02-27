from heapq import heapify,heappush,heappop
def kthSmallest(arr,k):
    h=[]
    heapify(h)
    for i in arr:
        heappush(h,i)
    #print(h)
    while k>0:
        x=heappop(h)
        heapify(h)
        k-=1
    #print(h)
    return x
    #arr.sort()
    #return arr[k-1]

arr=[3,5,7,4,2,8,6]
#arr=[2,3,4,5,6,7,8]
for k in range(1,8):
    print(kthSmallest(arr,k),end=' ')
