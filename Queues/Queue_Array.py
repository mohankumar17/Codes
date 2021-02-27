class Queue:
    def __init__(self):
        self.q=[]
    def push(self,val):
        self.q.append(val)
    def pop(self):
        if len(self.q)==0:
            return -1
        return self.q.pop(0)
    def display(self):
        return self.q

ob=Queue()
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
