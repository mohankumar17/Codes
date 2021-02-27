from queue import PriorityQueue
p=PriorityQueue()

p.put((2,3))
p.put((1,5))
p.put((3,6))
p.put((5,4))
p.put((4,8))

#print(q.empty())
#print(q.full())

while p.qsize():
    print(p.get()[1],end=' ')
