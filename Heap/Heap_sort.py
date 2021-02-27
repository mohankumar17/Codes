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

def heap_sort(ar):
	n=len(ar)
	for i in range(n//2-1,-1,-1):
		max_heapify(ar,i,n)

	for i in range(n-1,0,-1):
		ar[0],ar[i]=ar[i],ar[0]
		max_heapify(ar,0,i)

ar=[3,8,2,1,6]
heap_sort(ar)
print(ar)
