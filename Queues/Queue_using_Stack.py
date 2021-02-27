s=[1,2,3,4,5]
t=[]
q=[]

while len(s):
    t.append(s.pop())
while len(t):
    q.append(t.pop())
print(q)
print(q.pop(0))
