def isValid(s):
    if len(s)==0:
        return True
    if len(s)==1:
        return False
    st=[]
    open=['{','(','[']
    closed=['}',')',']']
    if s[0] in closed:
        return False

    for i in s:
        if i in open:
            st.append(i)
        if i in closed:
            x=st.pop()
            if i=='}':
                if x=='(' or x=='[':
                    return False
            elif i==']':
                if x=='{' or x=='(':
                    return False
            elif i==')':
                if x=='{' or x=='[':
                    return False

    if len(st):
        return False
    else:
        return True

s=input()
print(isValid(s))
