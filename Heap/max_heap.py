#minheap by default, add -1 to each element to form maxheap
from heapq import heapify,heappush,heappop
heap=[]
heapify(heap)

l=list(map(int,input().split()))
for i in l:
    heappush(heap,(-1*i))

for i in heap:
    print((-1*i),end=' ')
print()
print('Maximum element if heap:',-1*heap[0])

while len(heap):
    x=heappop(heap)
    print(-1*x,end=' ')
