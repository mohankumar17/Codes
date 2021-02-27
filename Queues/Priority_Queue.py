class PriorityQueue:
    def __init__(self):
        self.q=[]
    def push(self,val):
        self.q.append(val)
    def pop_(self):
        if len(self.q)==0:
            return -1
        max=0
        for i in range(0,len(self.q)):
            if self.q[i]>self.q[max]:
                max=i
        return self.q.pop(max)

    def display(self):
        return self.q

ob=PriorityQueue()
while True:
    ch=int(input())
    if ch==1:
        ob.push(int(input()))
    elif ch==2:
        print(ob.pop_())
    elif ch==3:
        print(ob.display())
    else:
        break
