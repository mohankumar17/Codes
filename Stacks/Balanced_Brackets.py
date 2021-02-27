def isValid(exp):
    s=[]
    open=['[','{','(']
    
    for i in exp:
        if i in open:
            s.append(i)
        else:
            if len(s)==0:
                return False
            x=s.pop()
            if x=='[':
                if i=='}' or i==')':
                    return False
            if x=='{':
                if i==']' or i==')':
                    return False
            if x=='(':
                if i=='}' or i==']':
                    return False

    if len(s):
        return False
    else:
        return True

exp=input()
print(isValid(exp))
