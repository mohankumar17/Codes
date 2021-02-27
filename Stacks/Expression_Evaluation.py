def compute(a,b,i):
    if i=='+':
        return b+a
    elif i=='-':
        return b-a
    elif i=='*':
        return b*a
    elif i=='/':
        return b//a

def evalExp(exp):
    s=[]
    for i in exp:
        if ord(i)>=48 and ord(i)<=57:
            s.append(i)
        else:
            a=s.pop()
            b=s.pop()
            c=compute(int(a),int(b),i)
            s.append(c)
    return s[-1]

exp=input()
print(evalExp(exp))
