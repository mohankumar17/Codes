def sortStack(s):
    t=[]
    while len(s):
        temp=s.pop()
        while len(t) and t[-1]>temp:
            x=t.pop()
            s.append(x)

        t.append(temp)
    return t

s=[6,1,3,5,2,4]
print(sortStack(s))
