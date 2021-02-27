q=[1,2,3,4,5]
#s=[i for i in q]

s=[q[i] for i in range(len(q))]

for i in range(len(q)-1,-1,-1):
    q[i]=s.pop(0)

print(q)
