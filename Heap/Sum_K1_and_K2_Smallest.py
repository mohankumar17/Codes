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

def min_heap(ar):
    n=len(ar)
    for i in range(n//2-1,-1,-1):
        min_heapify(ar,i,n)

def heappop(ar):
    if len(ar)==0:
        return 0
    return ar.pop(0)


ar=[3,8,2,1,6]
k1=int(input())
k2=int(input())
k2=k2-k1

min_heap(ar)
print(ar)
ans=0
while k1>0:
    heappop(ar)
    k1=k1-1
    min_heap(ar)
print(ar)

while k2>1:
    ans+=heappop(ar)
    k2=k2-1
    min_heap(ar)

print(ans)
