def func(S,T):
    s=[]
    t=[]
    for i in S:
        if i=='#':
            s.pop()
        else:
            s.append(i)
    for i in T:
        if i=='#':
            t.pop()
        else:
            t.append(i)
    s=''.join(s)
    t=''.join(t)
    if s==t:
        return True
    else:
        return False


S=input()
T=input()
print(func(S,T))
