class Stack:
    def __init__(self):
        self.s=[]
    def push(self,val):
        self.s.append(val)
    def pop(self):
        if len(self.s)==0:
            return -1
        return self.s.pop()
    def display(self):
        return self.s

ob=Stack()
while True:
    ch=int(input())
    if ch==1:
        ob.push(int(input()))
    elif ch==2:
        print(ob.pop())
    elif ch==3:
        print(ob.display())
    else:
        break
