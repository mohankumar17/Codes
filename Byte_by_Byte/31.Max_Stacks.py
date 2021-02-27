class Stack:
    def __init__(self):
        self.s=[]
        self.m=[]
    def push(self,val):
        self.s.append(val)
        if len(self.m)==0 or val>self.m[-1]:
            self.m.append(val)

    def pop(self):
        if len(self.s)==0:
            return -1
        x=self.s.pop()
        if len(self.m) and x==self.m[-1]:
            self.m.pop()
        return x

    def max(self):
        return self.m[-1]

ob=Stack()
ob.push(1)
print(ob.pop())
print(ob.pop())

ob.push(1)
ob.push(2)
print(ob.max())
ob.push(3)
print(ob.max())
print(ob.pop())
print(ob.max())
print(ob.pop())
print(ob.pop())
print(ob.pop())
