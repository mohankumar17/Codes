def max_heapify(ar,i,n):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<n and ar[left]>ar[largest]:
        largest=left
    if right<n and ar[right]>ar[largest]:
        largest=right

    if largest!=i:
        ar[i],ar[largest]=ar[largest],ar[i]
        max_heapify(ar,largest,n)

##################################################
def min_heapify(ar,i,n):
    smallest=i
    left=2*i+1
    right=2*i+2

    if left<n and ar[left]<ar[smallest]:
        smallest=left
    if right<n and ar[right]<ar[smallest]:
        smallest=right

    if smallest!=i:
        ar[i],ar[smallest]=ar[smallest],ar[i]
        min_heapify(ar,smallest,n)

################################################

def max_heap(ar):
    n=len(ar)
    for i in range(n//2-1,-1,-1):
        max_heapify(ar,i,n)

def min_heap(ar):
    n=len(ar)
    for i in range(n//2-1,-1,-1):
        min_heapify(ar,i,n)

def heappop(ar):
    if len(ar)==0:
        return -1
    return ar.pop(0)

ar=[3,8,2,1,6]
#max_heap(ar)
min_heap(ar)
print(ar)

ans=0
while ans!=-1:
    ans=heappop(ar)
    print(ans,end=' ')
    min_heap(ar)
