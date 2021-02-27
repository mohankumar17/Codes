#O(n^2)
def bubble(ar):
    for i in range(len(ar)):
        s=False
        for j in range(i+1,len(ar)):
            if ar[i]>ar[j]:
                ar[i],ar[j]=ar[j],ar[i]
                s=True
        if s==False:
            break

#O(n^2)
def selection(ar):
    for i in range(len(ar)):
        m=ar[i]
        t=i
        for j in range(i+1,len(ar)):
            if ar[j]<m:
                m=ar[j]
                t=j
        ar[i],ar[t]=ar[t],ar[i]

#O(n^2)
def insertion(ar):
    for i in range(0,len(ar)):
        key=ar[i]
        j=i-1
        while j>=0 and key<ar[j]:
            ar[j+1]=ar[j]
            j=j-1
        ar[j+1]=key

#O(nlogn)
def mergesort(ar):
    if len(ar)>1:
        mid=len(ar)//2
        left=mergesort(ar[:mid])
        right=mergesort(ar[mid:])
        i=0
        while len(left)>0 and len(right)>0:
            if left[0]<right[0]:
                ar[i]=left.pop(0)
            else:
                ar[i]=right.pop(0)
            i=i+1
        while len(left)>0:
            ar[i]=left.pop(0)
            i=i+1
        while len(right)>0:
            ar[i]=right.pop(0)
            i=i+1
    return ar

#Avg-O(nlogn) and worst-O(n^2)
def qs(ar,low,high):
    pivot=ar[high]
    i=low-1
    for j in range(low,high):
        if ar[j]<pivot:
            i=i+1
            ar[i],ar[j]=ar[j],ar[i]
    ar[i+1],ar[high]=ar[high],ar[i+1]
    return i+1

def quicksort(ar,low,high):
    if low<high:
        pi=qs(ar,low,high)
        quicksort(ar,low,pi-1)
        quicksort(ar,pi+1,high)

#O(nlogn)
def heapify(ar,i,n):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and ar[i]<ar[left]:
        largest=left
    if right<n and ar[largest]<ar[right]:
        largest=right

    if largest!=i:
        ar[i],ar[largest]=ar[largest],ar[i]
        heapify(ar,largest,n)

def heapsort(ar):
    n=len(ar)
    for i in range(n//2-1,-1,-1):
        heapify(ar,i,n)

    for i in range(n-1,0,-1):
        ar[i],ar[0]=ar[0],ar[i]
        heapify(ar,0,i)

ar=[5,8,3,7,1,6]
#bubble(ar)
#selection(ar)
#insertion(ar)
#mergesort(ar)
#quicksort(ar,0,len(ar)-1)
heapsort(ar)
print(ar)
