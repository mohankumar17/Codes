class CircularQueue:
    def __init__(self,n):
        self.n=n
        self.q=[None]*n
        self.front=-1
        self.rear=-1

    def push(self,val):
        if (self.rear+1)%self.n==self.front:
            print('Queue is Full')
            return -1
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.q[self.rear]=val
        else:
            self.rear=(self.rear+1)%self.n
            self.q[self.rear]=val

    def pop_(self):
        if self.front==-1:
            print('Queue is Empty')
            return -1
        elif self.front==self.rear:
            temp=self.q[self.front]
            self.front=-1
            self.rear=-1
            return temp

        else:
            temp=self.q[self.front]
            self.front=(self.front+1)%self.n
            return temp

    def display(self):
        return self.q

ob=CircularQueue(4)
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
