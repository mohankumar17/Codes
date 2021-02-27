class Stack:
    def __init__(self,N,capacity):
        self.N=N
        self.capacity=capacity
        self.stack=[[] for i in range(N)]
    def put(self,st,element):
        if len(self.stack[st])>self.capacity:
            return -1
        self.stack[st].append(element)

    def pop(self,st):
        if len(self.stack[st])==0:
            return -1
        return self.stack[st].pop()

N=3
capacity=10
s=Stack(N,capacity)
s.put(0,10)
s.put(2,11)
print(s.pop(0))
print(s.pop(2))
print(s.pop(1))
