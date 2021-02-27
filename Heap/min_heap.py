#minheap by default
from heapq import heapify,heappush,heappop
heap=[]
heapify(heap)

l=list(map(int,input().split()))
for i in l:
    heappush(heap,i)

for i in heap:
    print(i,end=' ')
print()
print('Minimum element if heap:',heap[0])

while len(heap):
    x=heappop(heap)
    print(x,end=' ')
