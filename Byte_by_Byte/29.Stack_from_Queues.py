def func(q):
    s=[]
    while len(q):
        x=q.pop(0)
        s.append(x)
    return s
        
q=[1,2,3]
print(func(q))
